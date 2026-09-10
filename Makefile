# Makefile para compilar el proyecto LaTeX

PROJECT = main
BUILD_DIR = build
TEST_BUILD_DIR = $(BUILD_DIR)/build_tests

all: pdf

pdf: $(PROJECT).tex
	@mkdir -p $(BUILD_DIR)
	pdflatex -output-directory=$(BUILD_DIR) $(PROJECT).tex
	# Segunda pasada para referencias
	pdflatex -output-directory=$(BUILD_DIR) $(PROJECT).tex

# Regla mock por si decides añadir tests (ej. tests de sintaxis o scripts en el futuro)
tests:
	@mkdir -p $(TEST_BUILD_DIR)
	@echo "Construyendo tests en $(TEST_BUILD_DIR)... (Placeholder)"

clean:
	rm -rf $(BUILD_DIR)

.PHONY: all pdf tests clean
