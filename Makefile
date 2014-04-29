PYTHONPATH := PYTHONPATH=src

check: flake8 test-unit test-integration

flake8:
	flake8 .

test-unit:
	$(PYTHONPATH) py.test test/unit

test-integration:
	$(PYTHONPATH) py.test test/integration

tdd:
	clear
	$(PYTHONPATH) watchmedo shell-command --patterns='*.py' --recursive --command='clear;py.test test/unit'

