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
import time
import threading

Row=0
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def selectTrigger():
    if(ui_home.DeviceList.currentRow()==-1):
        msgBox = QtGui.QMessageBox()
        msgBox.warning(ui_home.widget, "Alarm", "please select your target device to continue...")
    else:
        global SelectedDevice
        SelectedDevice=ui_home.DeviceList.currentItem().text()
        HomeWindow.close()
        MainWindow.show()

def statueStart():
    ui_main.statusBar.showMessage("Sniffing...")
    sniffing = True
    cap = pcapy.open_live( str(SelectedDevice), 65536 , 1 , 0)
    for i in range(10):
        time.sleep(0.2)
        (header, packet) = cap.next()
        t = threading.Thread(target=parse_packet, args = (packet,))
        t.daemon = True
        t.start()
        #t.join()
        #parse_packet(packet)
    

def eth_addr (a) :
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
    return b

def parse_packet(packet) :
    eth_length = 14
    global Row
    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH' , eth_header)
    eth_protocol = socket.ntohs(eth[2])
    #rowPosition = ui_main.PacketTable.rowCount()
    #ui_main.PacketTable.insertRow(rowPosition)
    #ui_main.PacketTable.setItem(rowPosition,0,QtGui.QTableWidgetItem(str(eth_protocol)))
    #ui_main.PacketTable.setItem(rowPosition , 1, QtGui.QTableWidgetItem(eth_addr(packet[0:6])))
    #ui_main.PacketTable.setItem(rowPosition , 2, QtGui.QTableWidgetItem(eth_addr(packet[6:12])))
    item_0 = QtGui.QTreeWidgetItem(ui_main.PacketTable)
    ui_main.PacketTable.topLevelItem(Row).setText(0, _translate("MainWindow", str(eth_protocol), None))
    ui_main.PacketTable.topLevelItem(Row).setText(1, _translate("MainWindow", eth_addr(packet[0:6]), None))
    ui_main.PacketTable.topLevelItem(Row).setText(2, _translate("MainWindow", eth_addr(packet[6:12]), None))
    Row+=1
    #self.PacketTable.topLevelItem(rowPosition).setText(3, _translate("MainWindow", "field3", None))
    #elf.PacketTable.topLevelItem(rowPosition).setText(4, _translate("MainWindow", "field4", None))

    #ui_main.PacketTable.setItem(rowPosition , 3, QtGui.QTableWidgetItem(eth_protocol))
    #sys.exit(1)




    
def statueStop():
    sniffing = False
    ui_main.statusBar.showMessage("Sniffing has been stopped.")
    
def FilterFn():
    global Row
    word=ui_main.FilterText.toPlainText()
    try:

        for i in range(Row):
            test=ui_main.PacketTable.topLevelItem(i)
            if (word!=test.text(0) and word!=test.text(1) and word!=test.text(2) and word!=test.text(3) and word!=test.text(4)  ):
                ui_main.PacketTable.takeTopLevelItem(i)
                Row-=1
                i=-1
    except:
        FilterFn()
    #msgBox.warning(ui_home.widget, "Alarm", word)


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
ui_main.FilterBtn.clicked.connect(FilterFn)
HomeWindow.show()
sys.exit(app.exec_())