pys:
	${MAKE} -C gen all

py2app:
	python setup.py py2app --includes sip --packages PyQt4

clean:
	${MAKE} -C gen clean
