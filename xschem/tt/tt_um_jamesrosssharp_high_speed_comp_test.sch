v {xschem version=3.4.4 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
B 2 -110 -800 690 -400 {flags=graph

y2=1.93443
ypos1=0.186565
ypos2=2.18658
divy=5
subdivy=1
unity=1

x2=5e-6
divx=5
subdivx=1
xlabmag=1.0
ylabmag=1.0
node="inn
inp
vdpwr
out0
out1
out2
out3
out4
out5
out6
out7
out8
out9"
color="12 4 7 8 12 12 12 12 12 12 12 12 12"
dataset=-1
unitx=1
logx=0
logy=0
digital=1
x1=0
y1=0
hilight_wave=8}
B 2 -2030 -870 -1230 -470 {flags=graph
y1=0
y2=2
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0
x2=1e-6
divx=5
subdivx=1
xlabmag=1.0
ylabmag=1.0
node="inn
clk
pwm"
color="7 12 8"
dataset=-1
unitx=1
logx=0
logy=0
}
B 2 480 -230 1280 170 {flags=graph
y1=0
y2=2
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=0
x2=5e-6
divx=5
subdivx=1
xlabmag=1.0
ylabmag=1.0
node="inn
inp"
color="8 7"
dataset=-1
unitx=1
logx=0
logy=0
}
N -540 -310 -540 -280 {lab=VDPWR}
N -540 -220 -540 -150 {lab=GND}
N -590 -100 -590 -70 {
lab=INP}
N -1010 -100 -1010 -70 {
lab=CLK}
N -540 -310 -540 -280 {lab=VDPWR}
N -540 -220 -540 -150 {lab=GND}
N -680 -300 -680 -270 {lab=VGND}
N -680 -210 -680 -140 {lab=GND}
N -680 -300 -680 -270 {lab=VGND}
N -680 -210 -680 -140 {lab=GND}
N -330 90 -160 90 {
lab=VGND}
N -340 -310 -160 -310 {
lab=CLK}
N -330 70 -160 70 {
lab=VDPWR}
N 140 10 270 10 {
lab=OUT0}
N 140 30 270 30 {
lab=OUT1}
N 140 50 270 50 {
lab=OUT2}
N 140 70 270 70 {
lab=OUT3}
N 140 90 270 90 {
lab=OUT4}
N 140 110 270 110 {
lab=OUT5}
N 140 130 270 130 {
lab=OUT6}
N 140 150 270 150 {
lab=OUT7}
N 140 170 270 170 {
lab=OUT8}
N 140 190 270 190 {
lab=OUT9}
N 140 210 140 360 {
lab=#net1}
N 140 -150 190 -150 {
lab=#net2}
N 140 -130 190 -130 {
lab=#net2}
N 140 -110 190 -110 {
lab=#net2}
N 140 -90 190 -90 {
lab=#net2}
N 140 -70 190 -70 {
lab=#net2}
N 140 -50 190 -50 {
lab=#net2}
N 140 -30 190 -30 {
lab=#net2}
N 140 -10 190 -10 {
lab=#net2}
N 190 -170 190 -10 {
lab=#net2}
N -300 50 -160 50 {
lab=VGND}
N -160 -290 -160 -270 {
lab=VGND}
N -160 -230 -160 30 {
lab=VGND}
N -340 -250 -160 -250 {
lab=PWM}
N -160 30 -160 50 {
lab=VGND}
N -780 -240 -780 -210 {lab=VSS}
N -780 -150 -780 -80 {lab=GND}
N -780 -240 -780 -210 {lab=VSS}
N -780 -150 -780 -80 {lab=GND}
N -1160 -100 -1160 -70 {
lab=PWM}
C {tt_um_jamesrosssharp_high_speed_comp.sym} -10 0 0 0 {name=x1}
C {devices/vsource.sym} -590 -40 0 0 {name=VPLUS value="sin(1.1 0.6 1Meg 0 0)"
spice_ignore=false}
C {devices/lab_pin.sym} -590 -100 0 0 {name=p35 lab=INP}
C {code_shown.sym} -1030 -600 0 0 {name=s1 only_toplevel=false format="tcleval( @value )" value="
.lib $::SKYWATER_MODELS/sky130.lib.spice tt

.inc /home/jrsharp/.ciel/sky130A/libs.ref/sky130_fd_sc_hd/spice/sky130_fd_sc_hd.spice

.param VDL = 1.2
.param DELTA = 0.1

.option savecurrents
.control
save all
tran 2n 5u
remzerovec
write comp_test_tran.raw
op
remzerovec
write comp_test_op.raw
.endc


"
}
C {lab_wire.sym} -590 -10 0 0 {name=p10 sig_type=std_logic lab=GND}
C {devices/vsource.sym} -1010 -40 0 0 {name=VCLK1 value="PULSE(0 1.8 0 1NS 1NS 10NS 20NS 0)"
spice_ignore=false}
C {devices/lab_pin.sym} -1010 -100 0 0 {name=p20 lab=CLK}
C {lab_wire.sym} -1010 -10 0 0 {name=p21 sig_type=std_logic lab=GND}
C {vsource.sym} -540 -250 0 0 {name=V3 value=1.8 savecurrent=false}
C {lab_wire.sym} -540 -310 0 0 {name=p8 sig_type=std_logic lab=VDPWR}
C {lab_wire.sym} -540 -150 0 0 {name=p9 sig_type=std_logic lab=GND}
C {vsource.sym} -680 -240 0 0 {name=V1 value=0 savecurrent=false}
C {lab_wire.sym} -680 -300 0 0 {name=p4 sig_type=std_logic lab=VGND}
C {lab_wire.sym} -680 -140 0 0 {name=p5 sig_type=std_logic lab=GND}
C {devices/lab_pin.sym} 140 -310 2 0 {name=p3 lab=INP}
C {devices/lab_pin.sym} 140 -290 2 0 {name=p6 lab=INN}
C {lab_wire.sym} -330 90 0 0 {name=p7 sig_type=std_logic lab=VGND}
C {lab_wire.sym} -330 70 0 0 {name=p11 sig_type=std_logic lab=VDPWR}
C {lab_wire.sym} 270 10 0 0 {name=p12 sig_type=std_logic lab=OUT0}
C {lab_wire.sym} 270 30 0 0 {name=p13 sig_type=std_logic lab=OUT1}
C {lab_wire.sym} 270 50 0 0 {name=p14 sig_type=std_logic lab=OUT2}
C {lab_wire.sym} 270 70 0 0 {name=p15 sig_type=std_logic lab=OUT3}
C {lab_wire.sym} 270 90 0 0 {name=p16 sig_type=std_logic lab=OUT4}
C {lab_wire.sym} 270 110 0 0 {name=p17 sig_type=std_logic lab=OUT5}
C {lab_wire.sym} 270 130 0 0 {name=p18 sig_type=std_logic lab=OUT6}
C {lab_wire.sym} 270 150 0 0 {name=p19 sig_type=std_logic lab=OUT7}
C {lab_wire.sym} 270 170 0 0 {name=p22 sig_type=std_logic lab=OUT8}
C {lab_wire.sym} 270 190 0 0 {name=p23 sig_type=std_logic lab=OUT9}
C {devices/lab_pin.sym} -340 -310 0 0 {name=p24 lab=CLK}
C {launcher.sym} -320 -790 0 0 {name=h5
descr="load waves" 
tclcommand="xschem raw_read $netlist_dir/comp_test_tran.raw tran"
}
C {lab_wire.sym} 140 420 0 0 {name=p25 sig_type=std_logic lab=GND}
C {res.sym} 140 390 0 0 {name=R1
value=1Meg
footprint=1206
device=resistor
m=1}
C {res.sym} 190 -200 0 0 {name=R2
value=1Meg
footprint=1206
device=resistor
m=1}
C {lab_wire.sym} 190 -230 0 0 {name=p26 sig_type=std_logic lab=GND}
C {lab_wire.sym} -300 50 0 0 {name=p27 sig_type=std_logic lab=VGND}
C {lab_wire.sym} -160 -270 0 0 {name=p1 sig_type=std_logic lab=VGND}
C {devices/lab_pin.sym} -340 -250 0 0 {name=p2 lab=PWM}
C {vsource.sym} -780 -180 0 0 {name=V2 value=0 savecurrent=false}
C {lab_wire.sym} -780 -240 0 0 {name=p28 sig_type=std_logic lab=VSS}
C {lab_wire.sym} -780 -80 0 0 {name=p29 sig_type=std_logic lab=GND}
C {devices/vsource.sym} -1160 -40 0 0 {name=VCLK2 value="PULSE(0 1.8 0 1NS 1NS 22NS 45NS 0)"
spice_ignore=false}
C {devices/lab_pin.sym} -1160 -100 0 0 {name=p30 lab=PWM}
C {lab_wire.sym} -1160 -10 0 0 {name=p31 sig_type=std_logic lab=GND}
