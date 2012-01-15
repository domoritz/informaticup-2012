pys:
	${MAKE} -C gen all

py2exe:
	python compyle.py

py2app:
	python setup.py py2app --includes sip --packages PyQt4

clean:
	${MAKE} -C gen clean
