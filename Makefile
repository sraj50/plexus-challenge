MODULE := app

venv:
	python3 -m venv venv
run:
	@python -m $(MODULE)
