all: extract_results

BUILD_DIR=build

.PHONY:	extract_results

CORNERS=tt ss sf fs ff
#CORNERS=tt
RAW_FILES=$(addprefix $(BUILD_DIR)/,$(addsuffix .raw, $(CORNERS)))

$(info $(RAW_FILES))

$(BUILD_DIR)/%.raw: ../../tt/tt_um_jamesrosssharp_high_speed_comp.pex.spice testbench.spice
	@mkdir -p $(BUILD_DIR)
	$(eval CORNER := $(notdir $(basename $@)))
	@echo "Building for corner $(CORNER)"
	@# Substitute parameters
	cat testbench.spice | sed s/\$$\{RAW_FILE\}/$(BUILD_DIR)\\/$(CORNER).raw/g | sed s/\$$\{CORNER\}/$(CORNER)/g > $(BUILD_DIR)/top_$(CORNER).spice
	@ngspice $(BUILD_DIR)/top_$(CORNER).spice

extract_results: $(RAW_FILES)
	@mkdir -p results
	python3 extract_results.py | tee results/results.txt

clean:
	rm -rf $(BUILD_DIR)
