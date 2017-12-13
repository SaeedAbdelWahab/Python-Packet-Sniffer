# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindoww.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(779, 610)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.StopSniffing = QtGui.QPushButton(self.splitter)
        self.StopSniffing.setObjectName(_fromUtf8("StopSniffing"))
        self.StartButton = QtGui.QPushButton(self.splitter)
        self.StartButton.setObjectName(_fromUtf8("StartButton"))
        self.Exit = QtGui.QPushButton(self.splitter)
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.gridLayout.addWidget(self.splitter, 6, 0, 1, 2)
        self.PacketTree = QtGui.QTreeWidget(self.centralwidget)
        self.PacketTree.setObjectName(_fromUtf8("PacketTree"))
        self.gridLayout.addWidget(self.PacketTree, 3, 0, 1, 1)
        self.PacketTable = QtGui.QTreeWidget(self.centralwidget)
        self.PacketTable.setObjectName(_fromUtf8("PacketTable"))
        self.gridLayout.addWidget(self.PacketTable, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setStatusTip(_fromUtf8(""))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionAbout_us = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Windows/about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_us.setIcon(icon)
        self.actionAbout_us.setObjectName(_fromUtf8("actionAbout_us"))
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAbout_us)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.Exit, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Packets", None))
        self.label.setText(_translate("MainWindow", "Sniffing", None))
        self.StopSniffing.setText(_translate("MainWindow", "Stop Sniffing", None))
        self.StartButton.setText(_translate("MainWindow", "Start Sniffing", None))
        self.Exit.setText(_translate("MainWindow", "Exit", None))
        self.PacketTree.headerItem().setText(0, _translate("MainWindow", "Selected Packet Info", None))
        self.PacketTable.headerItem().setText(0, _translate("MainWindow", "Protocol", None))
        self.PacketTable.headerItem().setText(1, _translate("MainWindow", "Source MAC", None))
        self.PacketTable.headerItem().setText(2, _translate("MainWindow", "Destinatiin MAC", None))
        self.PacketTable.headerItem().setText(3, _translate("MainWindow", "Length", None))
        self.PacketTable.headerItem().setText(4, _translate("MainWindow", "Info", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionAbout_us.setText(_translate("MainWindow", "about us", None))
        self.actionAbout_us.setToolTip(_translate("MainWindow", "<html><head/><body><p>about us</p></body></html>", None))

