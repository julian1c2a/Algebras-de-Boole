# Makefile para compilar el proyecto LaTeX

SRC_DIR = src/latex
BUILD_DIR = build/latex
DOC_OUT_DIR = doc_out/latex
DOC_OUT_MD_DIR = doc_out/markdown
TEST_BUILD_DIR = build/build_tests

# Busca todos los subdirectorios en src/latex
PROJECTS = $(notdir $(wildcard $(SRC_DIR)/*))

all: docs

docs:
	@for proj in $(PROJECTS); do \
		if [ -f "$(SRC_DIR)/$$proj/$$proj.tex" ]; then \
			echo "========================================"; \
			echo "Compilando $$proj..."; \
			echo "========================================"; \
			mkdir -p "$(BUILD_DIR)/$$proj"; \
			mkdir -p "$(DOC_OUT_DIR)/$$proj"; \
			cd "$(SRC_DIR)/$$proj" && \
			C:/msys64/ucrt64/bin/pdflatex.exe -interaction=nonstopmode -synctex=1 -output-directory="../../../$(BUILD_DIR)/$$proj" "$$proj.tex" ; \
			C:/msys64/ucrt64/bin/pdflatex.exe -interaction=nonstopmode -synctex=1 -output-directory="../../../$(BUILD_DIR)/$$proj" "$$proj.tex" ; \
			if [ -f "../../../$(BUILD_DIR)/$$proj/$$proj.pdf" ]; then \
				cp "../../../$(BUILD_DIR)/$$proj/$$proj.pdf" "../../../$(DOC_OUT_DIR)/$$proj/" ; \
				rm -f "../../../$(BUILD_DIR)/$$proj/$$proj.pdf" ; \
			fi; \
			if [ -f "../../../$(BUILD_DIR)/$$proj/$$proj.synctex.gz" ]; then \
				cp "../../../$(BUILD_DIR)/$$proj/$$proj.synctex.gz" "../../../$(DOC_OUT_DIR)/$$proj/" ; \
				rm -f "../../../$(BUILD_DIR)/$$proj/$$proj.synctex.gz" ; \
			fi; \
			mkdir -p "../../../$(DOC_OUT_MD_DIR)/$$proj"; \
			pandoc "$$proj.tex" -o "../../../$(DOC_OUT_MD_DIR)/$$proj/$$proj.md" --katex --from=latex --to=markdown ; \
			cd ../../../; \
		else \
			echo "Aviso: No se encontró $(SRC_DIR)/$$proj/$$proj.tex"; \
		fi \
	done

tests:
	@mkdir -p $(TEST_BUILD_DIR)
	@echo "Construyendo tests en $(TEST_BUILD_DIR)... (Placeholder)"

clean:
	rm -rf build/* doc_out/*

.PHONY: all docs tests clean
