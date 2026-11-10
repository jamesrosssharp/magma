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
N -40 -260 -40 1240 {
lab=CLK}
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
C {vdd.sym} 40 -150 3 0 {name=l1 lab=VDD}
C {vdd.sym} 40 20 3 0 {name=l2 lab=VDD}
C {vdd.sym} 40 200 3 0 {name=l3 lab=VDD}
C {vdd.sym} 40 400 3 0 {name=l4 lab=VDD}
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
C {vdd.sym} 40 -130 3 0 {name=l5 lab=VSS}
C {vdd.sym} 40 40 3 0 {name=l6 lab=VSS}
C {vdd.sym} 40 220 3 0 {name=l7 lab=VSS}
C {vdd.sym} 40 420 3 0 {name=l8 lab=VSS}
C {vdd.sym} 40 610 3 0 {name=l9 lab=VSS}
C {vdd.sym} 40 590 3 0 {name=l10 lab=VDD}
C {vdd.sym} 40 810 3 0 {name=l11 lab=VSS}
C {vdd.sym} 40 790 3 0 {name=l12 lab=VDD}
C {vdd.sym} 40 980 3 0 {name=l13 lab=VSS}
C {vdd.sym} 40 960 3 0 {name=l14 lab=VDD}
C {vdd.sym} 40 1160 3 0 {name=l15 lab=VSS}
C {vdd.sym} 40 1140 3 0 {name=l16 lab=VDD}
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
C {vdd.sym} 40 -130 3 0 {name=l18 lab=VSS}
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
