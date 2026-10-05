#!/bin/bash
# Usage: run_rcx.sh <cellname>
# where <cellname> is a magic layout (<cellname>.mag)

PDK_ROOT=/home/jrsharp/old_home_mnt/asic/sky130_pdk/share/pdk/
PDK=sky130A

for CELL in post_amplifier_routed; do

PDK_ROOT=${PDK_ROOT} magic -dnull -noconsole -rcfile ${PDK_ROOT}/${PDK}/libs.tech/magic/${PDK}.magicrc > magic.lvs.log << EOF
load $CELL
extract all
ext2spice lvs
ext2spice -o $CELL.lvs.out.spice
quit -noprompt
EOF

netgen -batch lvs "$CELL.lvs.out.spice $CELL" "$CELL.xschem.out.spice $CELL" ${PDK_ROOT}/${PDK}/libs.tech/netgen/${PDK}_setup.tcl


done

rm *.ext

echo "Done!"
exit 0 
