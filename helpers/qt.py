# -*- coding: utf-8 -*-
from PyQt4 import QtCore

class Settings(QtCore.QSettings):

	def value(self, *args, **kwargs):
		return c(QtCore.QSettings.value(self, *args, **kwargs))

def c(value):
	if type(value) is QtCore.QVariant:
		if value.typeName() == 'QString':
			return value.toString()
		elif value.typeName() == 'bool':
			return value.toBool()
		elif value.typeName() == 'int':
			return value.toInt()[0]
		elif value.typeName() == 'double':
			return value.toDouble()[0]
		elif value.typeName() == 'qulonglong':
			return value.toULongLong()[0]
		elif value.typeName() == 'QByteArray':
			return value.toByteArray()
		elif value.typeName() == 'QStringList':
			return value.toStringList()
		elif value.typeName() == 'QDate':
			return value.toDate()
		elif value.typeName() == 'QDateTime':
			return value.toDateTime()
		elif value.typeName() == 'QPoint':
			return value.toPoint()
		elif value.typeName() == 'QSize':
			return value.toSize()
		elif value.typeName() == 'None' or value.typeName() is None:
			return None
		else:
			print("\033[01;31munknown type {0}\033[m".format(value.typeName()))
			return value
	else:
		return value
