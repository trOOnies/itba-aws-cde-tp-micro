COLOUR_GREEN=\033[0;32m
COLOUR_RED=\033[0;31m
COLOUR_BLUE=\033[0;34m
END_COLOUR=\033[0m

.PHONY: venv
venv:
	@if [ -d ".venv" ]; then\
		echo "${COLOUR_RED}El virtual environment ya existe, por favor borrarlo manualmente primero${END_COLOUR}";\
		false;\
	else\
		python3 -m venv .venv;\
	fi;

.PHONY: fmt
fmt:
	black .

.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: arch
arch:
	python3 nueva_arqui.py

.PHONY: arch2
arch:
	python3 nueva_arqui_2.py
