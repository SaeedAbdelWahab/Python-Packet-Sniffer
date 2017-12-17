from pcapy import findalldevs
import os,sys,pcapy
from Windows.homewin import Ui_HomeWindow
from Windows.MainWindow import Ui_MainWindow
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread,SIGNAL
from scapy.all import *
import socket
from struct import *
import datetime
import pcapy
import sys
import time

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


#global Variables
data = ""
cap=""
times = ""
word = ""  #filter word
Row = 0
sniffing = True
packets= []
dumper = ""
pcap=[]
captureFromFile=False



def hexadump(x, dump=False):
    """ Build a tcpdump like hexadecimal view
    :param x: a Packet
    :param dump: define if the result must be printed or returned in a variable
    :returns: a String only when dump=True
    """
    s = ""
    x = str(x)
    l = len(x)
    i = 0
    while i < l:
        s += "%04x  " % i
        for j in xrange(16):
            if i+j < l:
                s += "%02X " % ord(x[i+j])
            else:
                s += "  "
            if j%16 == 7:
                s += ""
        s += "  "
        s += sane_color(x[i:i+16])
        i += 16
        s += "\n"
    if s.endswith("\n"):
        s = s[:-1]
    if dump:
        return s
    else:
        print(s)

   
class getPacketsThread(QThread) :
    def __init__(self,cap) :
        QThread.__init__(self)
        self.cap = cap

    def __del__(self) :
        self.wait()

    def _get_top_packet(self) :
        global times
        global packets
        (header,packet) = cap.next()
        pcap.append((header,packet))
        times = datetime.datetime.now().time()
        param = parse_packet(packet)
        return param

    def run(self) :
        global sniffing
        global data
        while (sniffing) :
            param = self._get_top_packet()
            if param : 
                data = param[-1]
                data = hexadump(data,True)
                param = param [0:-1]
                param.append(data)
                packets.append(param)
                param = param [0:-1]
                params_str = ' '.join(param)
                self.emit(SIGNAL('add_packet(QString)'),params_str)
                time.sleep(0.1)
                

def selectTrigger():
    if(ui_home.DeviceList.currentRow()==-1):
        msgBox = QtGui.QMessageBox()
        msgBox.warning(ui_home.widget, "Alarm", "please select your target device to continue...")
    else:
        global SelectedDevice
        global cap
        SelectedDevice=str(ui_home.DeviceList.currentItem().text())
        HomeWindow.close()
        MainWindow.show()
        cap = pcapy.open_live( SelectedDevice, 65536 , 1 , 0)
        get_thread.start()

def statueStart(packet=""):
    global Row
    global data
    global times
    global word
    ui_main.StartButton.setEnabled(False)
    ui_main.StopSniffing.setEnabled(True)
    packet = str(packet).split()
    #packet.append(data)
    #packets.append(packet)
    ui_main.statusBar.showMessage("Sniffing...")
    if len(packet)>12 : 
            if packet[12] == "Http" :
                protocol = "Http"
    else : 
        protocol = packet[6]

    if (word==packet[4] or word==packet[5] or word==protocol or word==""):
        item_0 = QtGui.QTreeWidgetItem(ui_main.PacketTable)
        ui_main.PacketTable.topLevelItem(Row).setText(0, _translate("MainWindow", str(Row+1), None))
        ui_main.PacketTable.topLevelItem(Row).setText(1, _translate("MainWindow", str(times), None))
        ui_main.PacketTable.topLevelItem(Row).setText(2, _translate("MainWindow", str(packet[4]), None))
        ui_main.PacketTable.topLevelItem(Row).setText(3, _translate("MainWindow", str(packet[5]), None))
        ui_main.PacketTable.topLevelItem(Row).setText(5, _translate("MainWindow", str(packets[Row][0]), None))
        ui_main.PacketTable.topLevelItem(Row).setText(6, _translate("MainWindow", str(packets[Row][7]), None))
        ui_main.PacketTable.topLevelItem(Row).setText(4, _translate("MainWindow", protocol, None))    
        Row+=1
    else:
        None

    # if word!="":
    #     if (word!=packet[4] and word!=packet[5] and word!=protocol ):#and word!=Packet.text(3) and word!=Packet.text(4) and word!=Packet.text(5) and word!=Packet.text(6)  ):
    #         None
    #     else:
    #         item_0 = QtGui.QTreeWidgetItem(ui_main.PacketTable)
    #         ui_main.PacketTable.topLevelItem(Row).setText(0, _translate("MainWindow", str(Row+1), None))
    #         ui_main.PacketTable.topLevelItem(Row).setText(1, _translate("MainWindow", str(times), None))
    #         ui_main.PacketTable.topLevelItem(Row).setText(2, _translate("MainWindow", str(packet[4]), None))
    #         ui_main.PacketTable.topLevelItem(Row).setText(3, _translate("MainWindow", str(packet[5]), None))
    #         ui_main.PacketTable.topLevelItem(Row).setText(5, _translate("MainWindow", str(packets[Row][0]), None))
    #         ui_main.PacketTable.topLevelItem(Row).setText(6, _translate("MainWindow", str(packets[Row][7]), None))
    #         ui_main.PacketTable.topLevelItem(Row).setText(4, _translate("MainWindow", protocol, None))    
    #         Row+=1
    # else:
    #     item_0 = QtGui.QTreeWidgetItem(ui_main.PacketTable)
    #     ui_main.PacketTable.topLevelItem(Row).setText(0, _translate("MainWindow", str(Row+1), None))
    #     ui_main.PacketTable.topLevelItem(Row).setText(1, _translate("MainWindow", str(times), None))
    #     ui_main.PacketTable.topLevelItem(Row).setText(2, _translate("MainWindow", str(packet[4]), None))
    #     ui_main.PacketTable.topLevelItem(Row).setText(3, _translate("MainWindow", str(packet[5]), None))
    #     ui_main.PacketTable.topLevelItem(Row).setText(5, _translate("MainWindow", str(packets[Row][0]), None))
    #     ui_main.PacketTable.topLevelItem(Row).setText(6, _translate("MainWindow", str(packets[Row][7]), None))
    #     ui_main.PacketTable.topLevelItem(Row).setText(4, _translate("MainWindow", protocol, None))    
    #     Row+=1

def statueResume() :
    global sniffing
    if sniffing:
        ui_main.StartButton.setEnabled(False)
        ui_main.StopSniffing.setEnabled(True)    
    sniffing = True 
    get_thread.start()   
    ui_main.statusBar.showMessage("Sniffing...")
       
    

def eth_addr (a) :
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
    return b

def parse_packet(packet) :
    param = []
    length_of_packet = len(packet)
    param.append(str(length_of_packet)) #packet length
    eth_length = 14
    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH' , eth_header)
    eth_protocol = socket.ntohs(eth[2])

    if eth_protocol == 8 : #IPV4 

        param.append(str(eth_protocol)) # no of the protocol of ethernet
        param.append(eth_addr(packet[0:6])) # Destination MAC 2
        param.append(eth_addr(packet[6:12])) #Source MAC 3

        ip_header = packet[eth_length:20+eth_length] #extract the ip header
        iph = unpack('!BBHHHBBH4s4s' , ip_header) #unpack it
        version_ihl = iph[0]
        version = version_ihl >> 4 #get ip header verion
        ihl = version_ihl & 0xF
        iph_length = ihl * 4 #get ip header length
        ttl = iph[5]  #get the TTL
        protocol = iph[6]  #get the number of the protocol
        s_addr = socket.inet_ntoa(iph[8]); #source ip address
        d_addr = socket.inet_ntoa(iph[9]); #destination ip address
        param.append(str(s_addr)) #source IP 4
        param.append(str(d_addr)) #destination IP 5

        if protocol == 6 : #TCP Protocol

            param.append("TCP") #TCP Protocol 6

            t = iph_length + eth_length #keep parsing the packet
            tcp_header = packet[t:t+20] #the TCP Header
            tcph = unpack('!HHLLBBHHH' , tcp_header) #unpack it
            source_port = tcph[0] #source Port
            dest_port = tcph[1] #Destination Port
            sequence = tcph[2] #seq
            acknowledgement = tcph[3] #Ack
            doff_reserved = tcph[4]
            tcph_length = doff_reserved >> 4  #TCP Length

            param.append(str(source_port)) #source port 7
            param.append(str(dest_port)) #destination port    8
            param.append(str(sequence)) #sequence number 9
            param.append(str(acknowledgement)) #acknowledgment  10
            param.append(str(tcph_length))  # 11
            h_size = eth_length + iph_length + tcph_length * 4 #header length
            data_size = len(packet) - h_size
            data = packet[h_size:]
            if (dest_port == 80 or source_port == 80) :
                param.append("Http") #12

            if len(data) > 0 :
                param.append(data) 
            else :
                param.append("no data Found in this packet")
            return param

        elif protocol == 1 : #ICMP 

            param.append("ICMP") #6
            u = iph_length + eth_length
            icmph_length = 4
            icmp_header = packet[u:u+4]
            icmph = unpack('!BBH' , icmp_header)  
            icmp_type = icmph[0]
            code = icmph[1]
            checksum = icmph[2]
             
            param.append(str(icmp_type))
            param.append(str(code))
            param.append(str(checksum))
            param.append(str(icmp_header))
             
            h_size = eth_length + iph_length + icmph_length
            data_size = len(packet) - h_size
            data = packet[h_size:] 

            if len(data)>0 :
                param.append(data) 
            else :
                param.append("no data Found in this packet")

            return param 

        elif protocol == 17 : #UDP 

            param.append("UDP") #6

            u = iph_length + eth_length
            udph_length = 8
            udp_header = packet[u:u+8]
            udph = unpack('!HHHH' , udp_header)         
            source_port = udph[0]
            dest_port = udph[1]
            length = udph[2]
            checksum = udph[3]
            
            param.append(str(source_port)) #source port
            param.append(str(dest_port)) #destination port
            param.append(str(checksum)) #acknowledgment
            param.append(str(length)) 

            h_size = eth_length + iph_length + udph_length
            data_size = len(packet) - h_size
             
            data = packet[h_size:]   

            if len(data) :
                param.append(data) 
            else :
                param.append("no data Found in this packet payload")

            return param

    
def statueStop():
    global sniffing
    sniffing = False
    ui_main.StartButton.setEnabled(True)
    ui_main.StopSniffing.setEnabled(False)
    ui_main.statusBar.showMessage("Sniffing has been stopped.")
    ui_main.StartButton.setText(_translate("MainWindow", "Resume Sniffing", None))
    


def DisplayPacket() : 
    global packets
    SelectedPacket = str(ui_main.PacketTable.currentItem().text(0))
    #print str(packets[int(SelectedPacket)-1][-1])
    ui_main.plainTextEdit.setPlainText(_translate("MainWindow", str(packets[int(SelectedPacket)-1][-1]), None))
    ui_main.PacketTree.clear()
    item_0 = QtGui.QTreeWidgetItem(ui_main.PacketTree)
    ui_main.PacketTree.topLevelItem(0).setText(0, _translate("MainWindow", str("Packet Length : "+str(packets[int(SelectedPacket)-1][0])), None))
    item_0 = QtGui.QTreeWidgetItem(ui_main.PacketTree)
    ui_main.PacketTree.topLevelItem(1).setText(0, _translate("MainWindow", str("Destination MAC : "+str(packets[int(SelectedPacket)-1][2])), None))
    item_0 = QtGui.QTreeWidgetItem(ui_main.PacketTree)
    ui_main.PacketTree.topLevelItem(2).setText(0, _translate("MainWindow", str("Source MAC : "+str(packets[int(SelectedPacket)-1][3])), None))
    item_0 = QtGui.QTreeWidgetItem(ui_main.PacketTree)
    ui_main.PacketTree.topLevelItem(3).setText(0, _translate("MainWindow", str("Source IP : "+str(packets[int(SelectedPacket)-1][4])), None))
    item_0 = QtGui.QTreeWidgetItem(ui_main.PacketTree)
    ui_main.PacketTree.topLevelItem(4).setText(0, _translate("MainWindow", str("Destination IP : "+str(packets[int(SelectedPacket)-1][5])), None))
    item_0 = QtGui.QTreeWidgetItem(ui_main.PacketTree)
    ui_main.PacketTree.topLevelItem(5).setText(0, _translate("MainWindow", str("Protocol : "+str(packets[int(SelectedPacket)-1][6])), None))
    item_0 = QtGui.QTreeWidgetItem(ui_main.PacketTree)
    ui_main.PacketTree.topLevelItem(6).setText(0, _translate("MainWindow", str("Source port : "+str(packets[int(SelectedPacket)-1][7])), None))
    item_0 = QtGui.QTreeWidgetItem(ui_main.PacketTree)
    ui_main.PacketTree.topLevelItem(7).setText(0, _translate("MainWindow", str("Destination port : "+str(packets[int(SelectedPacket)-1][8])), None))
    if str(packets[int(SelectedPacket)-1][6]) == "UDP":
        item_0 = QtGui.QTreeWidgetItem(ui_main.PacketTree)
        ui_main.PacketTree.topLevelItem(8).setText(0, _translate("MainWindow", str("acknowledgment  : "+str(packets[int(SelectedPacket)-1][9])), None))
    else:
        item_0 = QtGui.QTreeWidgetItem(ui_main.PacketTree)
        ui_main.PacketTree.topLevelItem(8).setText(0, _translate("MainWindow", str("sequence no. : "+str(packets[int(SelectedPacket)-1][9])), None))
        item_0 = QtGui.QTreeWidgetItem(ui_main.PacketTree)
        ui_main.PacketTree.topLevelItem(9).setText(0, _translate("MainWindow", str("acknowledgment  : "+str(packets[int(SelectedPacket)-1][10])), None))

    
def FilterFn():
    global Row
    global word
    word=ui_main.FilterText.toPlainText()
    try:
        for i in range(Row):
            test=ui_main.PacketTable.topLevelItem(i)
            if (word!=test.text(0) and word!=test.text(1) and word!=test.text(2) and word!=test.text(3) and word!=test.text(4) and word!=test.text(5) and word!=test.text(6)  ):
                ui_main.PacketTable.takeTopLevelItem(i)
                Row-=1
                i=-1
    except:
        FilterFn()
def Reselect():     #this fn restarts all global vars and clears all containers (trees and txt) to startover live data
                    #usualy is used after finishing work with pcap file and user wants to capture live data again
    global data,cap,times,word,Row,sniffing,packets,captureFromFile
    data = ""
    cap=""
    times = ""
    word = ""  #filter word
    Row = 0
    sniffing = True
    packets= []
    captureFromFile=False
    ui_main.PacketTable.clear()
    ui_main.PacketTree.clear()
    ui_main.plainTextEdit.clear()
    MainWindow.close()
    HomeWindow.show()
    

def OpenFile():     #this fn restarts all global vars and clears all containers (trees and txt) to startover with the pcap file
    global data,cap,times,word,Row,sniffing,packets,captureFromFile
    filename = QtGui.QFileDialog.getOpenFileName(ui_main.centralwidget, "Save file", "", "pcap (*.pcap)")
    if filename!="":

        msg = "This pcap file is going to overwrite the current captured data...continue without saving?"
        reply = QtGui.QMessageBox.question(ui_main.centralwidget, 'overwrite', msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.No:
            None
        else:
            data = ""
            cap=""
            times = ""
            word = ""  #filter word
            Row = 0
            sniffing = True
            packets= []
            captureFromFile=True
            cap = pcapy.open_offline(str(filename))
            ui_main.PacketTable.clear()
            ui_main.PacketTree.clear()
            ui_main.plainTextEdit.clear()
            get_thread.start()

def SaveFile():
    filename = QtGui.QFileDialog.getSaveFileName(ui_main.centralwidget, "Save file", "", "pcap (*.pcap);;All files (*.*)") #opens save file dialog with filter (*.pcap)
    if str(filename)[-5:]!=".pcap":             #check if user forgot to type the extention and correct that
        filename=str(filename)+".pcap"
    else:
        filename=str(filename)
    dumper = cap.dump_open(filename)
    for item in pcap:
        (hdr,pkt)=item
        dumper.dump(hdr, pkt)



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
ui_main.PacketTable.header().setResizeMode(QtGui.QHeaderView.ResizeToContents)
#ui_main.PacketTable.header().setStretchLastSection(False)
QtCore.QObject.connect(ui_main.actionSave, QtCore.SIGNAL(("triggered()")), SaveFile)  #save file trigger (check SaveFile fn)
QtCore.QObject.connect(ui_main.actionOpen, QtCore.SIGNAL(("triggered()")), OpenFile)  #open file trigger (check OpenFile fn)
QtCore.QObject.connect(ui_main.Reselect, QtCore.SIGNAL(("clicked()")), Reselect)      #Reselect device btn trigger
ui_main.StartButton.clicked.connect(statueResume)
ui_main.StopSniffing.clicked.connect(statueStop)
ui_main.FilterBtn.clicked.connect(FilterFn)          #filter btn trigger
ui_main.DisplayButton.clicked.connect(DisplayPacket) #display btn have been hidden but still used as signals are sent to id (please don't delete :'D) 
HomeWindow.show()

get_thread = getPacketsThread(cap)
MainWindow.connect(get_thread,SIGNAL("add_packet(QString)"),statueStart)


sys.exit(app.exec_())