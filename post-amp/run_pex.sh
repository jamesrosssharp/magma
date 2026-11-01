#!/bin/bash
# Usage: run_rcx.sh <cellname>
# where <cellname> is a magic layout (<cellname>.mag)

PDK_ROOT=/home/jrsharp/old_home_mnt/asic/sky130_pdk/share/pdk/
PDK=sky130A

for CELL in post_amplifier_routed; do

PDK_ROOT=${PDK_ROOT} magic -dnull -noconsole -rcfile ${PDK_ROOT}/${PDK}/libs.tech/magic/${PDK}.magicrc > magic.lvs.log << EOF
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
extract path extfiles
extract do unique
extract do resistance
extresist threshold 10000
extract all
ext2spice lvs
ext2spice cthresh 0.1
ext2spice extresist on
ext2spice -p extfiles -o $CELL.pex.spice
quit -noprompt
EOF

rm -rf extfiles

done

echo "Done!"
exit 0 
