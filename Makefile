# Developed by: Nemanja Radojkovic, www.linkedin.com/in/radojkovic

BASE_PYTHON := python3.9

.PHONY: venv
venv: pyproject.toml
	rm -rf venv
	$(BASE_PYTHON) -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/python -m pip install -e .