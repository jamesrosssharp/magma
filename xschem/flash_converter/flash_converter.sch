v {xschem version=3.4.4 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
T {Dummy devices} -630 -50 0 0 0.4 0.4 {}
N -140 -260 -140 -140 {
lab=RES_TOP}
N -140 -170 40 -170 {
lab=RES_TOP}
N -210 -190 40 -190 {
lab=VIN}
N -210 -240 -210 1140 {
lab=VIN}
N -210 -20 40 -20 {
lab=VIN}
N -210 160 40 160 {
lab=VIN}
N -140 -80 -140 30 {
lab=#net1}
N -140 90 -140 180 {
lab=#net2}
N -140 0 40 0 {
lab=#net1}
N -140 180 -140 210 {
lab=#net2}
N -140 180 40 180 {
lab=#net2}
N -140 260 -140 400 {
lab=#net3}
N -140 460 -140 580 {
lab=#net4}
N -140 380 40 380 {
lab=#net3}
N -140 570 40 570 {
lab=#net4}
N -140 640 -140 780 {
lab=#net5}
N -140 770 40 770 {
lab=#net5}
N -140 840 -140 960 {
lab=#net6}
N -140 1020 -140 1140 {
lab=#net7}
N -140 940 40 940 {
lab=#net6}
N -140 1120 40 1120 {
lab=#net7}
N -210 360 40 360 {
lab=VIN}
N -210 550 40 550 {
lab=VIN}
N -210 750 40 750 {
lab=VIN}
N -210 920 40 920 {
lab=VIN}
N -210 1100 40 1100 {
lab=VIN}
N -40 1080 40 1080 {
lab=CLK}
N -40 900 40 900 {
lab=CLK}
N -40 730 40 730 {
lab=CLK}
N -40 530 40 530 {
lab=CLK}
N -40 340 40 340 {
lab=CLK}
N -40 140 40 140 {
lab=CLK}
N -40 -40 40 -40 {
lab=CLK}
N -40 -210 40 -210 {
lab=CLK}
N -40 -250 -40 1080 {
lab=CLK}
N -560 80 -460 80 {
lab=VDD}
N -560 110 -460 110 {
lab=VSS}
C {high_speed_comp_top.sym} 190 -170 0 0 {name=x1}
C {high_speed_comp_top.sym} 190 0 0 0 {name=x2}
C {high_speed_comp_top.sym} 190 180 0 0 {name=x3}
C {high_speed_comp_top.sym} 190 380 0 0 {name=x4}
C {high_speed_comp_top.sym} 190 570 0 0 {name=x5}
C {high_speed_comp_top.sym} 190 770 0 0 {name=x6}
C {high_speed_comp_top.sym} 190 940 0 0 {name=x7}
C {high_speed_comp_top.sym} 190 1120 0 0 {name=x8}
C {sky130_fd_pr/res_high_po_1p41.sym} -140 -110 0 0 {name=R1
L=1.41
model=res_high_po_1p41
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_high_po_1p41.sym} -140 60 0 0 {name=R2
L=1.41
model=res_high_po_1p41
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_high_po_1p41.sym} -140 230 0 0 {name=R3
L=1.41
model=res_high_po_1p41
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_high_po_1p41.sym} -140 430 0 0 {name=R4
L=1.41
model=res_high_po_1p41
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_high_po_1p41.sym} -140 610 0 0 {name=R5
L=1.41
model=res_high_po_1p41
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_high_po_1p41.sym} -140 810 0 0 {name=R6
L=1.41
model=res_high_po_1p41
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_high_po_1p41.sym} -140 990 0 0 {name=R7
L=1.41
model=res_high_po_1p41
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_high_po_1p41.sym} -140 1170 0 0 {name=R8
L=1.41
model=res_high_po_1p41
spiceprefix=X
mult=1}
C {ipin.sym} -210 -240 1 0 {name=p1 lab=VIN}
C {ipin.sym} -140 -260 1 0 {name=p2 lab=RES_TOP}
C {opin.sym} -140 1200 1 0 {name=p3 lab=RES_OUT}
C {opin.sym} 340 -210 0 0 {name=p4 lab=O0}
C {opin.sym} 340 -40 0 0 {name=p5 lab=O1
}
C {opin.sym} 340 140 0 0 {name=p6 lab=O2}
C {opin.sym} 340 340 0 0 {name=p7 lab=O3}
C {opin.sym} 340 530 0 0 {name=p8 lab=O4}
C {opin.sym} 340 730 0 0 {name=p9 lab=O5
}
C {opin.sym} 340 900 0 0 {name=p10 lab=O6}
C {opin.sym} 340 1080 0 0 {name=p11 lab=O7}
C {ipin.sym} -40 -250 1 0 {name=p12 lab=CLK}
C {sky130_fd_pr/res_high_po_1p41.sym} -480 -130 0 0 {name=R9
L=1.41
model=res_high_po_1p41
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_high_po_1p41.sym} -350 -130 0 0 {name=R10
L=1.41
model=res_high_po_1p41
spiceprefix=X
mult=1}
C {vdd.sym} -350 -100 2 0 {name=l17 lab=VSS}
C {vdd.sym} -480 -100 2 0 {name=l19 lab=VSS}
C {vdd.sym} -350 -160 0 0 {name=l20 lab=VSS}
C {vdd.sym} -480 -160 0 0 {name=l21 lab=VSS}
C {sky130_fd_pr/res_high_po_1p41.sym} -630 -130 0 0 {name=R11
L=1.41
model=res_high_po_1p41
spiceprefix=X
mult=1}
C {vdd.sym} -630 -100 2 0 {name=l22 lab=VSS}
C {vdd.sym} -630 -160 0 0 {name=l23 lab=VSS}
C {sky130_fd_pr/res_high_po_1p41.sym} -770 -130 0 0 {name=R12
L=1.41
model=res_high_po_1p41
spiceprefix=X
mult=1}
C {vdd.sym} -770 -100 2 0 {name=l24 lab=VSS}
C {vdd.sym} -770 -160 0 0 {name=l25 lab=VSS}
C {vdd.sym} -160 -110 3 0 {name=l26 lab=VSS}
C {vdd.sym} -160 60 3 0 {name=l27 lab=VSS}
C {vdd.sym} -160 230 3 0 {name=l28 lab=VSS}
C {vdd.sym} -160 430 3 0 {name=l29 lab=VSS}
C {vdd.sym} -160 610 3 0 {name=l30 lab=VSS}
C {vdd.sym} -160 810 3 0 {name=l31 lab=VSS}
C {vdd.sym} -160 990 3 0 {name=l32 lab=VSS}
C {vdd.sym} -160 1170 3 0 {name=l33 lab=VSS}
C {vdd.sym} -370 -130 3 0 {name=l34 lab=VSS}
C {vdd.sym} -500 -130 3 0 {name=l35 lab=VSS}
C {vdd.sym} -650 -130 3 0 {name=l36 lab=VSS}
C {vdd.sym} -790 -130 3 0 {name=l37 lab=VSS}
C {lab_wire.sym} 40 -150 0 0 {name=p13 sig_type=std_logic lab=VDD}
C {lab_wire.sym} 40 20 0 0 {name=p14 sig_type=std_logic lab=VDD}
C {lab_wire.sym} 40 200 0 0 {name=p15 sig_type=std_logic lab=VDD}
C {lab_wire.sym} 40 400 0 0 {name=p16 sig_type=std_logic lab=VDD}
C {lab_wire.sym} 40 590 0 0 {name=p17 sig_type=std_logic lab=VDD}
C {lab_wire.sym} 40 790 0 0 {name=p18 sig_type=std_logic lab=VDD}
C {lab_wire.sym} 40 960 0 0 {name=p19 sig_type=std_logic lab=VDD}
C {lab_wire.sym} 40 1140 0 0 {name=p20 sig_type=std_logic lab=VDD}
C {lab_wire.sym} 40 -130 0 0 {name=p21 sig_type=std_logic lab=VSS}
C {lab_wire.sym} 40 40 0 0 {name=p22 sig_type=std_logic lab=VSS}
C {lab_wire.sym} 40 220 0 0 {name=p23 sig_type=std_logic lab=VSS}
C {lab_wire.sym} 40 420 0 0 {name=p24 sig_type=std_logic lab=VSS}
C {lab_wire.sym} 40 610 0 0 {name=p25 sig_type=std_logic lab=VSS}
C {lab_wire.sym} 40 810 0 0 {name=p26 sig_type=std_logic lab=VSS}
C {lab_wire.sym} 40 980 0 0 {name=p27 sig_type=std_logic lab=VSS}
C {lab_wire.sym} 40 1160 0 0 {name=p28 sig_type=std_logic lab=VSS}
C {ipin.sym} -560 80 0 0 {name=p29 lab=VDD}
C {ipin.sym} -560 110 0 0 {name=p30 lab=VSS}
C {lab_wire.sym} -470 80 0 0 {name=p31 sig_type=std_logic lab=VDD}
C {lab_wire.sym} -470 110 0 0 {name=p32 sig_type=std_logic lab=VSS}
