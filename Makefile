THIS_DIR := $(dir $(lastword $(MAKEFILE_LIST)))
OUTDIR := .
DEFAULTS := $(THIS_DIR)md/defaults.yaml
include $(THIS_DIR)wg21/Makefile

$(THIS_DIR)md/defaults.yaml : $(THIS_DIR)md/defaults.py
	python $< > $@

$(OUTDIR)/sd6.md : sd6.py sd6.tmpl macros.yaml reduced.json $(THIS_DIR)md/defaults.yaml
	python $< > $@

$(OUTDIR)/sd6.html : $(OUTDIR)/sd6.md
	$(PANDOC) --bibliography $(THIS_DIR)md/wg21_fmt.yaml --bibliography $(DATADIR)/csl.json --bibliography $(THIS_DIR)md/early.yaml

reduced.json : md/wg21_fmt.yaml wg21/data/index.yaml md/early.yaml reduce_refs.py
	python reduce_refs.py > $@ 


.DEFAULT_GOAL := $(OUTDIR)/sd6.html
