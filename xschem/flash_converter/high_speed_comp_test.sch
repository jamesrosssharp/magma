v {xschem version=3.4.4 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
B 2 60 -590 860 -190 {flags=graph
y1=-0.566594
y2=2.87904
ypos1=0
ypos2=2
divy=5
subdivy=1
unity=1
x1=-2.8899e-08
x2=6.89534e-07
divx=5
subdivx=1
xlabmag=1.0
ylabmag=1.0
node="inp
inn
clk
comp_out"
color="4 7 12 10"
dataset=-1
unitx=1
logx=0
logy=0

autoload=1
sim_type=tran}
N -520 -180 -520 -150 {lab=VDD}
N -520 -90 -520 -20 {lab=GND}
N -570 30 -570 60 {
lab=INP}
N -390 30 -390 60 {
lab=INN}
N -990 30 -990 60 {
lab=CLK}
N -400 260 -310 260 {lab=CLK}
N -400 280 -310 280 {lab=INP}
N -400 300 -310 300 {lab=INN}
N -400 320 -310 320 {lab=VDD}
N -400 340 -310 340 {lab=GND}
N -10 260 90 260 {lab=COMP_OUT}
C {vsource.sym} -520 -120 0 0 {name=V1 value=1.8 savecurrent=false}
C {lab_wire.sym} -520 -180 0 0 {name=p6 sig_type=std_logic lab=VDD}
C {lab_wire.sym} -520 -20 0 0 {name=p7 sig_type=std_logic lab=GND}
C {devices/vsource.sym} -570 90 0 0 {name=VPLUS value='VDL'
spice_ignore=false}
C {devices/lab_pin.sym} -570 30 0 0 {name=p35 lab=INP}
C {devices/vsource.sym} -390 90 0 0 {name=VMINUS value="pwl
+0 'VDL-DELTA'
+30.5n 'VDL-DELTA'
+170.5n 'VDL+DELTA'
+209.9n 'VDL+DELTA'
"
spice_ignore=false}
C {devices/lab_pin.sym} -390 30 0 0 {name=p37 lab=INN}
C {code_shown.sym} -1010 -470 0 0 {name=s1 only_toplevel=false format="tcleval( @value )" value=".lib $::SKYWATER_MODELS/sky130.lib.spice tt

.inc /home/jrsharp/old_home_mnt/asic/sky130_pdk/share/pdk/sky130A/libs.ref/sky130_fd_sc_hd/spice/sky130_fd_sc_hd.spice

.param VDL = 1.2
.param DELTA = 0.1

.option savecurrents
.control
save all
tran 0.1n 500n
remzerovec
write comp_test_tran.raw
op
remzerovec
write comp_test_op.raw
.endc


"
}
C {lab_wire.sym} -570 120 0 0 {name=p10 sig_type=std_logic lab=GND}
C {lab_wire.sym} -390 120 0 0 {name=p11 sig_type=std_logic lab=GND}
C {launcher.sym} -150 -630 0 0 {name=h5
descr="load waves" 
tclcommand="xschem raw_read $netlist_dir/comp_test_tran.raw tran"
}
C {devices/vsource.sym} -990 90 0 0 {name=VCLK1 value="pwl
+0 0
+20n 0
+20.1n 1.8
+29.9n   1.8
+30n 0
+40n 0
+40.1n 1.8
+49.9n   1.8
+50n 0
+60n 0
+60.1n 1.8
+69.9n   1.8
+70n 0
+80n 0
+80.1n 1.8
+89.9n   1.8
+90n 0
+100n 0
+100.1n 1.8
+109.9n   1.8
+110n 0
+120n 0
+120.1n 1.8
+129.9n   1.8
+130n 0
+140n 0
+140.1n 1.8
+149.9n   1.8
+150n 0
+160n 0
+160.1n 1.8
+169.9n   1.8
+170n 0
+180n 0
+180.1n 1.8
+189.9n   1.8
+190n 0
+200n 0
+200.1n 1.8
+209.9n   1.8
+210n 0
+220n 0
+220.1n 1.8
+229.9n   1.8
+230n 0
+240n 0
"
spice_ignore=false}
C {devices/lab_pin.sym} -990 30 0 0 {name=p20 lab=CLK}
C {lab_wire.sym} -990 120 0 0 {name=p21 sig_type=std_logic lab=GND}
C {high_speed_comp_top.sym} -160 300 0 0 {name=x1}
C {lab_wire.sym} -350 260 0 0 {name=p1 sig_type=std_logic lab=CLK}
C {lab_wire.sym} -350 280 0 0 {name=p2 sig_type=std_logic lab=INP}
C {lab_wire.sym} -350 300 0 0 {name=p3 sig_type=std_logic lab=INN}
C {lab_wire.sym} -350 320 0 0 {name=p4 sig_type=std_logic lab=VDD}
C {lab_wire.sym} -350 340 0 0 {name=p5 sig_type=std_logic lab=GND}
C {lab_wire.sym} 70 260 0 0 {name=p8 sig_type=std_logic lab=COMP_OUT}
C {launcher.sym} -150 -580 0 0 {name=h1
descr="load waves from batch sim" 
tclcommand="xschem raw_read /home/jrsharp/home_mnt/asic/high_speed_comparator/sim/design001/high_speed_comp.raw tran"
}
