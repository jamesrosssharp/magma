v {xschem version=3.4.4 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
B 2 610 -580 1410 -180 {flags=graph


ypos1=-0.4
ypos2=1.6
divy=5
subdivy=1
unity=1


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



digital=0
y2=1.9139


color="4 14 12 7"
node="inp
x1.net_pwm
x1.net_in
output"
hilight_wave=6
y1=-0.0861141
x1=2.15e-06
x2=5.15e-06}
B 2 1180 -120 1980 280 {flags=graph
y1=0
y2=2
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=2.15e-06
x2=5.15e-06
divx=5
subdivx=1
xlabmag=1.0
ylabmag=1.0
node=output
color=4
dataset=-1
unitx=1
logx=0
logy=0
}
N -100 -100 -100 -70 {lab=VDD}
N -100 -10 -100 60 {lab=GND}
N -150 110 -150 140 {
lab=INP}
N -570 110 -570 140 {
lab=CLK}
N -100 -100 -100 -70 {lab=VDD}
N -100 -10 -100 60 {lab=GND}
N -240 -90 -240 -60 {lab=VSS}
N -240 0 -240 70 {lab=GND}
N -240 -90 -240 -60 {lab=VSS}
N -240 0 -240 70 {lab=GND}
N 20 70 40 70 {
lab=VDD}
N 20 90 40 90 {
lab=GND}
N 20 110 40 110 {
lab=PWM}
N 20 130 40 130 {
lab=CLK}
N 30 20 30 50 {
lab=INP}
N 30 50 40 50 {
lab=INP}
N 340 80 470 80 {
lab=OUTPUT}
N 340 50 340 80 {
lab=OUTPUT}
N 650 60 650 80 {
lab=#net1}
N 650 80 680 80 {
lab=#net1}
N 860 60 930 60 {
lab=PWM}
C {1bit_am.sym} 190 90 0 0 {name=x1}
C {devices/vsource.sym} -150 170 0 0 {name=VPLUS value="sin(0.9 20m 1Meg 0 0)"
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
tran 0.1n 5u
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
C {vsource.sym} -100 -40 0 0 {name=V3 value=1.8 savecurrent=false}
C {lab_wire.sym} -100 -100 0 0 {name=p8 sig_type=std_logic lab=VDD}
C {launcher.sym} 210 -660 0 0 {name=h5
descr="load waves" 
tclcommand="xschem raw_read $netlist_dir/comp_test_tran.raw tran"
}
C {lab_wire.sym} -100 60 0 0 {name=p9 sig_type=std_logic lab=GND}
C {vsource.sym} -240 -30 0 0 {name=V1 value=0 savecurrent=false}
C {lab_wire.sym} -240 -90 0 0 {name=p4 sig_type=std_logic lab=VSS}
C {lab_wire.sym} -240 70 0 0 {name=p5 sig_type=std_logic lab=GND}
C {lab_wire.sym} 20 70 0 0 {name=p1 sig_type=std_logic lab=VDD}
C {devices/lab_pin.sym} 20 110 0 0 {name=p3 lab=PWM}
C {devices/lab_pin.sym} 20 130 0 0 {name=p6 lab=CLK}
C {devices/lab_pin.sym} 30 20 0 0 {name=p12 lab=INP}
C {lab_wire.sym} 20 90 0 0 {name=p2 sig_type=std_logic lab=GND}
C {devices/lab_pin.sym} 340 50 2 0 {name=p13 lab=OUTPUT}
C {code_shown.sym} -450 -590 0 0 {name=s2 only_toplevel=false format="tcleval( @value )" value="
.ic v(x1.NET_PWM) = 1.0
"}
C {sky130_stdcells/dfxtp_1.sym} 560 70 0 0 {name=x2 VGND=VSS VNB=VSS VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/dfxtp_1.sym} 770 70 0 0 {name=x3 VGND=VSS VNB=VSS VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {devices/lab_pin.sym} 930 60 2 0 {name=p7 lab=PWM}
C {devices/lab_pin.sym} 470 60 0 0 {name=p11 lab=CLK}
C {devices/lab_pin.sym} 680 60 0 0 {name=p14 lab=CLK}
