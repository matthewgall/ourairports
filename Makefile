NAME := ourairports
VERSION := 0.0.2

.PHONY: update
update:
	curl https://ourairports.com/data/airports.csv > ourairports/data/airports.csv
	gzip ourairports/data/airports.csv

.PHONY: docs
docs:
	pandoc --from=markdown --to=rst --output=README.rst README.md

.PHONY: build
build:
	python setup.py bdist_wheel --universal

.PHONY: upload
upload:
	twine upload dist/${NAME}-${VERSION}-py2.py3-none-any.whl