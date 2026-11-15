# 1bit_am LVS mismatch summary

Comparison of `1bit_am_routed.lvs.out.spice` (layout, netgen Circuit 1) against
`1bit_am_routed.xschem.out.spice` (schematic, Circuit 2), based on `comp.out`.

All subcells (`strong_arm_latch`, `post_amplifier`, standard cells) and transistor
counts match. The failures are all at the `1bit_am_routed` top level. The final
"Top level cell failed pin matching" is a consequence of the issues below, not a
separate problem.

## 1. Layout short: second inverter output tied to VSS

Schematic:

```
x3 PWM_IN ... net1  inv_1      ; first inverter
x2 net1   ... net10 inv_1      ; second inverter -> net10
XR1 net10 net11 ...            ; feeds R1-R7-R8-R2 chain to NET_PWM
```

Layout:

```
Xx2 PWM_IN ... x3/A  inv_1
Xx3 x3/A   ... VSS   inv_1     ; output Y is on VSS
XXR1 VSS XR7/R2 VSS            ; R1's far end is also on VSS
```

The inverter-output / R1 net has merged into VSS (netgen: extra `inv_1/Y = 1` on
VSS, missing `net10`). The only labels in `1bit_am_routed.mag` are the six ports,
so this is a physical short. Check metal1/li around the Y pin of instance `x3`
and the adjacent end of `XR1`.

Note: instance names `x2`/`x3` are swapped between layout and schematic
(harmless for LVS, but confusing when cross-probing).

**Fix:** remove the short in layout.

## 2. Resistor body (B) terminals floating in schematic

Layout ties every `res_xhigh_po` body pin to VSS. The schematic leaves each one on
its own unconnected net (`net3, net5, net6, net8, net9, net12, net14, net15`),
which are the eight `(no matching net)` entries with `res_xhigh_po_0p35/3 = 1`.

As a result, netgen series-merges the layout resistors (8 -> 3) but cannot merge the
schematic ones (8), giving the 29 vs 34 device-count mismatch.

**Fix:** in `xschem/1bit_am/1bit_am.sch`, connect the B pin of R1-R8 to VSS.

## 3. XC1 polarity reversed

- Schematic: `XC1 VIN NET_IN`, so VIN is on terminal 1 (C1) and NET_IN on terminal 2 (C2).
- Layout: `XXC1` has VIN on the C2 pins and NET_IN (`XR5/R2`) on the C1 pins.

Netgen reports `VIN: cap_mim_m3_1/2` (layout) vs `cap_mim_m3_1/1` (schematic).
XC2 is consistent.

**Fix:** either swap the C1 pins in the schematic, or swap the plate
connections of XC1 in the layout, whichever matches the intended orientation.

## Not issues

- The `tapvpwrvgnd_1` cells in the schematic are absent from the layout. They contain
  no devices and are flattened away.
- The resistor divider VDD-R3-R4-NET_IN-R5-R6-VSS matches.
- The comparator inputs (VINP = NET_IN, VINN = NET_PWM) match.
- The MIM cap sizes and multiplicity (20 x 10x10) match.

After fixing issues 1-3, rerun `run_lvs.sh`.
