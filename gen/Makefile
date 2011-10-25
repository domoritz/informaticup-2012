GUI = ../gui
PYUIC = pyuic

UI 	:= $(shell cd ${GUI}; ls *.ui)

UIPY = $(UI:%.ui=%.py)

pys: ${UIPY}

${UIPY}:  %.py : ${GUI}/%.ui
	${PYUIC} -o $@ $<
