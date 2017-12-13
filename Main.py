from pcapy import findalldevs
import os,sys
from Windows.homewin import Ui_HomeWindow
from Windows.MainWindow import Ui_MainWindow
from PyQt4 import QtCore, QtGui


def selectTrigger():
    if(ui_home.DeviceList.currentRow()==-1):
        msgBox = QtGui.QMessageBox()
        msgBox.warning(ui_home.widget, "Alarm", "please select your target device to continue...")
    else:
        SelectedDevice=ui_home.DeviceList.currentItem().text()
        nmsgBox = QtGui.QMessageBox()
        nmsgBox.warning(ui_home.widget, "SelectedDevice:", SelectedDevice+"          ")
        HomeWindow.close()
        MainWindow.show()
        



app = QtGui.QApplication(sys.argv)
HomeWindow = QtGui.QMainWindow()
MainWindow = QtGui.QMainWindow()
ui_home = Ui_HomeWindow()
ui_main = Ui_MainWindow()
ui_home.setupUi(HomeWindow)
ui_main.setupUi(MainWindow)
if os.getuid()!=0 :
    msgBox = QtGui.QMessageBox()
    msgBox.warning(ui.widget, "not sudo", "please re-execute the app in admin(root) mode...")
    sys.exit()
devices = findalldevs()                  #list of strings to test addItems() function
ui_home.DeviceList.addItems(devices)                #adds elemnts of the list(devices) to QlistWidget
ui_home.select.clicked.connect(selectTrigger)       #when button (select) is been trigger it calls selectTrigger()
HomeWindow.show()
sys.exit(app.exec_())