NAME := ourairports
VERSION := $(shell date +'%Y%m%d')

.PHONY: update
update:
	curl https://ourairports.com/data/airports.csv > ourairports/data/airports.csv
	curl https://ourairports.com/data/airport-frequencies.csv > ourairports/data/frequencies.csv
	curl https://ourairports.com/data/runways.csv > ourairports/data/runways.csv
	curl https://ourairports.com/data/navaids.csv > ourairports/data/navaids.csv
	curl https://ourairports.com/data/countries.csv > ourairports/data/countries.csv
	curl https://ourairports.com/data/regions.csv > ourairports/data/regions.csv
	gzip -f ourairports/data/*

.PHONY: docs
docs:
	pandoc --from=markdown --to=rst --output=README.rst README.md

.PHONY: build
build:
	rm -rf build/ dist/ *.egg-info/
	VERSION=${VERSION} python3 setup.py sdist bdist_wheel --universal

.PHONY: upload
upload:
	twine upload dist/*