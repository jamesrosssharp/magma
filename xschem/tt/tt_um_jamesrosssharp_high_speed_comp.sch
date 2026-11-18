v {xschem version=3.4.4 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 160 370 310 370 {
lab=clk_prime}
N 150 510 300 510 {
lab=clk_prime}
N 160 310 310 310 {
lab=VDPWR}
N 160 330 310 330 {
lab=VGND}
N 160 350 310 350 {
lab=ui_in[0]}
N 160 290 310 290 {
lab=ua[0]}
N 160 390 310 390 {
lab=ua[1]}
N 150 550 300 550 {
lab=VDPWR}
N 150 570 300 570 {
lab=VGND}
N 150 530 300 530 {
lab=ua[0]}
N 610 290 750 290 {
lab=#net1}
N 160 150 310 150 {
lab=ua[0]}
N 160 170 310 170 {
lab=ua[1]}
N 160 190 310 190 {
lab=VDPWR}
N 160 210 310 210 {
lab=VGND}
N 160 130 310 130 {
lab=clk_prime}
N 610 130 750 130 {
lab=#net2}
N 600 650 850 650 {
lab=#net3}
N 910 650 940 650 {
lab=#net4}
N 1000 650 1030 650 {
lab=#net5}
N 1090 650 1180 650 {
lab=VGND}
N 100 490 300 490 {
lab=#net6}
N -10 490 40 490 {
lab=VDPWR}
N 70 -10 80 -10 {
lab=clk}
N 830 130 850 130 {
lab=uo_out[1]}
N 830 290 860 290 {
lab=uo_out[0]}
N 850 460 940 460 {
lab=uio_out[0]}
N 740 480 860 480 {
lab=#net7}
N 760 500 770 500 {
lab=#net8}
N 770 520 860 520 {
lab=#net9}
N 600 630 860 630 {
lab=#net10}
N 860 600 860 630 {
lab=#net10}
N 850 580 940 580 {
lab=uio_out[6]}
N 770 580 770 610 {
lab=#net11}
N 600 610 770 610 {
lab=#net11}
N 600 590 760 590 {
lab=#net12}
N 760 560 760 590 {
lab=#net12}
N 760 560 860 560 {
lab=#net12}
N 850 540 940 540 {
lab=uio_out[4]}
N 740 540 770 540 {
lab=#net13}
N 740 540 740 570 {
lab=#net13}
N 600 570 740 570 {
lab=#net13}
N 720 520 770 520 {
lab=#net9}
N 720 520 720 550 {
lab=#net9}
N 600 550 720 550 {
lab=#net9}
N 850 500 940 500 {
lab=uio_out[2]}
N 700 500 770 500 {
lab=#net8}
N 700 500 700 530 {
lab=#net8}
N 600 530 700 530 {
lab=#net8}
N 680 480 740 480 {
lab=#net7}
N 680 480 680 510 {
lab=#net7}
N 600 510 680 510 {
lab=#net7}
N 660 460 770 460 {
lab=#net14}
N 660 460 660 490 {
lab=#net14}
N 600 490 650 490 {
lab=#net14}
N 650 490 660 490 {
lab=#net14}
C {ipin.sym} -150 -80 0 0 {name=p1 lab=clk}
C {ipin.sym} -150 -50 0 0 {name=p2 lab=ena}
C {ipin.sym} -150 -20 0 0 {name=p3 lab=rst_n}
C {iopin.sym} -80 20 0 0 {name=p4 lab=ua[0]}
C {iopin.sym} -80 50 0 0 {name=p5 lab=ua[1]}
C {iopin.sym} -80 80 0 0 {name=p6 lab=ua[2]}
C {iopin.sym} -80 110 0 0 {name=p7 lab=ua[3]}
C {iopin.sym} -80 140 0 0 {name=p8 lab=ua[4]}
C {iopin.sym} -80 170 0 0 {name=p9 lab=ua[5]}
C {iopin.sym} -80 200 0 0 {name=p10 lab=ua[6]}
C {iopin.sym} -80 230 0 0 {name=p11 lab=ua[7]}
C {ipin.sym} -150 10 0 0 {name=p12 lab=ui_in[0]}
C {ipin.sym} -150 40 0 0 {name=p13 lab=ui_in[1]}
C {ipin.sym} -150 70 0 0 {name=p14 lab=ui_in[2]}
C {ipin.sym} -150 100 0 0 {name=p15 lab=ui_in[3]}
C {ipin.sym} -150 130 0 0 {name=p16 lab=ui_in[4]}
C {ipin.sym} -150 160 0 0 {name=p17 lab=ui_in[5]}
C {ipin.sym} -150 190 0 0 {name=p18 lab=ui_in[6]}
C {ipin.sym} -150 220 0 0 {name=p19 lab=ui_in[7]}
C {ipin.sym} -150 250 0 0 {name=p20 lab=uio_in[0]}
C {ipin.sym} -150 280 0 0 {name=p21 lab=uio_in[1]}
C {ipin.sym} -150 310 0 0 {name=p22 lab=uio_in[2]}
C {ipin.sym} -150 340 0 0 {name=p23 lab=uio_in[3]}
C {ipin.sym} -150 370 0 0 {name=p24 lab=uio_in[4]}
C {ipin.sym} -150 400 0 0 {name=p25 lab=uio_in[5]}
C {ipin.sym} -150 430 0 0 {name=p26 lab=uio_in[6]}
C {ipin.sym} -150 460 0 0 {name=p27 lab=uio_in[7]}
C {opin.sym} -150 490 0 0 {name=p28 lab=uio_oe[0]}
C {opin.sym} -150 520 0 0 {name=p29 lab=uio_oe[1]}
C {opin.sym} -150 550 0 0 {name=p30 lab=uio_oe[2]}
C {opin.sym} -150 580 0 0 {name=p31 lab=uio_oe[3]}
C {opin.sym} -150 610 0 0 {name=p32 lab=uio_oe[4]}
C {opin.sym} -150 640 0 0 {name=p33 lab=uio_oe[5]}
C {opin.sym} -150 670 0 0 {name=p34 lab=uio_oe[6]}
C {opin.sym} -150 700 0 0 {name=p35 lab=uio_oe[7]}
C {iopin.sym} -150 730 0 0 {name=p36 lab=uio_out[0]}
C {iopin.sym} -150 760 0 0 {name=p37 lab=uio_out[1]}
C {iopin.sym} -150 790 0 0 {name=p38 lab=uio_out[2]}
C {iopin.sym} -150 820 0 0 {name=p39 lab=uio_out[3]}
C {iopin.sym} -150 850 0 0 {name=p40 lab=uio_out[4]}
C {iopin.sym} -150 880 0 0 {name=p41 lab=uio_out[5]}
C {iopin.sym} -150 910 0 0 {name=p42 lab=uio_out[6]}
C {iopin.sym} -150 940 0 0 {name=p43 lab=uio_out[7]}
C {opin.sym} -150 970 0 0 {name=p44 lab=uo_out[0]}
C {opin.sym} -150 1000 0 0 {name=p45 lab=uo_out[1]}
C {opin.sym} -150 1030 0 0 {name=p46 lab=uo_out[2]}
C {opin.sym} -150 1060 0 0 {name=p47 lab=uo_out[3]}
C {opin.sym} -150 1090 0 0 {name=p48 lab=uo_out[4]}
C {opin.sym} -150 1120 0 0 {name=p49 lab=uo_out[5]}
C {opin.sym} -150 1150 0 0 {name=p50 lab=uo_out[6]}
C {opin.sym} -150 1180 0 0 {name=p51 lab=uo_out[7]}
C {ipin.sym} -150 1210 0 0 {name=p52 lab=VDPWR}
C {ipin.sym} -150 1240 0 0 {name=p53 lab=VGND}
C {1bit_am.sym} 460 340 0 0 {name=x1}
C {flash_converter.sym} 450 570 0 0 {name=x2}
C {lab_pin.sym} 160 370 0 0 {name=p54 sig_type=std_logic lab=clk_prime}
C {lab_pin.sym} 150 510 0 0 {name=p55 sig_type=std_logic lab=clk_prime}
C {lab_pin.sym} 940 600 2 0 {name=p63 sig_type=std_logic lab=uio_out[7]}
C {sky130_stdcells/conb_1.sym} 70 780 0 0 {name=x3 VGND=VGND VNB=VNB VPB=VPB VPWR=VPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/conb_1.sym} 250 780 0 0 {name=x4 VGND=VGND VNB=VNB VPB=VPB VPWR=VPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/conb_1.sym} 450 780 0 0 {name=x5 VGND=VGND VNB=VNB VPB=VPB VPWR=VPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/conb_1.sym} 690 780 0 0 {name=x6 VGND=VGND VNB=VNB VPB=VPB VPWR=VPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/conb_1.sym} 70 890 0 0 {name=x7 VGND=VGND VNB=VNB VPB=VPB VPWR=VPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/conb_1.sym} 240 890 0 0 {name=x8 VGND=VGND VNB=VNB VPB=VPB VPWR=VPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/conb_1.sym} 450 890 0 0 {name=x9 VGND=VGND VNB=VNB VPB=VPB VPWR=VPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/conb_1.sym} 680 890 0 0 {name=x10 VGND=VGND VNB=VNB VPB=VPB VPWR=VPWR prefix=sky130_fd_sc_hd__ }
C {lab_pin.sym} 160 290 0 0 {name=p64 sig_type=std_logic lab=ua[0]}
C {lab_pin.sym} 160 330 0 0 {name=p66 sig_type=std_logic lab=VGND}
C {lab_pin.sym} 130 760 2 0 {name=p67 sig_type=std_logic lab=uio_oe[0]}
C {lab_pin.sym} 310 760 2 0 {name=p68 sig_type=std_logic lab=uio_oe[1]}
C {lab_pin.sym} 510 760 2 0 {name=p69 sig_type=std_logic lab=uio_oe[2]}
C {lab_pin.sym} 750 760 2 0 {name=p70 sig_type=std_logic lab=uio_oe[3]}
C {lab_pin.sym} 130 870 2 0 {name=p71 sig_type=std_logic lab=uio_oe[4]}
C {lab_pin.sym} 300 870 2 0 {name=p72 sig_type=std_logic lab=uio_oe[5]}
C {lab_pin.sym} 510 870 2 0 {name=p73 sig_type=std_logic lab=uio_oe[6]}
C {lab_pin.sym} 740 870 2 0 {name=p74 sig_type=std_logic lab=uio_oe[7]}
C {lab_pin.sym} 160 390 0 0 {name=p75 sig_type=std_logic lab=ua[1]}
C {lab_pin.sym} 150 550 0 0 {name=p76 sig_type=std_logic lab=VDPWR}
C {lab_pin.sym} 150 570 0 0 {name=p77 sig_type=std_logic lab=VGND}
C {lab_pin.sym} 150 530 0 0 {name=p78 sig_type=std_logic lab=ua[0]}
C {high_speed_comp_top.sym} 460 170 0 0 {name=x11}
C {lab_pin.sym} 160 350 0 0 {name=p80 sig_type=std_logic lab=ui_in[0]}
C {lab_pin.sym} 160 150 0 0 {name=p81 sig_type=std_logic lab=ua[0]}
C {lab_pin.sym} 160 170 0 0 {name=p82 sig_type=std_logic lab=ua[1]}
C {lab_pin.sym} 160 190 0 0 {name=p83 sig_type=std_logic lab=VDPWR}
C {lab_pin.sym} 160 210 0 0 {name=p84 sig_type=std_logic lab=VGND}
C {lab_pin.sym} 160 130 0 0 {name=p85 sig_type=std_logic lab=clk_prime}
C {sky130_stdcells/conb_1.sym} 70 990 0 0 {name=x12 VGND=VGND VNB=VNB VPB=VPB VPWR=VPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/conb_1.sym} 240 990 0 0 {name=x13 VGND=VGND VNB=VNB VPB=VPB VPWR=VPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/conb_1.sym} 450 990 0 0 {name=x14 VGND=VGND VNB=VNB VPB=VPB VPWR=VPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/conb_1.sym} 680 990 0 0 {name=x15 VGND=VGND VNB=VNB VPB=VPB VPWR=VPWR prefix=sky130_fd_sc_hd__ }
C {lab_pin.sym} 130 1010 2 0 {name=p87 sig_type=std_logic lab=uo_out[2]}
C {lab_pin.sym} 300 1010 2 0 {name=p88 sig_type=std_logic lab=uo_out[3]}
C {lab_pin.sym} 510 1010 2 0 {name=p89 sig_type=std_logic lab=uo_out[4]}
C {lab_pin.sym} 740 1010 2 0 {name=p90 sig_type=std_logic lab=uo_out[5]}
C {sky130_stdcells/conb_1.sym} 70 1090 0 0 {name=x16 VGND=VGND VNB=VNB VPB=VPB VPWR=VPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/conb_1.sym} 240 1090 0 0 {name=x17 VGND=VGND VNB=VNB VPB=VPB VPWR=VPWR prefix=sky130_fd_sc_hd__ }
C {lab_pin.sym} 130 1110 2 0 {name=p91 sig_type=std_logic lab=uo_out[6]}
C {lab_pin.sym} 300 1110 2 0 {name=p92 sig_type=std_logic lab=uo_out[7]}
C {sky130_fd_pr/res_high_po_1p41.sym} 70 490 3 0 {name=R11
L=1.41
model=res_high_po_1p41
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_high_po_1p41.sym} 880 650 1 0 {name=R1
L=1.41
model=res_high_po_1p41
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_high_po_1p41.sym} 970 650 1 0 {name=R2
L=1.41
model=res_high_po_1p41
spiceprefix=X
mult=1}
C {sky130_fd_pr/res_high_po_1p41.sym} 1060 650 1 0 {name=R3
L=1.41
model=res_high_po_1p41
spiceprefix=X
mult=1}
C {lab_pin.sym} -10 490 3 0 {name=p93 sig_type=std_logic lab=VDPWR}
C {lab_pin.sym} 70 510 0 0 {name=p94 sig_type=std_logic lab=VGND}
C {lab_pin.sym} 880 630 0 0 {name=p95 sig_type=std_logic lab=VGND}
C {lab_pin.sym} 970 630 0 0 {name=p96 sig_type=std_logic lab=VGND}
C {lab_pin.sym} 1060 630 0 0 {name=p97 sig_type=std_logic lab=VGND}
C {lab_pin.sym} 1180 650 2 0 {name=p98 sig_type=std_logic lab=VGND}
C {sky130_stdcells/clkbuf_16.sym} 120 -10 0 0 {name=x18 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/decap_3.sym} 110 -70 0 0 {name=x19 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/tapvpwrvgnd_1.sym} 120 -120 0 0 {name=x20 VGND=VGND VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {lab_pin.sym} 70 -10 0 0 {name=p99 sig_type=std_logic lab=clk}
C {lab_pin.sym} 160 -10 2 0 {name=p100 sig_type=std_logic lab=clk_prime}
C {sky130_stdcells/buf_16.sym} 790 130 0 0 {name=x21 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {lab_pin.sym} 850 130 2 0 {name=p86 sig_type=std_logic lab=uo_out[1]}
C {lab_pin.sym} 860 290 2 0 {name=p79 sig_type=std_logic lab=uo_out[0]}
C {sky130_stdcells/buf_16.sym} 790 290 0 0 {name=x22 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/decap_3.sym} 1060 150 0 0 {name=x23 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/tapvpwrvgnd_1.sym} 1070 100 0 0 {name=x24 VGND=VGND VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/decap_3.sym} 1060 320 0 0 {name=x25 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/tapvpwrvgnd_1.sym} 1070 270 0 0 {name=x26 VGND=VGND VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {lab_pin.sym} 940 460 2 0 {name=p56 sig_type=std_logic lab=uio_out[0]}
C {lab_pin.sym} 940 480 2 0 {name=p57 sig_type=std_logic lab=uio_out[1]}
C {lab_pin.sym} 940 500 2 0 {name=p58 sig_type=std_logic lab=uio_out[2]}
C {lab_pin.sym} 940 520 2 0 {name=p59 sig_type=std_logic lab=uio_out[3]}
C {lab_pin.sym} 940 540 2 0 {name=p60 sig_type=std_logic lab=uio_out[4]}
C {lab_pin.sym} 940 560 2 0 {name=p61 sig_type=std_logic lab=uio_out[5]}
C {lab_pin.sym} 940 580 2 0 {name=p62 sig_type=std_logic lab=uio_out[6]}
C {sky130_stdcells/buf_16.sym} 810 460 0 0 {name=x27 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/buf_16.sym} 900 480 0 0 {name=x28 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/buf_16.sym} 810 500 0 0 {name=x29 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/buf_16.sym} 810 540 0 0 {name=x31 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/buf_16.sym} 900 560 0 0 {name=x32 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/buf_16.sym} 810 580 0 0 {name=x33 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/buf_16.sym} 900 600 0 0 {name=x34 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/buf_16.sym} 900 520 0 0 {name=x30 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/decap_3.sym} 1280 430 0 0 {name=x35 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/tapvpwrvgnd_1.sym} 1290 380 0 0 {name=x36 VGND=VGND VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/decap_3.sym} 1280 530 0 0 {name=x37 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/tapvpwrvgnd_1.sym} 1290 480 0 0 {name=x38 VGND=VGND VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/decap_3.sym} 1280 610 0 0 {name=x39 VGND=VGND VNB=VGND VPB=VDPWR VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {sky130_stdcells/tapvpwrvgnd_1.sym} 1290 560 0 0 {name=x40 VGND=VGND VPWR=VDPWR prefix=sky130_fd_sc_hd__ }
C {lab_pin.sym} 160 310 0 0 {name=p65 sig_type=std_logic lab=VDPWR}
