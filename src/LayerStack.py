"""
Physical layer stack used to give Magic layers a vertical (z) extent.

Magic .mag files are 2D: each rect is tagged with a Magic layer name
(e.g. 'metal1', 'viali', 'ndiffc').  This module maps those names onto
the process cross-section so a cell can be rendered (or exported) in 3D.

Heights are taken from the SkyWater sky130 metal stack (um above the
substrate surface).  Contact types in Magic occupy both the lower and
upper conductor planes, so they span from the bottom of the lower layer
to the top of the upper layer.
"""

from collections import namedtuple

# Magic sky130A tech is saved with "magscale 1 2": one database unit is
# half a lambda, i.e. 0.005 um.
DB_UNIT_UM = 0.005

# z0, z1 in um; colour as (r, g, b, a)
Layer = namedtuple("Layer", ["name", "z0", "z1", "color", "visible"])

# Conductor plane extents (bottom, top) in um
_DIFF   = (0.000, 0.120)
_POLY   = (0.3262, 0.5062)
_LI     = (0.9361, 1.0361)
_MET1   = (1.3761, 1.7361)
_MET2   = (2.0061, 2.3661)
_MET3   = (2.7861, 3.6311)
_MET4   = (4.0211, 4.8661)
_MET5   = (5.3711, 6.6311)

# MiM capacitor top plates.  sky130A-extract.tech gives each plate a 0.1 um
# dielectric gap above its bottom-plate metal and a 0.2 um thickness, but its
# absolute z values (mimcap 2.4661, mimcap2 3.7311) sit one metal level too
# low (above met2/met3 rather than met3/met4).  Use the PDK offsets relative
# to the correct bottom plate so the contacts reach the metal above.
_MIM_GAP, _MIM_THICK = 0.1, 0.2
_MIMCAP  = (_MET3[1] + _MIM_GAP, _MET3[1] + _MIM_GAP + _MIM_THICK)
_MIMCAP2 = (_MET4[1] + _MIM_GAP, _MET4[1] + _MIM_GAP + _MIM_THICK)

_NDIFF_COL   = (0.25, 0.70, 0.30, 1.0)
_PDIFF_COL   = (0.75, 0.60, 0.25, 1.0)
_CHAN_COL    = (0.80, 0.45, 0.20, 1.0)
_CONT_COL    = (0.70, 0.70, 0.74, 1.0)


def _span(lower, upper):
    return (lower[0], upper[1])


SKY130_LAYERS = [
    # Wells: thin translucent slab just below the surface, hidden by default
    Layer("nwell",        -0.20, -0.01, (0.35, 0.55, 0.35, 0.18), False),
    Layer("pwell",        -0.20, -0.01, (0.55, 0.40, 0.35, 0.18), False),
    Layer("dnwell",       -0.40, -0.21, (0.25, 0.45, 0.25, 0.18), False),

    # Diffusion and device channels
    Layer("ndiff",        *_DIFF, _NDIFF_COL, True),
    Layer("pdiff",        *_DIFF, _PDIFF_COL, True),
    Layer("nsubdiff",     *_DIFF, (0.20, 0.55, 0.45, 1.0), True),
    Layer("psubdiff",     *_DIFF, (0.60, 0.50, 0.35, 1.0), True),
    Layer("nmos",         *_DIFF, _CHAN_COL, True),
    Layer("pmos",         *_DIFF, _CHAN_COL, True),
    Layer("nmoslvt",      *_DIFF, _CHAN_COL, True),
    Layer("pmoslvt",      *_DIFF, _CHAN_COL, True),
    Layer("pmoshvt",      *_DIFF, _CHAN_COL, True),
    Layer("nmoshvt",      *_DIFF, _CHAN_COL, True),
    Layer("varactor",     *_DIFF, _CHAN_COL, True),

    # Diffusion -> local interconnect contacts (licon)
    Layer("ndiffc",       *_span(_DIFF, _LI), _CONT_COL, True),
    Layer("pdiffc",       *_span(_DIFF, _LI), _CONT_COL, True),
    Layer("nsubdiffcont", *_span(_DIFF, _LI), _CONT_COL, True),
    Layer("psubdiffcont", *_span(_DIFF, _LI), _CONT_COL, True),

    Layer("poly",         *_POLY, (0.85, 0.20, 0.20, 1.0), True),
    Layer("polycont",     *_span(_POLY, _LI), _CONT_COL, True),
    # High-sheet-resistance poly resistor body and its contact (xhrpoly is
    # in the PDK's allpoly alias, so it shares the poly height)
    Layer("xpolyres",     *_POLY, (0.60, 0.15, 0.40, 1.0), True),
    Layer("xpolycontact", *_span(_POLY, _LI), _CONT_COL, True),

    Layer("locali",       *_LI,   (0.55, 0.40, 0.80, 1.0), True),
    Layer("viali",        *_span(_LI, _MET1), _CONT_COL, True),

    Layer("metal1",       *_MET1, (0.30, 0.55, 0.95, 1.0), True),
    Layer("via1",         *_span(_MET1, _MET2), _CONT_COL, True),
    Layer("metal2",       *_MET2, (0.85, 0.35, 0.85, 1.0), True),
    Layer("via2",         *_span(_MET2, _MET3), _CONT_COL, True),
    Layer("metal3",       *_MET3, (0.40, 0.80, 0.80, 1.0), True),
    Layer("mimcap",       *_MIMCAP, (0.55, 0.85, 0.40, 1.0), True),
    Layer("mimcapcontact", *_span(_MIMCAP, _MET4), _CONT_COL, True),
    Layer("via3",         *_span(_MET3, _MET4), _CONT_COL, True),
    Layer("metal4",       *_MET4, (0.95, 0.75, 0.30, 1.0), True),
    Layer("mimcap2",      *_MIMCAP2, (0.45, 0.75, 0.35, 1.0), True),
    Layer("mimcap2contact", *_span(_MIMCAP2, _MET5), _CONT_COL, True),
    Layer("via4",         *_span(_MET4, _MET5), _CONT_COL, True),
    Layer("metal5",       *_MET5, (0.75, 0.90, 0.95, 1.0), True),
]

# Magic layers that carry no physical geometry
NON_PHYSICAL = {"checkpaint", "error_s", "error_p", "error_ps", "labels",
                "properties", "end"}


def layer_map(stack=SKY130_LAYERS):
    """Return {magic layer name: Layer}."""
    return {l.name: l for l in stack}
