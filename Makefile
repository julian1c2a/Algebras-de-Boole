# Makefile para compilar el proyecto LaTeX

PROJECT = main
BUILD_DIR = build
TEST_BUILD_DIR = $(BUILD_DIR)/build_tests

all: pdf

pdf: $(PROJECT).tex
	@mkdir -p $(BUILD_DIR)
	pdflatex -interaction=nonstopmode -output-directory=$(BUILD_DIR) $(PROJECT).tex
	# Segunda pasada para referencias
	pdflatex -interaction=nonstopmode -output-directory=$(BUILD_DIR) $(PROJECT).tex

# Regla mock por si decides añadir tests (ej. tests de sintaxis o scripts en el futuro)
tests:
	@mkdir -p $(TEST_BUILD_DIR)
	@echo "Construyendo tests en $(TEST_BUILD_DIR)... (Placeholder)"

clean:
clean:
	find $(BUILD_DIR) -type f -delete 2>/dev/null || true
	rm -f $(PROJECT).aux $(PROJECT).log $(PROJECT).out $(PROJECT).toc $(PROJECT).pdf $(PROJECT).bbl $(PROJECT).blg $(PROJECT).fls $(PROJECT).fdb_latexmk $(PROJECT).synctex.gz

.PHONY: all pdf tests clean
