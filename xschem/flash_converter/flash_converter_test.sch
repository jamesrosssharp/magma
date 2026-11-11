v {xschem version=3.4.4 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
B 2 610 -580 1410 -180 {flags=graph
y1=0.399493

ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=-3.40137e-08
x2=2.1099e-06
divx=5
subdivx=1
xlabmag=1.0
ylabmag=1.0


dataset=-1
unitx=1
logx=0
logy=0

autoload=1
sim_type=tran



digital=1
y2=1.96613


color="4 7 7 7 7 7 7 7 7 7"
node="o7
o6
o5
o4
o3
o2
clk
o1
o0
inp"}
N -100 -100 -100 -70 {lab=VDD}
N -100 -10 -100 60 {lab=GND}
N -150 110 -150 140 {
lab=INP}
N -570 110 -570 140 {
lab=CLK}
N 160 80 250 80 {lab=CLK}
N 160 100 250 100 {lab=INP}
N 550 220 580 220 {
lab=#net1}
N 160 60 250 60 {
lab=#net2}
N 80 60 100 60 {
lab=VDD}
N -100 -100 -100 -70 {lab=VDD}
N -100 -10 -100 60 {lab=GND}
N 640 220 700 220 {
lab=GND}
N 550 60 720 60 {
lab=O0}
N 550 80 720 80 {
lab=O1}
N 550 100 720 100 {
lab=O2}
N 550 120 720 120 {
lab=O3}
N 550 140 720 140 {
lab=O4}
N 550 160 720 160 {
lab=O5}
N 550 180 720 180 {
lab=O6}
N 550 200 720 200 {
lab=O7}
N 210 120 250 120 {
lab=VDD}
N 210 140 250 140 {
lab=GND}
N 160 120 210 120 {
lab=VDD}
N 160 140 210 140 {
lab=GND}
N -240 -90 -240 -60 {lab=VSS}
N -240 0 -240 70 {lab=GND}
N -240 -90 -240 -60 {lab=VSS}
N -240 0 -240 70 {lab=GND}
C {devices/vsource.sym} -150 170 0 0 {name=VPLUS value="sin(1.1 0.7 1Meg 0 0)"
spice_ignore=false}
C {devices/lab_pin.sym} -150 110 0 0 {name=p35 lab=INP}
C {code_shown.sym} -590 -390 0 0 {name=s1 only_toplevel=false format="tcleval( @value )" value="
.lib $::SKYWATER_MODELS/sky130.lib.spice tt

.inc /home/jrsharp/.ciel/sky130A/libs.ref/sky130_fd_sc_hd/spice/sky130_fd_sc_hd.spice

.param VDL = 1.2
.param DELTA = 0.1

.option savecurrents
.control
save all
tran 0.1n 2000n
remzerovec
write comp_test_tran.raw
op
remzerovec
write comp_test_op.raw
.endc


"
}
C {lab_wire.sym} -150 200 0 0 {name=p10 sig_type=std_logic lab=GND}
C {devices/vsource.sym} -570 170 0 0 {name=VCLK1 value="PULSE(0 1.8 0 1NS 1NS 10NS 20NS 0)"
spice_ignore=false}
C {devices/lab_pin.sym} -570 110 0 0 {name=p20 lab=CLK}
C {lab_wire.sym} -570 200 0 0 {name=p21 sig_type=std_logic lab=GND}
C {launcher.sym} 210 -570 0 0 {name=h1
descr="load waves from batch sim" 
tclcommand="xschem raw_read /home/jrsharp/home_mnt/asic/high_speed_comparator/sim/design001/high_speed_comp.raw tran"
}
C {lab_wire.sym} 210 80 0 0 {name=p1 sig_type=std_logic lab=CLK}
C {lab_wire.sym} 210 100 0 0 {name=p2 sig_type=std_logic lab=INP}
C {res.sym} 130 60 1 0 {name=R1
value=500
footprint=1206
device=resistor
m=1}
C {res.sym} 610 220 1 0 {name=R2
value=1.5k
footprint=1206
device=resistor
m=1}
C {lab_wire.sym} 80 60 0 0 {name=p3 sig_type=std_logic lab=VDD}
C {vsource.sym} -100 -40 0 0 {name=V3 value=1.8 savecurrent=false}
C {lab_wire.sym} -100 -100 0 0 {name=p8 sig_type=std_logic lab=VDD}
C {lab_wire.sym} 700 220 0 0 {name=p11 sig_type=std_logic lab=GND}
C {launcher.sym} 210 -660 0 0 {name=h5
descr="load waves" 
tclcommand="xschem raw_read $netlist_dir/comp_test_tran.raw tran"
}
C {lab_wire.sym} 660 60 0 0 {name=p6 sig_type=std_logic lab=O0}
C {lab_wire.sym} 660 80 0 0 {name=p7 sig_type=std_logic lab=O1}
C {lab_wire.sym} 660 100 0 0 {name=p12 sig_type=std_logic lab=O2}
C {lab_wire.sym} 650 120 0 0 {name=p13 sig_type=std_logic lab=O3}
C {lab_wire.sym} 650 140 0 0 {name=p14 sig_type=std_logic lab=O4}
C {lab_wire.sym} 650 160 0 0 {name=p15 sig_type=std_logic lab=O5}
C {lab_wire.sym} 650 180 0 0 {name=p16 sig_type=std_logic lab=O6}
C {lab_wire.sym} 650 200 0 0 {name=p17 sig_type=std_logic lab=O7}
C {flash_converter.sym} 400 140 0 0 {name=x1}
C {lab_wire.sym} 210 120 0 0 {name=p18 sig_type=std_logic lab=VDD}
C {lab_wire.sym} 210 140 0 0 {name=p19 sig_type=std_logic lab=GND}
C {lab_wire.sym} -100 60 0 0 {name=p9 sig_type=std_logic lab=GND}
C {vsource.sym} -240 -30 0 0 {name=V1 value=0 savecurrent=false}
C {lab_wire.sym} -240 -90 0 0 {name=p4 sig_type=std_logic lab=VSS}
C {lab_wire.sym} -240 70 0 0 {name=p5 sig_type=std_logic lab=GND}
