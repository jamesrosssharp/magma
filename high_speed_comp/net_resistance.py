import re
import sys
import argparse
from collections import defaultdict

import numpy as np

# Parasitic resistance of each net in a Magic PEX spice netlist.
# Magic names extracted sub-nodes <net>.n<k> / <net>.t<k> (t = device
# terminal), so the net is recovered by stripping that suffix.
#
# For each net the effective (point-to-point) resistance is computed by
# solving the resistor network:
#   - root given with --root: resistance from that node to every terminal
#   - net has both source/drain and gate terminals (a signal net):
#       drivers (source/drain terminals) are shorted together and the
#       resistance from them to every gate terminal is reported
#   - bare <net> node (port/label) present: resistance from it to every terminal
#   - otherwise (supply ports): worst-case terminal-to-terminal resistance

SUFFIXES = {
    't': 1e12, 'g': 1e9, 'meg': 1e6, 'k': 1e3,
    'm': 1e-3, 'u': 1e-6, 'n': 1e-9, 'p': 1e-12, 'f': 1e-15,
}

def parse_value(s):
    s = s.lower()
    if '=' in s:
        s = s.split('=', 1)[1]
    m = re.match(r'^([-+]?[0-9.]+(?:e[-+]?[0-9]+)?)(meg|[tgkmunpf])?', s)
    if not m:
        raise ValueError("Can't parse resistor value: " + s)
    return float(m.group(1)) * SUFFIXES.get(m.group(2), 1.0)

def net_name(node):
    return re.sub(r'\.[nt][0-9]+$', '', node)

def parse_netlist(fname):
    resistors = defaultdict(list)   # net -> [(n1, n2, R)]
    terminals = defaultdict(list)   # node -> [(device, role)]
    ports = set()
    roles = {1: 'd', 2: 'g', 3: 's', 4: 'b'}

    with open(fname) as f:
        for line in f:
            tok = line.split()
            if not tok:
                continue
            kind = tok[0][0].upper()
            if tok[0].lower() == '.subckt':
                ports.update(tok[2:])
            elif kind == 'R' and len(tok) >= 4:
                n1 = net_name(tok[1])
                if n1 != net_name(tok[2]):
                    print("Warning: %s bridges nets %s and %s" % (tok[0], n1, net_name(tok[2])))
                resistors[n1].append((tok[1], tok[2], parse_value(tok[3])))
            elif kind == 'X' and len(tok) >= 6:
                for i in range(1, 5):
                    terminals[tok[i]].append((tok[0], roles[i]))

    return resistors, terminals, ports

def solve(res, root_nodes):
    """Short root_nodes together, ground them and return {node: R to root}."""
    root = '<root>'
    def m(n):
        return root if n in root_nodes else n

    nodes = set()
    for n1, n2, _ in res:
        nodes.add(m(n1))
        nodes.add(m(n2))
    nodes.discard(root)
    idx = dict((n, i) for i, n in enumerate(sorted(nodes)))

    G = np.zeros((len(idx), len(idx)))
    for n1, n2, r in res:
        a, b = m(n1), m(n2)
        if a == b:
            continue
        g = 1.0 / r
        for x, y in ((a, b), (b, a)):
            if x != root:
                G[idx[x], idx[x]] += g
                if y != root:
                    G[idx[x], idx[y]] -= g

    # Nodes not connected to root make G singular; report them as inf
    Rinv = np.linalg.pinv(G)
    reach = reachable(res, root_nodes)
    out = dict((n, Rinv[i, i] if n in reach else float('inf')) for n, i in idx.items())
    for n in root_nodes:
        out[n] = 0.0
    return out

def reachable(res, start):
    adj = defaultdict(set)
    for n1, n2, _ in res:
        adj[n1].add(n2)
        adj[n2].add(n1)
    seen = set()
    stack = list(start)
    while stack:
        n = stack.pop()
        if n not in seen:
            seen.add(n)
            stack.extend(adj[n])
    return seen

def pairwise_worst(res, nodes):
    """Largest effective resistance between any two of nodes."""
    worst = (0.0, None, None)
    nodes = sorted(nodes)
    for i, a in enumerate(nodes[:-1]):
        r = solve(res, set([a]))
        for b in nodes[i + 1:]:
            if r[b] > worst[0]:
                worst = (r[b], a, b)
    return worst

def describe(node, terminals):
    return ' '.join('%s.%s' % t for t in terminals[node])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('netlist', nargs='?', default="high_speed_comp_top_routed.pex.spice")
    ap.add_argument('--root', action='append', default=[],
                    help="NET=NODE, measure from NODE on NET (repeatable)")
    ap.add_argument('-v', '--verbose', action='store_true',
                    help="list the resistance to every terminal")
    args = ap.parse_args()

    resistors, terminals, ports = parse_netlist(args.netlist)
    user_roots = dict(r.split('=', 1) for r in args.root)

    print("%-12s %5s %12s  %s" % ("Net", "Rs", "Sum R (ohm)", "Effective resistance"))
    for net in sorted(resistors, key=lambda n: -len(resistors[n])):
        res = resistors[net]
        total = sum(r for _, _, r in res)
        nodes = set(n for r in res for n in r[:2])
        terms = sorted(n for n in nodes if n in terminals)
        drivers = [n for n in terms if any(role in 'ds' for _, role in terminals[n])]
        loads = [n for n in terms if any(role == 'g' for _, role in terminals[n])]

        if net in ports and net not in nodes:
            print("Warning: port %s is not connected to any %s.* node" % (net, net))

        if net in user_roots:
            root = user_roots[net]
            r = solve(res, set([root]))
            targets = [n for n in terms if n != root]
            how = "from %s" % root
        elif drivers and loads and net not in ports:
            r = solve(res, set(drivers))
            targets = loads
            how = "drivers (%d S/D) -> gates" % len(drivers)
        elif net in nodes:
            r = solve(res, set([net]))
            targets = terms
            how = "from port node %s" % net
        else:
            worst, a, b = pairwise_worst(res, terms)
            print("%-12s %5d %12.3f  worst terminal-terminal %.3f (%s <-> %s)"
                  % (net, len(res), total, worst, a, b))
            if args.verbose:
                print("    %s: %s\n    %s: %s" % (a, describe(a, terminals), b, describe(b, terminals)))
            continue

        vals = [r[n] for n in targets]
        print("%-12s %5d %12.3f  %s: min %.3f  mean %.3f  max %.3f"
              % (net, len(res), total, how, min(vals), sum(vals) / len(vals), max(vals)))
        if args.verbose:
            for n in sorted(targets, key=lambda n: -r[n]):
                print("    %-14s %10.3f  %s" % (n, r[n], describe(n, terminals)))

if __name__ == "__main__":
    main()
