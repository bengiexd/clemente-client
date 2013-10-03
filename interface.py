from PyQt4 import QtCore, QtGui
from cliente import Cliente
import sys

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

class Ui_Form(object):
    ip = "10.42.0.82"
    puerto = 9000
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(330, 426)
        self.btnTop = QtGui.QPushButton(Form)
        self.btnTop.setGeometry(QtCore.QRect(130, 30, 71, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.btnTop.setPalette(palette)
        self.btnTop.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/arriba-icono-9739-64.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnTop.setIcon(icon)
        self.btnTop.setIconSize(QtCore.QSize(100, 100))
        self.btnTop.setObjectName(_fromUtf8("btnTop"))
        self.btnLeft = QtGui.QPushButton(Form)
        self.btnLeft.setGeometry(QtCore.QRect(40, 120, 71, 71))
        self.btnLeft.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/izquierdo-icono-4692-64.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnLeft.setIcon(icon1)
        self.btnLeft.setIconSize(QtCore.QSize(100, 100))
        self.btnLeft.setObjectName(_fromUtf8("btnLeft"))
        self.btnRight = QtGui.QPushButton(Form)
        self.btnRight.setGeometry(QtCore.QRect(220, 120, 71, 71))
        self.btnRight.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/derecho-icono-4865-64.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnRight.setIcon(icon2)
        self.btnRight.setIconSize(QtCore.QSize(100, 100))
        self.btnRight.setObjectName(_fromUtf8("btnRight"))
        self.btnDown = QtGui.QPushButton(Form)
        self.btnDown.setGeometry(QtCore.QRect(130, 210, 71, 71))
        self.btnDown.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/a-los-bajos-icono-5369-64.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnDown.setIcon(icon3)
        self.btnDown.setIconSize(QtCore.QSize(100, 100))
        self.btnDown.setObjectName(_fromUtf8("btnDown"))
        self.btnStop = QtGui.QPushButton(Form)
        self.btnStop.setGeometry(QtCore.QRect(130, 120, 71, 71))
        self.btnStop.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/bloque-icono-9427-64.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnStop.setIcon(icon4)
        self.btnStop.setIconSize(QtCore.QSize(50, 50))
        self.btnStop.setObjectName(_fromUtf8("btnStop"))
        self.btnConnect = QtGui.QPushButton(Form)
        self.btnConnect.setGeometry(QtCore.QRect(0, 390, 71, 31))
        self.btnConnect.setObjectName(_fromUtf8("btnConnect"))
        self.graphicsView = QtGui.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 81, 81))
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setInteractive(True)
        self.graphicsView.setDragMode(QtGui.QGraphicsView.NoDrag)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.btnDisconnect = QtGui.QPushButton(Form)
        self.btnDisconnect.setGeometry(QtCore.QRect(90, 390, 81, 31))
        self.btnDisconnect.setObjectName(_fromUtf8("btnDisconnect"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 310, 41, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.txtMessage = QtGui.QLineEdit(Form)
        self.txtMessage.setGeometry(QtCore.QRect(40, 310, 281, 23))
        self.txtMessage.setObjectName(_fromUtf8("txtMessage"))
        self.btnSend = QtGui.QPushButton(Form)
        self.btnSend.setGeometry(QtCore.QRect(40, 340, 90, 27))
        self.btnSend.setObjectName(_fromUtf8("btnSend"))
        self.btnClear = QtGui.QPushButton(Form)
        self.btnClear.setGeometry(QtCore.QRect(230, 340, 90, 27))
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.graphicsView_2 = QtGui.QGraphicsView(Form)
        self.graphicsView_2.setGeometry(QtCore.QRect(230, 20, 81, 81))
        self.graphicsView_2.setAutoFillBackground(True)
        self.graphicsView_2.setInteractive(True)
        self.graphicsView_2.setDragMode(QtGui.QGraphicsView.NoDrag)
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.lblMsg = QtGui.QLabel(Form)
        self.lblMsg.setGeometry(QtCore.QRect(210, 400, 81, 16))
        self.lblMsg.setObjectName(_fromUtf8("lblMsg"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 260, 62, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txtAngulo = QtGui.QLineEdit(Form)
        self.txtAngulo.setGeometry(QtCore.QRect(270, 280, 51, 23))
        self.txtAngulo.setObjectName(_fromUtf8("txtAngulo"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btnConnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.btnConnect.click)
        QtCore.QObject.connect(self.btnTop, QtCore.SIGNAL(_fromUtf8("clicked()")), self.btnTop.click)
        QtCore.QObject.connect(self.btnLeft, QtCore.SIGNAL(_fromUtf8("clicked()")), self.btnLeft.click)
        QtCore.QObject.connect(self.btnStop, QtCore.SIGNAL(_fromUtf8("clicked()")), self.btnStop.click)
        QtCore.QObject.connect(self.btnRight, QtCore.SIGNAL(_fromUtf8("clicked()")), self.btnRight.click)
        QtCore.QObject.connect(self.btnDown, QtCore.SIGNAL(_fromUtf8("clicked()")), self.btnDown.click)
        QtCore.QObject.connect(self.btnSend, QtCore.SIGNAL(_fromUtf8("clicked()")), self.btnSend.click)
        QtCore.QObject.connect(self.btnClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.txtMessage.clear)
        QtCore.QObject.connect(self.btnDisconnect, QtCore.SIGNAL(_fromUtf8("clicked()")), self.btnDisconnect.click)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Clemente-Cliente", None))
        self.btnConnect.setText(_translate("Form", "Connect", None))
        self.btnDisconnect.setText(_translate("Form", "Disconnect", None))
        self.label.setText(_translate("Form", "Data:", None))
        self.btnSend.setText(_translate("Form", "Send", None))
        self.btnClear.setText(_translate("Form", "Clear", None))
        self.lblMsg.setText(_translate("Form", "Disconnect...", None))
        self.label_2.setText(_translate("Form", "Angulo", None))

    def Disconnect(self):    
        self.cliente.Stop() 
        self.lblMsg.setText("Desconectado...")  
        return 0         
            
    def Connect(self):
        self.cliente = Cliente(self.ip, self.puerto)
        self.cliente.start()
        self.lblMsg.setText("Conectado...")    
        return 0 
                
    def Top(self):
        temp = self.cliente.Send("ADELANTE") 
        self.txtMessage.setText(temp)          

    def Down(self):
        temp = self.cliente.Send("ATRAS") 
        self.txtMessage.setText(temp)
               

    def Left(self):
        temp = self.cliente.Send("DERECHA") 
        self.txtMessage.setText(temp)             

    def Right(self):
        stemp = self.cliente.Send("IZQUIERDA") 
        self.txtMessage.setText(temp)        

    def SendData(self):
        self.txtMessage.setText(self.cliente.Send(self.txtMessage.text()))         
        #tem = self.cliente.Send()   
        #self.txtMessage.setText(tem)  

    def Recived(self):
        pass        
        

class Controller:
    def __init__(self,ip,puerto):
        app = QtGui.QApplication(sys.argv)
        Form = QtGui.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)

        ui.ip = ip
        ui.puerto = puerto
        
        Form.show()
        sys.exit(app.exec_())      


