all: lint

black: force
	black src/

deps: force
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

flake8: force
	flake8 src/

lint: black flake8

mypy: force
	mypy src/

force: ;
