
.PHONY: distclean
distclean:
	rm -rf dist/*
.PHONY: clean
clean:
	rm -r __pycache__ PySimpleInput.egg-info

.PHONY: upload
upload:
	python3 -m twine upload dist/* --repository pypi
.PHONY: build
build:
	python3 -m build
.PHONY: test
test:
	python3 -m unittest discover

.all:
	$(MAKE) clean
	$(MAKE) distclean
	$(MAKE) build
	$(MAKE) upload
	$(MAKE) distclean
	$(MAKE) clean
