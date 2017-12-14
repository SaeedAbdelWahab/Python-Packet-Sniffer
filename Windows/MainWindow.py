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
        MainWindow.resize(791, 677)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 40, 15))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.PacketTree = QtGui.QTreeWidget(self.centralwidget)
        self.PacketTree.setGeometry(QtCore.QRect(10, 300, 761, 155))
        self.PacketTree.setObjectName(_fromUtf8("PacketTree"))
        self.PacketTable = QtGui.QTreeWidget(self.centralwidget)
        self.PacketTable.setGeometry(QtCore.QRect(10, 80, 761, 211))
        self.PacketTable.setObjectName(_fromUtf8("PacketTable"))
        self.FilterText = QtGui.QTextEdit(self.centralwidget)
        self.FilterText.setGeometry(QtCore.QRect(140, 40, 451, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FilterText.sizePolicy().hasHeightForWidth())
        self.FilterText.setSizePolicy(sizePolicy)
        self.FilterText.setObjectName(_fromUtf8("FilterText"))
        self.FilterBtn = QtGui.QPushButton(self.centralwidget)
        self.FilterBtn.setGeometry(QtCore.QRect(680, 40, 93, 27))
        self.FilterBtn.setObjectName(_fromUtf8("FilterBtn"))
        self.StopSniffing = QtGui.QPushButton(self.centralwidget)
        self.StopSniffing.setGeometry(QtCore.QRect(140, 0, 104, 27))
        self.StopSniffing.setObjectName(_fromUtf8("StopSniffing"))
        self.StartButton = QtGui.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(10, 0, 104, 27))
        self.StartButton.setObjectName(_fromUtf8("StartButton"))
        self.Exit = QtGui.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(270, 0, 85, 27))
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 460, 761, 131))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
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
        self.toolBar.addAction(self.actionAbout_us)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.Exit, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Packets", None))
        self.label.setText(_translate("MainWindow", "filter:", None))
        self.PacketTree.headerItem().setText(0, _translate("MainWindow", "Selected Packet Info", None))
        self.PacketTable.headerItem().setText(0, _translate("MainWindow", "No", None))
        self.PacketTable.headerItem().setText(1, _translate("MainWindow", "Time", None))
        self.PacketTable.headerItem().setText(2, _translate("MainWindow", "Source", None))
        self.PacketTable.headerItem().setText(3, _translate("MainWindow", "Destination", None))
        self.PacketTable.headerItem().setText(4, _translate("MainWindow", "Protocol", None))
        self.FilterBtn.setText(_translate("MainWindow", "Filter", None))
        self.StopSniffing.setText(_translate("MainWindow", "Stop Sniffing", None))
        self.StartButton.setText(_translate("MainWindow", "Start Sniffing", None))
        self.Exit.setText(_translate("MainWindow", "Exit", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionAbout_us.setText(_translate("MainWindow", "about us", None))
        self.actionAbout_us.setToolTip(_translate("MainWindow", "<html><head/><body><p>about us</p></body></html>", None))

