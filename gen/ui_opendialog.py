# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../gui/ui_opendialog.ui'
#
# Created: Sun Jan 15 23:11:44 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_OpenDialog(object):
    def setupUi(self, OpenDialog):
        OpenDialog.setObjectName(_fromUtf8("OpenDialog"))
        OpenDialog.resize(613, 636)
        self.gridLayout = QtGui.QGridLayout(OpenDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(OpenDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.distancesLayout = QtGui.QHBoxLayout()
        self.distancesLayout.setObjectName(_fromUtf8("distancesLayout"))
        self.distancesFileEdit = QtGui.QLineEdit(OpenDialog)
        self.distancesFileEdit.setObjectName(_fromUtf8("distancesFileEdit"))
        self.distancesLayout.addWidget(self.distancesFileEdit)
        self.distancesFileButton = QtGui.QPushButton(OpenDialog)
        self.distancesFileButton.setObjectName(_fromUtf8("distancesFileButton"))
        self.distancesLayout.addWidget(self.distancesFileButton)
        self.gridLayout.addLayout(self.distancesLayout, 1, 4, 1, 1)
        self.label_2 = QtGui.QLabel(OpenDialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.pricesLayout = QtGui.QHBoxLayout()
        self.pricesLayout.setObjectName(_fromUtf8("pricesLayout"))
        self.pricesFileEdit = QtGui.QLineEdit(OpenDialog)
        self.pricesFileEdit.setObjectName(_fromUtf8("pricesFileEdit"))
        self.pricesLayout.addWidget(self.pricesFileEdit)
        self.pricesFileButton = QtGui.QPushButton(OpenDialog)
        self.pricesFileButton.setObjectName(_fromUtf8("pricesFileButton"))
        self.pricesLayout.addWidget(self.pricesFileButton)
        self.gridLayout.addLayout(self.pricesLayout, 2, 4, 1, 1)
        self.dialogButton = QtGui.QDialogButtonBox(OpenDialog)
        self.dialogButton.setOrientation(QtCore.Qt.Horizontal)
        self.dialogButton.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help|QtGui.QDialogButtonBox.Ok)
        self.dialogButton.setObjectName(_fromUtf8("dialogButton"))
        self.gridLayout.addWidget(self.dialogButton, 5, 4, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.geneticOptions = QtGui.QGroupBox(OpenDialog)
        self.geneticOptions.setEnabled(False)
        self.geneticOptions.setObjectName(_fromUtf8("geneticOptions"))
        self.formLayout_2 = QtGui.QFormLayout(self.geneticOptions)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_5 = QtGui.QLabel(self.geneticOptions)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.popSizeEdit = QtGui.QSpinBox(self.geneticOptions)
        self.popSizeEdit.setMaximum(1000000)
        self.popSizeEdit.setProperty("value", 250)
        self.popSizeEdit.setObjectName(_fromUtf8("popSizeEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.popSizeEdit)
        self.label_6 = QtGui.QLabel(self.geneticOptions)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.childrenGroupEdit = QtGui.QSpinBox(self.geneticOptions)
        self.childrenGroupEdit.setMaximum(1000000)
        self.childrenGroupEdit.setProperty("value", 5)
        self.childrenGroupEdit.setObjectName(_fromUtf8("childrenGroupEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.childrenGroupEdit)
        self.label_7 = QtGui.QLabel(self.geneticOptions)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mutationEdit = QtGui.QSpinBox(self.geneticOptions)
        self.mutationEdit.setMaximum(100)
        self.mutationEdit.setProperty("value", 20)
        self.mutationEdit.setObjectName(_fromUtf8("mutationEdit"))
        self.horizontalLayout.addWidget(self.mutationEdit)
        self.label_11 = QtGui.QLabel(self.geneticOptions)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout.addWidget(self.label_11)
        self.formLayout_2.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_8 = QtGui.QLabel(self.geneticOptions)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_8)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.shorteningEdit = QtGui.QSpinBox(self.geneticOptions)
        self.shorteningEdit.setMaximum(100)
        self.shorteningEdit.setProperty("value", 10)
        self.shorteningEdit.setObjectName(_fromUtf8("shorteningEdit"))
        self.horizontalLayout_2.addWidget(self.shorteningEdit)
        self.label_12 = QtGui.QLabel(self.geneticOptions)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_2.addWidget(self.label_12)
        self.formLayout_2.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_9 = QtGui.QLabel(self.geneticOptions)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_9)
        self.maxGenerationsEdit = QtGui.QSpinBox(self.geneticOptions)
        self.maxGenerationsEdit.setMaximum(1000000)
        self.maxGenerationsEdit.setProperty("value", 50000)
        self.maxGenerationsEdit.setObjectName(_fromUtf8("maxGenerationsEdit"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.maxGenerationsEdit)
        self.label_4 = QtGui.QLabel(self.geneticOptions)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.catastrophyEdit = QtGui.QSpinBox(self.geneticOptions)
        self.catastrophyEdit.setMaximum(1000000)
        self.catastrophyEdit.setProperty("value", 2000)
        self.catastrophyEdit.setObjectName(_fromUtf8("catastrophyEdit"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.catastrophyEdit)
        self.stopAfterLabel = QtGui.QLabel(self.geneticOptions)
        self.stopAfterLabel.setObjectName(_fromUtf8("stopAfterLabel"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.stopAfterLabel)
        self.stopAfterEdit = QtGui.QSpinBox(self.geneticOptions)
        self.stopAfterEdit.setMaximum(1000000)
        self.stopAfterEdit.setProperty("value", 2000)
        self.stopAfterEdit.setObjectName(_fromUtf8("stopAfterEdit"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.stopAfterEdit)
        self.label_10 = QtGui.QLabel(self.geneticOptions)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_10)
        self.seedEdit = QtGui.QSpinBox(self.geneticOptions)
        self.seedEdit.setMaximum(1000000)
        self.seedEdit.setProperty("value", 42)
        self.seedEdit.setObjectName(_fromUtf8("seedEdit"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.seedEdit)
        self.horizontalLayout_3.addWidget(self.geneticOptions)
        self.clingoOptions = QtGui.QGroupBox(OpenDialog)
        self.clingoOptions.setEnabled(False)
        self.clingoOptions.setObjectName(_fromUtf8("clingoOptions"))
        self.formLayout = QtGui.QFormLayout(self.clingoOptions)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.clingoExecutableLabel = QtGui.QLabel(self.clingoOptions)
        self.clingoExecutableLabel.setObjectName(_fromUtf8("clingoExecutableLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.clingoExecutableLabel)
        self.clingoExecutableEdit = QtGui.QLineEdit(self.clingoOptions)
        self.clingoExecutableEdit.setObjectName(_fromUtf8("clingoExecutableEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.clingoExecutableEdit)
        self.clingoArgsLabel = QtGui.QLabel(self.clingoOptions)
        self.clingoArgsLabel.setObjectName(_fromUtf8("clingoArgsLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.clingoArgsLabel)
        self.clingoArgsEdit = QtGui.QLineEdit(self.clingoOptions)
        self.clingoArgsEdit.setObjectName(_fromUtf8("clingoArgsEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.clingoArgsEdit)
        self.horizontalLayout_3.addWidget(self.clingoOptions)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 5)
        self.label_3 = QtGui.QLabel(OpenDialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.geneticButton = QtGui.QRadioButton(OpenDialog)
        self.geneticButton.setObjectName(_fromUtf8("geneticButton"))
        self.horizontalLayout_4.addWidget(self.geneticButton)
        self.clingoButton = QtGui.QRadioButton(OpenDialog)
        self.clingoButton.setObjectName(_fromUtf8("clingoButton"))
        self.horizontalLayout_4.addWidget(self.clingoButton)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 4, 1, 1)
        self.gridLayout.setRowStretch(4, 1)

        self.retranslateUi(OpenDialog)
        QtCore.QObject.connect(self.dialogButton, QtCore.SIGNAL(_fromUtf8("accepted()")), OpenDialog.accept)
        QtCore.QObject.connect(self.dialogButton, QtCore.SIGNAL(_fromUtf8("rejected()")), OpenDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OpenDialog)

    def retranslateUi(self, OpenDialog):
        OpenDialog.setWindowTitle(QtGui.QApplication.translate("OpenDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("OpenDialog", "Distance File:", None, QtGui.QApplication.UnicodeUTF8))
        self.distancesFileEdit.setText(QtGui.QApplication.translate("OpenDialog", "sample_data/distances_more.txt", None, QtGui.QApplication.UnicodeUTF8))
        self.distancesFileButton.setText(QtGui.QApplication.translate("OpenDialog", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("OpenDialog", "Price File", None, QtGui.QApplication.UnicodeUTF8))
        self.pricesFileEdit.setText(QtGui.QApplication.translate("OpenDialog", "sample_data/prices_more.txt", None, QtGui.QApplication.UnicodeUTF8))
        self.pricesFileButton.setText(QtGui.QApplication.translate("OpenDialog", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.geneticOptions.setTitle(QtGui.QApplication.translate("OpenDialog", "Genetic Algorithm Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("OpenDialog", "Popsize:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("OpenDialog", "Children Group:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("OpenDialog", "Mutation:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("OpenDialog", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("OpenDialog", "Shortening:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("OpenDialog", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("OpenDialog", "Max Generation:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("OpenDialog", "Catastrophy After:", None, QtGui.QApplication.UnicodeUTF8))
        self.stopAfterLabel.setText(QtGui.QApplication.translate("OpenDialog", "Stop After:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("OpenDialog", "Seed:", None, QtGui.QApplication.UnicodeUTF8))
        self.clingoOptions.setTitle(QtGui.QApplication.translate("OpenDialog", "Clingo Algorithm Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.clingoExecutableLabel.setText(QtGui.QApplication.translate("OpenDialog", "Executable:", None, QtGui.QApplication.UnicodeUTF8))
        self.clingoExecutableEdit.setText(QtGui.QApplication.translate("OpenDialog", "clingo", None, QtGui.QApplication.UnicodeUTF8))
        self.clingoArgsLabel.setText(QtGui.QApplication.translate("OpenDialog", "Extra Arguments:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("OpenDialog", "Algorithm:", None, QtGui.QApplication.UnicodeUTF8))
        self.geneticButton.setText(QtGui.QApplication.translate("OpenDialog", "Genetic", None, QtGui.QApplication.UnicodeUTF8))
        self.clingoButton.setText(QtGui.QApplication.translate("OpenDialog", "Clingo", None, QtGui.QApplication.UnicodeUTF8))

