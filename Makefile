# Makefile para compilar el proyecto LaTeX

PROJECTS = main manual_ingenieria
BUILD_DIR = build
TEST_BUILD_DIR = $(BUILD_DIR)/build_tests

all: pdf

pdf:
	@for proj in $(PROJECTS); do \
		mkdir -p $(BUILD_DIR)/$$proj; \
		if [ -f $$proj.tex ]; then \
			C:/msys64/ucrt64/bin/pdflatex.exe -interaction=nonstopmode -output-directory=$(BUILD_DIR)/$$proj $$proj.tex; \
			C:/msys64/ucrt64/bin/pdflatex.exe -interaction=nonstopmode -output-directory=$(BUILD_DIR)/$$proj $$proj.tex; \
		fi \
	done

# Regla mock por si decides aadir tests (ej. tests de sintaxis o scripts en el futuro)
tests:
	@mkdir -p $(TEST_BUILD_DIR)
	@echo "Construyendo tests en $(TEST_BUILD_DIR)... (Placeholder)"

clean:
	find $(BUILD_DIR) -type f -delete 2>/dev/null || true
	@for proj in $(PROJECTS); do \
		rm -f $$proj.aux $$proj.log $$proj.out $$proj.toc $$proj.pdf $$proj.bbl $$proj.blg $$proj.fls $$proj.fdb_latexmk $$proj.synctex.gz; \
	done

.PHONY: all pdf tests clean
