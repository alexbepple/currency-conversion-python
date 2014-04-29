PYTHONPATH := PYTHONPATH=src

test-before-commit:
	$(PYTHONPATH) py.test test/unit
	$(PYTHONPATH) py.test test/integration

tdd:
	clear
	$(PYTHONPATH) watchmedo shell-command --patterns='*.py' --recursive --command='clear;py.test test/unit'

