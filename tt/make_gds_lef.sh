PDK_ROOT=${1:-/opt/pdk/}
PDK=sky130A

for CELL in tt_um_jamesrosssharp_high_speed_comp; do

	PDK_ROOT=${PDK_ROOT} magic -dnull -noconsole -rcfile ${PDK_ROOT}/${PDK}/libs.tech/magic/${PDK}.magicrc > magic.lvs.log << EOF
load ${CELL}_routed
gds write gds/${CELL}.gds
lef write lef/${CELL}.lef -hide -pinonly
EOF

done
