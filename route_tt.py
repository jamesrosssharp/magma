import sys

sys.path.append("build/lib.linux-x86_64-cpython-314/")

import MagParser
import MagDatabase
import Router
import numpy as np

p = MagParser.MagParser()
db = MagDatabase.MagDatabase()

p.parse("tt/tt_um_jamesrosssharp_high_speed_comp_master.mag", db, "~/.ciel/sky130A")

#db.dump()

db.findAllTransistors()

t = db.getCellTransistors('tt_um_jamesrosssharp_high_speed_comp_master')

#print(t)

db.findAllResistors()

res = db.getCellResistors('tt_um_jamesrosssharp_high_speed_comp_master')

#print(res)

db.findAllCapacitors()

cap = db.getCellCapacitors('tt_um_jamesrosssharp_high_speed_comp_master')

#print(cap)

p = db.getCellPins('tt_um_jamesrosssharp_high_speed_comp_master')

#print(p)

top = db.getCell('tt_um_jamesrosssharp_high_speed_comp_master')

r = Router.Router(db, "tt_um_jamesrosssharp_high_speed_comp_master")

# Route VDD and VSS to x1 (1bit am) and x11 (comparator)

for cell in ['x1', 'x11']:

    vv = [('VDPWR', 'VDD'), ('VGND', 'VSS')]

    for vvv, vvvv in vv:

        a = p['children'][cell]['self'][vvvv].centroid()
        b = p['self'][vvv].centroid()

        r.begin(a[0], a[1], 'metal1')
        r.viaExpansion('metal2', 400,400,500,500,500,500)
        r.viaExpansion('metal3', 400,400,500,500,600,600)
        r.routeTo('w', b[0], 600)
        r.viaExpansion('metal4', 540, 540, 600, 600, 600, 600)

# Power stripes

for v, vv in [('VPWR', 'VDPWR'), ('VGND', 'VGND')]:

    a = p['children']['x18']['self'][v].centroid()
    b = p['children']['x10']['self'][v].centroid()
    c = p['self'][vv].centroid()

    # Metal 1 stripe
    r.begin(a[0], a[1], 'metal1')
    r.routeTo('e', b[0], 80)

    # Locali body bias
    r.begin(a[0], a[1], 'locali')
    for i in range(0, 7):
        r.route('w', (a[0] - b[0]) / 7, 34)
        r.push()
        r.viaExpansion('metal1', 34, 34, 34, 34, 80, 80)
        r.pop()


    r.begin(a[0], a[1], 'metal3')
    for i in range(0, 10):
        r.route('w', (a[0] - b[0]) / 10, 200)
        r.push()
        r.viaExpansion('metal2', 120, 120, 200, 200, 140, 140)
        r.viaExpansion('metal1', 60, 60, 140, 140, 80, 80)
        r.pop()
    r.routeTo('w', c[0], 200)
    if v == 'VPWR':
        r.route('s', 400, 200)
    r.viaExpansion('metal4', 200, 200, 240, 240, 400, 400)

r.begin(27900, 12400, 'metal4')
r.route('s', 8400, 500)
r.viaExpansion('metal3', 400, 400, 500, 500, 500, 500)
r.viaExpansion('metal2', 400, 400, 500, 500, 500, 500)
r.viaExpansion('metal1', 400, 400, 500, 500, 500, 500)
 

# Route analog pins

a = p['self']['ua[0]'].centroid()
b = p['children']['x11']['self']['VINP'].centroid()

r.begin(a[0], a[1], 'metal4')
r.routeTo('n', b[1], 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
r.routeTo('w', b[0], 100)

a = p['self']['ua[1]'].centroid()
b = p['children']['x11']['self']['VINN'].centroid()

r.begin(a[0], a[1], 'metal4')
r.routeTo('n', b[1] - 3500, 100)
r.routeTo('e', b[0] + 1000, 100)
r.routeTo('n', b[1], 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
r.routeTo('w', b[0], 100)

a = p['self']['ua[0]'].centroid()
b = p['children']['x2']['self']['VIN'].centroid()
c = p['children']['x11']['self']['VINP'].centroid()

r.begin(a[0], a[1], 'metal4')
r.routeTo('n', c[1], 100)
r.routeTo('e', b[0], 100)
r.routeTo('n', b[1], 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)

# Route analog pins to 1bit AM fronted

a = p['self']['ua[0]'].centroid()
b = p['children']['x1']['self']['VIN'].centroid()

r.begin(a[0], a[1], 'metal4')
r.route('n', 1500, 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.routeTo('w', b[0] + 1200, 100)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.routeTo('n', b[1], 100)
r.routeTo('w', b[0], 100)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)

a = p['self']['ua[1]'].centroid()
b = p['children']['x1']['self']['VIN_MINUS'].centroid()

r.begin(a[0], a[1], 'metal4')
r.route('n', 1100, 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.routeTo('w', b[0] + 1000, 100)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.routeTo('n', b[1], 100)
r.routeTo('w', b[0], 100)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)

# Route x1.PWM_IN

a = p['children']['x1']['self']['PWM_IN'].centroid()
b = p['self']['ui_in[0]'].centroid()

r.begin(a[0], a[1], 'metal1')
r.route('e', 1000, 100)
r.routeTo('n', b[1] - 2000, 100) 
r.routeTo('e', b[0], 100) 
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal4', 100, 100, 120, 120, 120, 120)
r.routeTo('n', b[1], 100)

# Route x1.CLK

a = p['children']['x1']['self']['CLK'].centroid()
b = p['children']['x18']['self']['X'].centroid()

r.begin(a[0], a[1], 'metal1')
r.route('e', 800, 100)
r.routeTo('n', b[1] - 800, 100) 
r.routeTo('e', b[0] + 50, 100) 
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.routeTo('n', b[1] + 50, 100)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
r.viaExpansion('locali', 34, 34, 120, 120, 34, 34)

# Route x1.VOUT

a = p['children']['x1']['self']['VOUT'].centroid()
b = p['children']['x22']['self']['A'].centroid()

r.begin(a[0], a[1], 'metal1')
r.route('e', 600, 100)
r.routeTo('n', b[1] - 500, 100) 
r.routeTo('e', b[0], 100) 
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.routeTo('n', b[1], 100)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
r.viaExpansion('locali', 34, 34, 120, 120, 34, 34)

# Route x22.X to uo_out[0]

a = p['children']['x22']['self']['X'].centroid()
b = p['self']['uo_out[0]'].centroid()

r.begin(a[0], a[1], 'locali')
r.viaExpansion('metal1', 34, 34, 34, 34, 120, 120)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.route('n', 50, 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal4', 100, 100, 120, 120, 120, 120)
r.routeTo('e', b[0], 100)
r.routeTo('n', b[1], 100)

# Route x11.CLK to x1.CLK
a = p['children']['x11']['self']['CLK'].centroid()
b = p['children']['x1']['self']['CLK'].centroid()
c = p['children']['x2']['self']['CLK'].centroid()

r.begin(a[0], a[1], 'metal1')
r.route('w', 3800, 100)
r.route('n', b[1] - 9000, 100)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal4', 100, 100, 120, 120, 120, 120)
r.routeTo('n', b[1], 100)
r.push()
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
r.pop()
r.routeTo('e', c[0], 100)
r.routeTo('n', c[1], 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)


# Route x11.COMP_OUT to x21.A

a = p['children']['x11']['self']['COMP_OUT'].centroid()
b = p['children']['x21']['self']['A'].centroid()

r.begin(a[0], a[1], 'metal1')
r.route('w', 2350, 100)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.routeTo('n', b[1] - 300, 100)
r.routeTo('w', b[0], 100)
r.routeTo('n', b[1], 100)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
r.viaExpansion('locali', 34, 34, 120, 120, 34, 34)

# Route x21.X to uo_out[1]

a = p['children']['x21']['self']['X'].centroid()
b = p['self']['uo_out[1]'].centroid()

r.begin(a[0], a[1], 'locali')
r.viaExpansion('metal1', 34, 34, 34, 34, 120, 120)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.route('n', 50, 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal4', 100, 100, 120, 120, 120, 120)
r.routeTo('e', b[0], 100)
r.routeTo('n', b[1], 100)

# Route clock input to x18.A

a = p['self']['clk'].centroid()
b = p['children']['x18']['self']['A'].centroid()

r.begin(a[0], a[1], 'metal4')
r.routeTo('s', b[1], 100)
r.routeTo('w', b[0], 100)
r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
r.viaExpansion('locali', 34, 34, 120, 120, 34, 34)

# Route XR11 to VDD and res top

a = res['children']['XR11']['self'][0].contacts[0]
b = p['children']['x2']['self']['RES_TOP'].centroid()

r.begin(a[0], a[1], 'metal1')
r.routeTo('e', b[0], 100)
r.routeTo('n', b[1], 100)

a = res['children']['XR11']['self'][0].contacts[1]
b = p['children']['x11']['self']['VDD'].centroid()

r.begin(a[0], a[1], 'metal1')
r.routeTo('s', b[1], 100)
r.routeTo('w', b[0], 100)

# Route XR1, XR2, XR3 chain

for i in range(0,2):

    rr = f'XR{i+1}'
    rrr = f'XR{i+2}'

    a = res['children'][rr]['self'][0].contacts[0]
    b = res['children'][rrr]['self'][0].contacts[1]

    r.begin(a[0], a[1], 'metal1')
    r.routeTo('n', ((a[1] + b[1]) / 2) + i*0, 100)
    r.routeTo('e', b[0], 100)
    r.routeTo('n', b[1], 100)

# Route XR1 to VSS and XR3 to res out

a = res['children']['XR3']['self'][0].contacts[0]
b = p['children']['x2']['self']['RES_OUT'].centroid()

r.begin(a[0], a[1], 'metal1')
r.routeTo('e', b[0], 100)
r.routeTo('n', b[1], 100)

a = res['children']['XR1']['self'][0].contacts[1]
b = p['children']['x11']['self']['VSS'].centroid()

r.begin(a[0], a[1], 'metal1')
r.route('w', 400, 100)
r.routeTo('s', b[1] + 4800, 100)
r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
r.routeTo('s', b[1], 100)
r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
r.routeTo('w', b[0], 100)



top.writeMagFile(db, "tt/tt_um_jamesrosssharp_high_speed_comp.mag")
