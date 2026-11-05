#!/bin/bash
# Usage: run_rcx.sh <cellname>
# where <cellname> is a magic layout (<cellname>.mag)

PDK_ROOT=${1:-"/opt/pdk/"}
PDK=${2:-sky130A}

for CELL in high_speed_comp_top_routed; do

PDK_ROOT=${PDK_ROOT} magic -dnull -noconsole -rcfile ${PDK_ROOT}/${PDK}/libs.tech/magic/${PDK}.magicrc > magic.pex.log << EOF
drc off
locking disable
crashbackups stop
box 0 0 0 0 
load $CELL
select top cell
flatten myflat
load myflat
cellname delete $CELL
cellname rename myflat $CELL
select top cell
extract warn all
extract do resistance
extract do unique
extract do local
extract path extfiles
extresist threshold 10
extract all
ext2spice lvs
ext2spice cthresh 0.1
ext2spice extresist on
ext2spice -p extfiles -o $CELL.pex.spice
feedback why
quit -noprompt
EOF

rm -rf extfiles

done

echo "Done!"
exit 0 
