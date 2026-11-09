v {xschem version=3.4.4 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 0 180 0 190 {lab=VSS}
N -420 190 0 190 {lab=VSS}
N -100 100 -100 120 {lab=#net1}
N 100 100 100 120 {lab=#net1}
N -100 120 100 120 {lab=#net1}
N -160 70 -140 70 {lab=VINP}
N 140 70 160 70 {lab=VINN}
N -100 10 -100 40 {lab=#net2}
N 100 10 100 40 {lab=#net3}
N -100 -120 -100 -100 {lab=VOUT_PLUS}
N 100 -120 100 -100 {lab=VOUT_MINUS}
N 380 -200 380 -180 {lab=VDD}
N -420 -200 380 -200 {lab=VDD}
N -360 -200 -360 -180 {lab=VDD}
N -250 -200 -250 -180 {lab=VDD}
N -100 -200 -100 -180 {lab=VDD}
N 100 -200 100 -180 {lab=VDD}
N 250 -200 250 -180 {lab=VDD}
N 60 -110 100 -110 {lab=VOUT_MINUS}
N -100 -110 -20 -110 {lab=VOUT_PLUS}
N -20 -60 20 -20 {lab=VOUT_PLUS}
N 20 -20 60 -20 {lab=VOUT_PLUS}
N -120 -80 -100 -80 {lab=VOUT_PLUS}
N 20 -110 60 -110 {lab=VOUT_MINUS}
N -20 -20 20 -60 {lab=VOUT_MINUS}
N -60 -20 -20 -20 {lab=VOUT_MINUS}
N 100 -80 130 -80 {lab=VOUT_MINUS}
N -20 -110 20 -150 {lab=VOUT_PLUS}
N 20 -150 60 -150 {lab=VOUT_PLUS}
N -20 -150 20 -110 {lab=VOUT_MINUS}
N -60 -150 -20 -150 {lab=VOUT_MINUS}
N -100 -100 -100 -50 {lab=VOUT_PLUS}
N 100 -100 100 -50 {lab=VOUT_MINUS}
N 20 -60 100 -60 {lab=VOUT_MINUS}
N -100 -60 -20 -60 {lab=VOUT_PLUS}
N -250 -120 -250 -110 {lab=VOUT_PLUS}
N -250 -110 -100 -110 {lab=VOUT_PLUS}
N 100 -110 250 -110 {lab=VOUT_MINUS}
N 250 -120 250 -110 {lab=VOUT_MINUS}
N -360 -120 -360 20 {lab=#net2}
N -360 20 -100 20 {lab=#net2}
N 100 20 380 20 {lab=#net3}
N 380 -120 380 20 {lab=#net3}
N 420 -150 440 -150 {lab=CLK}
N -420 -150 -400 -150 {lab=CLK}
N 440 -150 460 -150 {lab=CLK}
N -120 150 -40 150 {lab=CLK}
N -400 -150 -290 -150 {lab=CLK}
N 290 -150 420 -150 {lab=CLK}
C {sky130_fd_pr/nfet3_01v8_lvt.sym} -120 70 0 0 {name=M1
W=5
L=1
nf=1
mult=1
body=VSS
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=nfet_01v8_lvt
spiceprefix=X
}
C {sky130_fd_pr/nfet3_01v8_lvt.sym} 120 70 0 1 {name=M2
W=5
L=1
nf=1
mult=1
body=VSS
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=nfet_01v8_lvt
spiceprefix=X
}
C {sky130_fd_pr/nfet3_01v8_lvt.sym} -20 150 0 0 {name=M3
W=5
L=1
nf=1
mult=1
body=VSS
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=nfet_01v8_lvt
spiceprefix=X
}
C {ipin.sym} -420 190 0 0 {name=p1 lab=VSS}
C {ipin.sym} -420 -200 0 0 {name=p2 lab=VDD}
C {sky130_fd_pr/nfet3_01v8.sym} -80 -20 0 1 {name=M4
W=1
L=0.15
body=VSS
nf=1
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=nfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/nfet3_01v8.sym} 80 -20 0 0 {name=M5
W=1
L=0.15
body=VSS
nf=1
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=nfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/pfet3_01v8.sym} -80 -150 0 1 {name=M6
W=1
L=0.15
body=VDD
nf=1
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=pfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/pfet3_01v8.sym} 80 -150 0 0 {name=M7
W=1
L=0.15
body=VDD
nf=1
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=pfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/pfet3_01v8.sym} -270 -150 0 0 {name=M8
W=10
L=0.15
body=VDD
nf=1
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=pfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/pfet3_01v8.sym} -380 -150 0 0 {name=M9
W=10
L=0.15
body=VDD
nf=1
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=pfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/pfet3_01v8.sym} 270 -150 0 1 {name=M10
W=10
L=0.15
body=VDD
nf=1
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=pfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/pfet3_01v8.sym} 400 -150 0 1 {name=M11
W=10
L=0.15
body=VDD
nf=1
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=pfet_01v8
spiceprefix=X
}
C {ipin.sym} -420 -150 0 0 {name=p3 lab=CLK}
C {ipin.sym} -160 70 0 0 {name=p5 lab=VINP}
C {ipin.sym} 160 70 2 0 {name=p6 lab=VINN}
C {opin.sym} 130 -80 0 0 {name=p7 lab=VOUT_MINUS}
C {opin.sym} -120 -80 0 1 {name=p8 lab=VOUT_PLUS}
C {lab_wire.sym} 460 -150 0 0 {name=p4 sig_type=std_logic lab=CLK}
C {lab_wire.sym} -80 150 0 0 {name=p9 sig_type=std_logic lab=CLK}
