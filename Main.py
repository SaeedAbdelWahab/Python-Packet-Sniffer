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
                s += "  "
        s += " "
        s += sane_color(x[i:i+16])
        i += 16
        s += "\n"
    # remove trailing \n
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
        (header,packet) = cap.next()
        param = parse_packet(packet)
        return param

    def run(self) :
           for i in range(1000) :
                param = self._get_top_packet()
                if param : 
                    data = param[-1]
                    x = hexadump(data,True)
                    if x :
                        print x
                        param = param[0:-1]
                    params_str = ' '.join(param)
                    self.emit(SIGNAL('add_packet(QString)'),params_str)
                



                
Row = 0

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
        get_thread.start()


def statueStart(packet=None):
    global Row
    print packet
    ui_main.statusBar.showMessage("Sniffing...")
    sniffing = True
    item_0 = QtGui.QTreeWidgetItem(ui_main.PacketTable)
    ui_main.PacketTable.topLevelItem(Row).setText(0, _translate("MainWindow", str(packet), None))
    Row+=1
    

def statueStarts(packet=None):
    
    ui_main.statusBar.showMessage("Sniffing...")
    sniffing = True
    


       
    

def eth_addr (a) :
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
    return b

def parse_packet(packet) :
    param = []
    eth_length = 14
    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH' , eth_header)
    eth_protocol = socket.ntohs(eth[2])

    if eth_protocol == 8 : #IPV4 

        param.append(str(eth_protocol)) # no of the protocol of ethernet
        param.append(eth_addr(packet[0:6])) # Destination MAC
        param.append(eth_addr(packet[6:12])) #Source MAC

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
        param.append(str(s_addr)) #source IP
        param.append(str(d_addr)) #destination IP

        if protocol == 6 : #TCP Protocol

            param.append("TCP") #TCP Protocol

            t = iph_length + eth_length #keep parsing the packet
            tcp_header = packet[t:t+20] #the TCP Header
            tcph = unpack('!HHLLBBHHH' , tcp_header) #unpack it
            source_port = tcph[0] #source Port
            dest_port = tcph[1] #Destination Port
            sequence = tcph[2] #seq
            acknowledgement = tcph[3] #Ack
            doff_reserved = tcph[4]
            tcph_length = doff_reserved >> 4  #TCP Length

            param.append(str(source_port)) #source port
            param.append(str(dest_port)) #destination port
            param.append(str(sequence)) #sequence number
            param.append(str(acknowledgement)) #acknowledgment
            param.append(str(tcph_length))
            h_size = eth_length + iph_length + tcph_length * 4 #header length
            data_size = len(packet) - h_size
            data = packet[h_size:]
            if (dest_port == 80 or source_port == 80) :
                param.append("Http")
            param.append(data)

            return param

        elif protocol == 1 : #ICMP 

            param.append("ICMP")
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

            param.append(data) 

            return param 

        elif protocol == 17 : #UDP 

            param.append("UDP")

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
            param.append(data) 

            return param




    
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

cap = pcapy.open_live( "wlp8s0", 65536 , 1 , 0)
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
ui_main.StartButton.clicked.connect(statueStarts)
ui_main.StopSniffing.clicked.connect(statueStop)
ui_main.FilterBtn.clicked.connect(FilterFn)
HomeWindow.show()

get_thread = getPacketsThread(cap)
MainWindow.connect(get_thread,SIGNAL("add_packet(QString)"),statueStart)




sys.exit(app.exec_())