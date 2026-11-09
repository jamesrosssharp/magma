v {xschem version=3.4.4 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N -60 -240 10 -240 {lab=#net1}
N -60 -220 10 -220 {lab=#net2}
N -60 -260 10 -260 {lab=VDD}
N -60 -200 10 -200 {lab=VSS}
N -440 -190 -360 -190 {lab=VSS}
N -440 -270 -360 -270 {lab=VDD}
N -440 -250 -360 -250 {lab=CLK_PRIME}
N -440 -230 -360 -230 {lab=VINP}
N -440 -210 -360 -210 {lab=VINN}
N 310 -230 390 -230 {lab=VOUT}
N 390 -230 420 -230 {lab=VOUT}
N 600 -250 690 -250 {lab=COMP_OUT}
N 360 -250 420 -250 {lab=CLK}
N -410 -500 -300 -500 {lab=CLK_PRIME}
N -540 -500 -490 -500 {lab=CLK}
N -450 -270 -440 -270 {lab=VDD}
N -520 -270 -450 -270 {lab=VDD}
N -520 -190 -440 -190 {lab=VSS}
N -620 -430 -540 -430 {lab=VINP}
N -620 -380 -540 -380 {lab=VINN}
N -240 -500 -140 -500 {
lab=CLK_PRIME}
N -300 -500 -270 -500 {
lab=CLK_PRIME}
N -270 -500 -240 -500 {
lab=CLK_PRIME}
N -580 -270 -520 -270 {
lab=VDD}
N -580 -190 -520 -190 {
lab=VSS}
C {strong_arm_latch.sym} -210 -230 0 0 {name=x1}
C {post_amplifier.sym} 160 -230 0 0 {name=x2}
C {lab_wire.sym} -10 -260 0 0 {name=p3 sig_type=std_logic lab=VDD}
C {lab_wire.sym} -10 -200 0 0 {name=p4 sig_type=std_logic lab=VSS}
C {lab_wire.sym} -400 -250 0 0 {name=p5 sig_type=std_logic lab=CLK_PRIME}
C {lab_wire.sym} -400 -230 0 0 {name=p6 sig_type=std_logic lab=VINP}
C {lab_wire.sym} -400 -210 0 0 {name=p7 sig_type=std_logic lab=VINN}
C {lab_wire.sym} 340 -230 0 0 {name=p24 sig_type=std_logic lab=VOUT}
C {lab_wire.sym} 400 -250 0 0 {name=p17 sig_type=std_logic lab=CLK}
C {sky130_stdcells/dfxtp_2.sym} 510 -240 0 0 {name=x3 VGND=VSS VNB=VSS VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/clkinv_4.sym} -450 -500 0 0 {name=x4 VGND=VSS VNB=VSS VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/decap_3.sym} 450 -370 0 0 {name=x5 VGND=VSS VNB=VSS VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/decap_3.sym} 450 -410 0 0 {name=x7 VGND=VSS VNB=VSS VPB=VDD VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {ipin.sym} -620 -430 0 0 {name=p11 lab=VINP}
C {ipin.sym} -620 -380 0 0 {name=p12 lab=VINN
}
C {ipin.sym} -540 -500 0 0 {name=p18 lab=CLK}
C {opin.sym} 690 -250 0 0 {name=p19 lab=COMP_OUT}
C {sky130_stdcells/tapvpwrvgnd_1.sym} 450 -450 0 0 {name=x9 VGND=VSS VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/tapvpwrvgnd_1.sym} 440 -500 0 0 {name=x6 VGND=VSS VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/tapvpwrvgnd_1.sym} 440 -550 0 0 {name=x8 VGND=VSS VPWR=VDD prefix=sky130_fd_sc_hd__ }
C {lab_wire.sym} -140 -500 0 0 {name=p10 sig_type=std_logic lab=CLK_PRIME}
C {ipin.sym} -580 -270 0 0 {name=p13 lab=VDD}
C {ipin.sym} -580 -190 0 0 {name=p14 lab=VSS}
