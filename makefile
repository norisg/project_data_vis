build/us_map.json: cb_2015_us_state_5m/cb_2015_us_state_5m.shp FORCE
	node_modules/.bin/topojson \
		-o $@ \
		--projection='width = 1400-75, height = 800-75, d3.geo.albersUsa() \
			.scale(1300) \
			.translate([width / 2, height / 2])' \
		--simplify=.5 \
		-- counties=$<

build/gz_2010_us_050_00_20m.shp: build/gz_2010_us_050_00_20m.zip
	unzip -od $(dir $@) $<
	touch $@


build/gz_2010_us_050_00_20m.zip:
	mkdir -p $(dir $@)
	curl -o $@ http://www2.census.gov/geo/tiger/GENZ2010/$(notdir $@)

FORCE: 



