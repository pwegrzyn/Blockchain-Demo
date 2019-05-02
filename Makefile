install_deps:
    pip install -r requirements.txt

test:
    py.test tests

build:
	python setup.py build

install:
	python setup.py install

develop:
	python setup.py develop

.PHONY: init test