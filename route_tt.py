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

    arr = [(a[0] - b[0]) * 0, 
           0, 
           0,
           0,
           ((a[0] - b[0]) * 4 / 7) + 600,
           ((a[0] - b[0]) * 5 / 7),
           ((a[0] - b[0]) * 6 / 7),
           ((a[0] - b[0]))
           ]

    for i in range(0, 8):
        r.routeTo('w', b[0] + arr[i], 34)
        r.push()
        r.viaExpansion('metal1', 34, 34, 34, 34, 80, 80)
        r.pop()

    arr = [(a[0] - b[0]) / 10, 
           ((a[0] - b[0]) * 2 / 10), 
           ((a[0] - b[0]) * 3 / 10),
           ((a[0] - b[0]) * 4 / 10) ,
           ((a[0] - b[0]) * 5 / 10) + 100,
           ((a[0] - b[0]) * 6 / 10) + 100,
           ((a[0] - b[0]) * 7 / 10) + 100,
           ((a[0] - b[0]) * 8 / 10),
           ((a[0] - b[0]) * 9 / 10),
           ((a[0] - b[0])),
           ]

    r.begin(a[0], a[1], 'metal3')
    for i in range(0, 10):
        r.routeTo('w', b[0] + arr[i], 200)
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
r.routeTo('n', b[1] - 2400, 100) 
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

# Route O0 - O7 in metal 3 to respective buffers

cell_ports = [
                ('O0', 'x27'), ('O1', 'x28'), ('O2', 'x29'), ('O3', 'x30'),
                ('O4', 'x31'), ('O5', 'x32'), ('O6', 'x33'), ('O7', 'x34'),
              ]

i = 0

for pp, c in cell_ports:
    a = p['children']['x2']['self'][pp].centroid()
    b = p['children'][c]['self']['A'].centroid()
 
    arr = [8, 7, 6, 5, 4, 3, 2, 1]

    r.begin(a[0], a[1], 'metal1')
    r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
    r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
    r.route('w', arr[i] * 200, 100)
    r.routeTo('n', b[1] - 1000 - arr[i] * 200, 100)
    r.routeTo('w', b[0], 100)
    r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
    r.routeTo('n', b[1], 100)
    r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
    r.viaExpansion('locali', 34, 34, 120, 120, 34, 34)

    i += 1

# Route buffers to pins

cell_ports =   [
                ('uio_out[0]', 'x27'), ('uio_out[1]', 'x28'), ('uio_out[2]', 'x29'), ('uio_out[3]', 'x30'),
                ('uio_out[4]', 'x31'), ('uio_out[5]', 'x32'), ('uio_out[6]', 'x33'), ('uio_out[7]', 'x34'),
              ]

i = 0
for pp, c in cell_ports:
    a = p['self'][pp].centroid()
    b = p['children'][c]['self']['X'].centroid()
 
    arr = [0, 1, 1, 4, 3, 2, 1, 0]

    rw = 60

    r.begin(a[0], a[1], 'metal4')
    r.route('s', 600 + arr[i]*150, rw)
    r.routeTo('e', b[0], rw)
    r.routeTo('s', b[1] + 100, rw)
    r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
    r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
    r.routeTo('s', b[1], rw)
    r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
    r.viaExpansion('locali', 34, 34, 120, 120, 34, 34)
    i += 1

# Route uo_out[2]..[7] to conb lo cells

cell_ports =   [
                ('uo_out[2]', 'x12'), ('uo_out[3]', 'x13'),
                ('uo_out[4]', 'x14'), ('uo_out[5]', 'x15'), ('uo_out[6]', 'x16'), ('uo_out[7]', 'x17'),
              ]

i = 0
for pp, c in cell_ports:
    a = p['self'][pp].centroid()
    b = p['children'][c]['self']['LO'].centroid()
 
    arr = [2, 1, 1, 1, 2, 3]

    rw = 60

    r.begin(a[0], a[1], 'metal4')
    r.route('s', 100 + arr[i]*120, rw)
    r.routeTo('e', b[0], rw)
    r.routeTo('s', b[1] + 100, rw)
    r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
    r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
    r.routeTo('s', b[1], rw)
    r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
    r.viaExpansion('locali', 34, 34, 120, 120, 34, 34)
    i += 1

# Route uio_oe[0] .. [7] to conb hi cells

cell_ports =   [
                ('uio_oe[0]', 'x3', True), ('uio_oe[1]', 'x4', True), ('uio_oe[2]', 'x5', True), ('uio_oe[3]', 'x6', False),
                ('uio_oe[4]', 'x7', False), ('uio_oe[5]', 'x8', False), ('uio_oe[6]', 'x9', False), ('uio_oe[7]', 'x10', False),
              ]

i = 0
for pp, c, dl in cell_ports:
    a = p['self'][pp].centroid()
    b = p['children'][c]['self']['HI'].centroid()
 
    arr = [3, 2, 1, 2, 1, 1, 2, 3]

    rw = 60

    r.begin(a[0], a[1], 'metal4')
    r.route('s', 100 + arr[i]*120, rw)
    if dl:
        r.route('w', 400, rw)
        r.route('s', 400, rw)
    r.routeTo('e', b[0], rw)
    r.routeTo('s', b[1] + 50, rw)
    r.viaExpansion('metal3', 100, 100, 120, 120, 120, 120)
    r.viaExpansion('metal2', 100, 100, 120, 120, 120, 120)
    r.routeTo('s', b[1], rw)
    r.viaExpansion('metal1', 100, 100, 120, 120, 120, 120)
    r.viaExpansion('locali', 34, 34, 120, 120, 34, 34)
    i += 1



top.writeMagFile(db, "tt/tt_um_jamesrosssharp_high_speed_comp.mag")
