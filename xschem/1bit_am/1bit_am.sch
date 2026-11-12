v {xschem version=3.4.4 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N -410 -120 -380 -120 {
lab=NET_PWM}
N -380 -60 -380 -30 {
lab=VSS}
N -380 -120 -220 -120 {
lab=NET_PWM}
N -220 -120 -220 10 {
lab=NET_PWM}
N -220 10 -140 10 {
lab=NET_PWM}
N -280 -170 -280 -150 {
lab=VSS}
N -280 -290 -180 -290 {
lab=NET_IN}
N -180 -290 -180 -10 {
lab=NET_IN}
N -180 -10 -140 -10 {
lab=NET_IN}
N -280 -440 -280 -410 {
lab=VDD}
N -140 -10 -60 -10 {
lab=NET_IN}
N -140 10 -60 10 {
lab=NET_PWM}
N -100 -30 -60 -30 {
lab=CLK}
N -390 -290 -280 -290 {
lab=NET_IN}
N 240 -30 310 -30 {
lab=VOUT}
N -750 -120 -740 -120 {
lab=#net1}
N -480 -120 -470 -120 {
lab=#net2}
C {/home/jrsharp/code/magma/xschem/flash_converter/high_speed_comp_top.sym} 90 10 0 0 {name=x1}
C {sky130_fd_pr/res_xhigh_po_0p35.sym} -440 -120 1 0 {name=R2
L=30
model=res_xhigh_po_0p35
spiceprefix=X
mult=1}
C {lab_wire.sym} -380 -30 0 0 {name=p1 sig_type=std_logic lab=VSS}
C {sky130_fd_pr/res_xhigh_po_0p35.sym} -280 -380 2 0 {name=R3
L=20
model=res_xhigh_po_0p35
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_xhigh_po_0p35.sym} -280 -320 2 0 {name=R4
L=20
model=res_xhigh_po_0p35
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_xhigh_po_0p35.sym} -280 -260 2 0 {name=R5
L=20
model=res_xhigh_po_0p35
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_xhigh_po_0p35.sym} -280 -200 2 0 {name=R6
L=20
model=res_xhigh_po_0p35
spiceprefix=X
mult=1}
C {lab_wire.sym} -280 -150 0 0 {name=p3 sig_type=std_logic lab=VSS}
C {lab_wire.sym} -280 -430 0 0 {name=p4 sig_type=std_logic lab=VDD}
C {ipin.sym} -80 -220 0 0 {name=p5 lab=VDD}
C {ipin.sym} -80 -180 0 0 {name=p6 lab=VSS}
C {lab_wire.sym} -60 30 0 0 {name=p7 sig_type=std_logic lab=VDD}
C {lab_wire.sym} -60 50 0 0 {name=p8 sig_type=std_logic lab=VSS}
C {ipin.sym} -100 -30 0 0 {name=p9 lab=CLK}
C {ipin.sym} -450 -290 0 0 {name=p10 lab=VIN}
C {opin.sym} 310 -30 0 0 {name=p11 lab=VOUT}
C {lab_wire.sym} -180 -290 0 0 {name=p12 sig_type=std_logic lab=NET_IN}
C {lab_wire.sym} -240 -120 0 0 {name=p13 sig_type=std_logic lab=NET_PWM}
C {sky130_fd_pr/cap_mim_m3_1.sym} -420 -290 3 0 {name=C1 model=cap_mim_m3_1 W=10 L=10 MF=20 spiceprefix=X}
C {sky130_fd_pr/cap_mim_m3_1.sym} -380 -90 0 0 {name=C2 model=cap_mim_m3_1 W=10 L=10 MF=20 spiceprefix=X}
C {sky130_stdcells/decap_3.sym} -660 -310 0 0 {name=x4 VGND=VSS VNB=VSS VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/decap_3.sym} -660 -270 0 0 {name=x5 VGND=VSS VNB=VSS VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/tapvpwrvgnd_1.sym} -660 -230 0 0 {name=x6 VGND=VSS VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/tapvpwrvgnd_1.sym} -660 -190 0 0 {name=x7 VGND=VSS VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_fd_pr/res_xhigh_po_0p35.sym} -630 -120 1 0 {name=R1
L=30
model=res_xhigh_po_0p35
spiceprefix=X
mult=1}
C {sky130_stdcells/inv_1.sym} -790 -120 0 0 {name=x3 VGND=VSS VNB=VSS VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {ipin.sym} -830 -120 0 0 {name=p2 lab=PWM_IN}
C {sky130_fd_pr/res_xhigh_po_0p35.sym} -570 -120 1 0 {name=R7
L=30
model=res_xhigh_po_0p35
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_xhigh_po_0p35.sym} -510 -120 1 0 {name=R8
L=30
model=res_xhigh_po_0p35
spiceprefix=X
mult=1}
C {sky130_stdcells/inv_1.sym} -700 -120 0 0 {name=x2 VGND=VSS VNB=VSS VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
