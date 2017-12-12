# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homewin.ui'
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

class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName(_fromUtf8("HomeWindow"))
        HomeWindow.resize(488, 450)
        self.centralwidget = QtGui.QWidget(HomeWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 491, 451))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.select = QtGui.QPushButton(self.widget)
        self.select.setGeometry(QtCore.QRect(200, 380, 93, 27))
        self.select.setObjectName(_fromUtf8("select"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(110, 50, 281, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.DeviceList = QtGui.QListWidget(self.widget)
        self.DeviceList.setGeometry(QtCore.QRect(70, 80, 351, 251))
        self.DeviceList.setObjectName(_fromUtf8("DeviceList"))
        HomeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(HomeWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        HomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HomeWindow)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        HomeWindow.setWindowTitle(_translate("HomeWindow", "packet sniffer", None))
        self.select.setText(_translate("HomeWindow", "select", None))
        self.label.setText(_translate("HomeWindow", "please select interface to start sniffing", None))
        __sortingEnabled = self.DeviceList.isSortingEnabled()
        self.DeviceList.setSortingEnabled(False)
        item = self.DeviceList.item(0)
        self.DeviceList.setSortingEnabled(__sortingEnabled)
def selectTrigger():
    if(ui.DeviceList.currentRow()==-1):
        msgBox = QtGui.QMessageBox()
        msgBox.warning(ui.widget, "Alarm", "please select your target device to continue...")
    else:
        SelectedDevice=ui.DeviceList.currentItem().text()
        nmsgBox = QtGui.QMessageBox()
        nmsgBox.warning(ui.widget, "SelectedDevice:", SelectedDevice+"          ")
        #here we would excute a new pyqt form 
        sys.exit() 

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    HomeWindow = QtGui.QMainWindow()
    ui = Ui_HomeWindow()
    ui.setupUi(HomeWindow)
    test=["test1","test2","test3"]                  #list of strings to test addItems() function
    ui.DeviceList.addItems(test)                    #adds elemnts of the list(test) to QlistWidget
    ui.select.clicked.connect(selectTrigger)        #when button (select) is been trigger it calls selectTrigger()
    HomeWindow.show()
    sys.exit(app.exec_())

