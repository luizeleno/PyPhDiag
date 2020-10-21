# Makefile to generate pdf or docx file with the code
# There must be a single md file in this folder!!!!!

AULA_MD := $(wildcard *.md)
AULA_PDF := ${AULA_MD:.md=.pdf}
AULA_DOCX := ${AULA_MD:.md=.docx}
AULA_HTML := ${AULA_MD:.md=.html}

default: $(AULA_PDF) $(AULA_DOCX) $(AULA_HTML)

$(AULA_PDF): $(AULA_MD)
	pandoc $< --filter pandoc-import-code -o $@ 

$(AULA_DOCX): $(AULA_MD)
	pandoc $< --filter pandoc-import-code -o $@ 

$(AULA_HTML): $(AULA_MD)
	pandoc $< --filter pandoc-import-code -s -o $@ 
