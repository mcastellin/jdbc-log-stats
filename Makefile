setup:
	@python3 -m venv ~/.jdbclog

install:
	@. ~/.jdbclog/bin/activate &&\
		pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	@. ~/.jdbclog/bin/activate &&\
		find . -name "*.py" -exec pylint --disable=R,C {} \;

test:
	@. ~/.jdbclog/bin/activate &&\
		python -m pytest -vv --cov=parser parser/*_test.py
fmt:
	@. ~/.jdbclog/bin/activate &&\
		find . -name "*.py" -exec black {} \;

all: setup install lint test
