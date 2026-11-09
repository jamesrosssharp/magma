v {xschem version=3.4.6RC file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N -80 -130 -40 -130 {lab=#net1}
N -80 -130 -80 200 {lab=#net1}
N -80 200 -40 200 {lab=#net1}
N -170 40 -80 40 {lab=#net1}
N -170 0 -170 60 {lab=#net1}
N 80 -80 80 -60 {lab=#net2}
N -170 -80 80 -80 {lab=#net2}
N -170 -80 -170 -60 {lab=#net2}
N -0 -100 -0 -80 {lab=#net2}
N 80 0 80 60 {lab=#net3}
N 0 -30 40 -30 {lab=VLAT_MINUS}
N 0 -30 -0 90 {lab=VLAT_MINUS}
N -0 90 40 90 {lab=VLAT_MINUS}
N -260 -30 -210 -30 {lab=VLAT_PLUS}
N -260 -30 -260 90 {lab=VLAT_PLUS}
N -260 90 -210 90 {lab=VLAT_PLUS}
N -170 120 -170 160 {lab=#net4}
N -170 160 80 160 {lab=#net4}
N 80 120 80 160 {lab=#net4}
N 0 160 0 170 {lab=#net4}
N 200 -30 220 -30 {lab=#net3}
N 200 -30 200 90 {lab=#net3}
N 200 90 220 90 {lab=#net3}
N 80 30 200 30 {lab=#net3}
N 260 0 260 60 {lab=#net5}
N 260 -220 260 -60 {lab=VDD}
N 0 -220 260 -220 {lab=VDD}
N 0 -220 -0 -160 {lab=VDD}
N 0 230 0 300 {lab=VSS}
N 0 300 260 300 {lab=VSS}
N 260 120 260 300 {lab=VSS}
C {sky130_fd_pr/nfet3_01v8.sym} -190 90 0 0 {name=M1
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
C {sky130_fd_pr/nfet3_01v8.sym} 60 90 0 0 {name=M2
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
C {sky130_fd_pr/nfet3_01v8.sym} -20 200 0 0 {name=M3
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
C {sky130_fd_pr/pfet3_01v8.sym} -190 -30 0 0 {name=M4
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
C {sky130_fd_pr/pfet3_01v8.sym} 60 -30 0 0 {name=M5
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
C {sky130_fd_pr/pfet3_01v8.sym} -20 -130 0 0 {name=M6
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
C {sky130_fd_pr/nfet3_01v8.sym} 240 90 0 0 {name=M7
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
C {sky130_fd_pr/pfet3_01v8.sym} 240 -30 0 0 {name=M8
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
C {ipin.sym} -260 30 0 0 {name=p1 lab=VLAT_PLUS}
C {ipin.sym} 0 30 0 0 {name=p2 lab=VLAT_MINUS}
C {ipin.sym} 0 -220 0 0 {name=p3 lab=VDD}
C {ipin.sym} 0 300 0 0 {name=p4 lab=VSS}
C {opin.sym} 260 30 0 0 {name=p5 lab=VOUT}
