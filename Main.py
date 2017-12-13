from pcapy import findalldevs
import os,sys
from Windows.homewin import Ui_HomeWindow
from PyQt4 import QtCore, QtGui


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



app = QtGui.QApplication(sys.argv)
HomeWindow = QtGui.QMainWindow()
ui = Ui_HomeWindow()
ui.setupUi(HomeWindow)
if os.getuid()!=0 :
    msgBox = QtGui.QMessageBox()
    msgBox.warning(ui.widget, "not sudo", "please re-execute the app in admin(root) mode...")
    sys.exit()
devices = findalldevs()                  #list of strings to test addItems() function
ui.DeviceList.addItems(devices)                #adds elemnts of the list(devices) to QlistWidget
ui.select.clicked.connect(selectTrigger)       #when button (select) is been trigger it calls selectTrigger()
HomeWindow.show()
sys.exit(app.exec_())