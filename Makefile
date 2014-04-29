test-before-commit:
	PYTHONPATH=src py.test test/unit
	PYTHONPATH=src py.test test/integration

tdd:
	clear
	PYTHONPATH=src watchmedo shell-command --patterns='*.py' --recursive --command='clear;py.test test/unit'

