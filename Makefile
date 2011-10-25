GUI = "./gui"
GEN = "./gen"
PYUIC = 'pyuic4'

UI 	:= $(shell cd ${GUI}; ls *.ui)

UI2 := $(shell ls ${GUI}/*.ui)
UIPY = $(UI:%.ui=%.py)

UIPY2 = $(UI:%.ui=gen/%.py)

pys: ${UIPY2}

${UIPY2}:  %.py : %.ui
	${PYUIC} -o $@ $<
