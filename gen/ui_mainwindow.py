# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../gui/ui_mainwindow.ui'
#
# Created: Thu Jan 12 22:49:07 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(944, 652)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.graphicsView = GraphWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(480, 480))
        self.graphicsView.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.graphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.graphicsView.setCacheMode(QtGui.QGraphicsView.CacheBackground)
        self.graphicsView.setResizeAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.graphicsView.setViewportUpdateMode(QtGui.QGraphicsView.SmartViewportUpdate)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayoutWidget = QtGui.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalGroupBox_2 = QtGui.QGroupBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalGroupBox_2.sizePolicy().hasHeightForWidth())
        self.verticalGroupBox_2.setSizePolicy(sizePolicy)
        self.verticalGroupBox_2.setObjectName(_fromUtf8("verticalGroupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_4.setMargin(5)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.shoppingTree = QtGui.QTreeWidget(self.verticalGroupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shoppingTree.sizePolicy().hasHeightForWidth())
        self.shoppingTree.setSizePolicy(sizePolicy)
        self.shoppingTree.setMinimumSize(QtCore.QSize(280, 0))
        self.shoppingTree.setAlternatingRowColors(True)
        self.shoppingTree.setObjectName(_fromUtf8("shoppingTree"))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.shoppingTree.headerItem().setFont(0, font)
        item_0 = QtGui.QTreeWidgetItem(self.shoppingTree)
        item_1 = QtGui.QTreeWidgetItem(item_0)
        self.shoppingTree.header().setDefaultSectionSize(60)
        self.verticalLayout_4.addWidget(self.shoppingTree)
        self.formGroupBox = QtGui.QGroupBox(self.verticalGroupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.formGroupBox.sizePolicy().hasHeightForWidth())
        self.formGroupBox.setSizePolicy(sizePolicy)
        self.formGroupBox.setObjectName(_fromUtf8("formGroupBox"))
        self.formLayout = QtGui.QFormLayout(self.formGroupBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_3 = QtGui.QLabel(self.formGroupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.expenses = QtGui.QLabel(self.formGroupBox)
        self.expenses.setMinimumSize(QtCore.QSize(10, 0))
        self.expenses.setObjectName(_fromUtf8("expenses"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.expenses)
        self.label_4 = QtGui.QLabel(self.formGroupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_2 = QtGui.QLabel(self.formGroupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.spendings = QtGui.QLabel(self.formGroupBox)
        self.spendings.setMinimumSize(QtCore.QSize(10, 0))
        self.spendings.setObjectName(_fromUtf8("spendings"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.spendings)
        self.total = QtGui.QLabel(self.formGroupBox)
        self.total.setMinimumSize(QtCore.QSize(10, 0))
        self.total.setObjectName(_fromUtf8("total"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.total)
        self.verticalLayout_4.addWidget(self.formGroupBox)
        self.verticalLayout.addWidget(self.verticalGroupBox_2)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 944, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionRun = QtGui.QAction(MainWindow)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuTools.addAction(self.actionPreferences)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionRun)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Shoppingtour", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalGroupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Shopping list", None, QtGui.QApplication.UnicodeUTF8))
        self.shoppingTree.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Store", None, QtGui.QApplication.UnicodeUTF8))
        self.shoppingTree.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Product", None, QtGui.QApplication.UnicodeUTF8))
        self.shoppingTree.headerItem().setToolTip(1, QtGui.QApplication.translate("MainWindow", "Number of products to be bought", None, QtGui.QApplication.UnicodeUTF8))
        self.shoppingTree.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Number", None, QtGui.QApplication.UnicodeUTF8))
        self.shoppingTree.headerItem().setToolTip(2, QtGui.QApplication.translate("MainWindow", "Number of products to be bought", None, QtGui.QApplication.UnicodeUTF8))
        self.shoppingTree.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "Price", None, QtGui.QApplication.UnicodeUTF8))
        self.shoppingTree.headerItem().setToolTip(3, QtGui.QApplication.translate("MainWindow", "Price per item", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.shoppingTree.isSortingEnabled()
        self.shoppingTree.setSortingEnabled(False)
        self.shoppingTree.topLevelItem(0).setText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.shoppingTree.topLevelItem(0).child(0).setText(1, QtGui.QApplication.translate("MainWindow", "Milk", None, QtGui.QApplication.UnicodeUTF8))
        self.shoppingTree.topLevelItem(0).child(0).setText(2, QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.shoppingTree.topLevelItem(0).child(0).setText(3, QtGui.QApplication.translate("MainWindow", "5.34", None, QtGui.QApplication.UnicodeUTF8))
        self.shoppingTree.setSortingEnabled(__sortingEnabled)
        self.formGroupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Expenses:", None, QtGui.QApplication.UnicodeUTF8))
        self.expenses.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Spendings:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Total costs:", None, QtGui.QApplication.UnicodeUTF8))
        self.spendings.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.total.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setText(QtGui.QApplication.translate("MainWindow", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setToolTip(QtGui.QApplication.translate("MainWindow", "run the calculation", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRun.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setToolTip(QtGui.QApplication.translate("MainWindow", "Quit application", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))

from gui.graphWidget import GraphWidget
