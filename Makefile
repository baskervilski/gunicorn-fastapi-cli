BASE_PYTHON := python3.9

.PHONY: venv
venv: requirements.txt
	rm -rf venv
	$(BASE_PYTHON) -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/python -m pip install -r requirements.txt