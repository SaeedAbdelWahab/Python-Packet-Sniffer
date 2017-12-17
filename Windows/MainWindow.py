# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Windows/MainWindow.ui'
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
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(791, 677))
        MainWindow.setMaximumSize(QtCore.QSize(791, 677))
        #window center :
        frameGm = MainWindow.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        MainWindow.move(frameGm.topLeft())

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 40, 15))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.PacketTree = QtGui.QTreeWidget(self.centralwidget)
        self.PacketTree.setGeometry(QtCore.QRect(10, 280, 761, 155))
        self.PacketTree.setObjectName(_fromUtf8("PacketTree"))
        self.PacketTable = QtGui.QTreeWidget(self.centralwidget)
        self.PacketTable.setGeometry(QtCore.QRect(10, 60, 761, 211))
        self.PacketTable.setObjectName(_fromUtf8("PacketTable"))
        self.FilterText = QtGui.QTextEdit(self.centralwidget)
        self.FilterText.setGeometry(QtCore.QRect(70, 20, 581, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FilterText.sizePolicy().hasHeightForWidth())
        self.FilterText.setSizePolicy(sizePolicy)
        self.FilterText.setObjectName(_fromUtf8("FilterText"))
        self.FilterBtn = QtGui.QPushButton(self.centralwidget)
        self.FilterBtn.setGeometry(QtCore.QRect(670, 20, 93, 27))
        self.FilterBtn.setObjectName(_fromUtf8("FilterBtn"))
        self.StopSniffing = QtGui.QPushButton(self.centralwidget)
        self.StopSniffing.setGeometry(QtCore.QRect(140, 580, 104, 27))
        self.StopSniffing.setObjectName(_fromUtf8("StopSniffing"))
        self.StartButton = QtGui.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(30, 580, 104, 27))
        self.StartButton.setObjectName(_fromUtf8("StartButton"))
        self.Exit = QtGui.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(660, 580, 85, 27))
        self.Exit.setObjectName(_fromUtf8("Exit"))
        self.DisplayButton = QtGui.QPushButton(self.centralwidget)
        self.DisplayButton.setGeometry(QtCore.QRect(420, 570, 99, 27))
        self.DisplayButton.setVisible(False)
        self.DisplayButton.setObjectName(_fromUtf8("DisplayButton"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 440, 761, 131))
        self.plainTextEdit.setAcceptDrops(True)
        self.plainTextEdit.setUndoRedoEnabled(False)
        self.plainTextEdit.setPlainText(_fromUtf8(""))
        self.plainTextEdit.setCursorWidth(0)
        self.plainTextEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.Reselect = QtGui.QPushButton(self.centralwidget)
        self.Reselect.setGeometry(QtCore.QRect(532, 580, 121, 27))
        self.Reselect.setObjectName(_fromUtf8("Reselect"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setStatusTip(_fromUtf8(""))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 791, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menuBar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionAbout_us = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Windows/about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_us.setIcon(icon)
        self.actionAbout_us.setObjectName(_fromUtf8("actionAbout_us"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.Exit, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QObject.connect(self.PacketTable, QtCore.SIGNAL(_fromUtf8("itemClicked(QTreeWidgetItem*,int)")), self.DisplayButton.click)
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
        self.PacketTable.headerItem().setText(5, _translate("MainWindow", "Length", None))
        self.PacketTable.headerItem().setText(6, _translate("MainWindow", "Source port", None))
        self.FilterBtn.setText(_translate("MainWindow", "Filter", None))
        self.StopSniffing.setText(_translate("MainWindow", "Stop Sniffing", None))
        self.StartButton.setText(_translate("MainWindow", "Start Sniffing", None))
        self.Exit.setText(_translate("MainWindow", "Exit", None))
        self.DisplayButton.setText(_translate("MainWindow", "Display", None))
        self.Reselect.setText(_translate("MainWindow", "Re-select device", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuAbout.setTitle(_translate("MainWindow", "about", None))
        self.actionAbout_us.setText(_translate("MainWindow", "about us", None))
        self.actionAbout_us.setToolTip(_translate("MainWindow", "<html><head/><body><p>about us</p></body></html>", None))
        self.actionOpen.setText(_translate("MainWindow", "open", None))
        self.actionOpen.setToolTip(_translate("MainWindow", "open pcap file", None))
        self.actionSave.setText(_translate("MainWindow", "save", None))
        self.actionSave.setToolTip(_translate("MainWindow", "save pcap file", None))

