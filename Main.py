from pcapy import findalldevs
import os,sys,pcapy
from Windows.homewin import Ui_HomeWindow
from Windows.MainWindow import Ui_MainWindow
from PyQt4 import QtCore, QtGui
import socket
from struct import *
import datetime
import pcapy
import sys


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
def statueStart():
    ui_main.statusBar.showMessage("Sniffing...")
    sniffing = True
    cap = pcapy.open_live("wlp8s0" , 65536 , 1 , 0)
    
    (header, packet) = cap.next()
    parse_packet(packet)

def eth_addr (a) :
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
    return b

def parse_packet(packet) :
    eth_length = 14
     
    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH' , eth_header)
    eth_protocol = socket.ntohs(eth[2])
    rowPosition = ui_main.PacketTable.rowCount()
    ui_main.PacketTable.insertRow(rowPosition)
    ui_main.PacketTable.setItem(rowPosition,0,QtGui.QTableWidgetItem(str(eth_protocol)))
    ui_main.PacketTable.setItem(rowPosition , 1, QtGui.QTableWidgetItem(eth_addr(packet[0:6])))
    ui_main.PacketTable.setItem(rowPosition , 2, QtGui.QTableWidgetItem(eth_addr(packet[6:12])))
    #ui_main.PacketTable.setItem(rowPosition , 3, QtGui.QTableWidgetItem(eth_protocol))
    #sys.exit(1)




    
def statueStop():
    sniffing = False
    ui_main.statusBar.showMessage("Sniffing has been stopped.")
   


sniffing = False
app = QtGui.QApplication(sys.argv)
HomeWindow = QtGui.QMainWindow()
MainWindow = QtGui.QMainWindow()
ui_home = Ui_HomeWindow()
ui_main = Ui_MainWindow()
ui_home.setupUi(HomeWindow)
ui_main.setupUi(MainWindow)
if os.getuid()!=0 :
    msgBox = QtGui.QMessageBox()
    msgBox.warning(ui_home.widget, "not sudo", "please re-execute the app in admin(root) mode...")
    sys.exit()
devices = findalldevs()                  #list of strings to test addItems() function
ui_home.DeviceList.addItems(devices)                #adds elemnts of the list(devices) to QlistWidget
ui_home.select.clicked.connect(selectTrigger)       #when button (select) is been trigger it calls selectTrigger()
ui_main.StartButton.clicked.connect(statueStart)
ui_main.StopSniffing.clicked.connect(statueStop)
HomeWindow.show()
sys.exit(app.exec_())