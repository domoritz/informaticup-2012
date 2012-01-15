GUI = ../gui
PYUIC = pyuic
PYRCC = pyrcc4

all: pys resources_rc.py

UI 	:= $(shell cd ${GUI}; ls *.ui)

UIPY = $(UI:%.ui=%.py)

pys: ${UIPY}

${UIPY}:  %.py : ${GUI}/%.ui
	${PYUIC} -o $@ $<

resources_rc.py: ${GUI}/resources.qrc
	${PYRCC} -o $@ $<

clean:
	rm -f *.py
	rm -f *.pyc
	touch __init__.py
	
