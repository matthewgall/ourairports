NAME := ourairports
VERSION := 1.1.0
DATE := $(shell date +'%Y%m%d')

.PHONY: update
update:
	curl https://raw.githubusercontent.com/davidmegginson/ourairports-data/main/airports.csv > ourairports/data/airports.csv
	curl https://raw.githubusercontent.com/davidmegginson/ourairports-data/main/airport-frequencies.csv > ourairports/data/frequencies.csv
	curl https://raw.githubusercontent.com/davidmegginson/ourairports-data/main/runways.csv > ourairports/data/runways.csv
	curl https://raw.githubusercontent.com/davidmegginson/ourairports-data/main/navaids.csv > ourairports/data/navaids.csv
	curl https://raw.githubusercontent.com/davidmegginson/ourairports-data/main/countries.csv > ourairports/data/countries.csv
	curl https://raw.githubusercontent.com/davidmegginson/ourairports-data/main/regions.csv > ourairports/data/regions.csv
	gzip -f ourairports/data/*

.PHONY: docs
docs:
	pandoc --from=markdown --to=rst --output=README.rst README.md

.PHONY: build
build:
	rm -rf build/ dist/ *.egg-info/
	VERSION=${VERSION}.${DATE} python3 setup.py sdist bdist_wheel --universal

.PHONY: upload
upload:
	twine upload dist/*

.PHONY: version
version:
	@echo ${VERSION}.${DATE}
