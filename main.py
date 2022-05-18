from cProfile import label
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QVBoxLayout,QGridLayout, QFrame
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
from os import environ
#from stylesheet import  stylesheet
from qt_material import apply_stylesheet

from win32api import GetSystemMetrics

WIDTH= GetSystemMetrics(0)
HEIGHT= GetSystemMetrics(1)


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

def dialog():
    mbox = QMessageBox()

    mbox.setText("Your allegiance has been noted")
    mbox.setDetailedText("You are now a disciple and subject of the all-knowing Guru")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            
    mbox.exec_()

def startProgram():
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_amber.xml',invert_secondary=True)
    
    appWindow = QWidget()
    appWindow.resize(WIDTH,HEIGHT)
    appWindow.setWindowTitle("ThinkWild ToDo")
    appWindow.setStyleSheet("QLabel{color: rgb(229, 233, 240)}")
    #appWindow.setStyleSheet("border-image: url(bg.jpg) 0 0 0 0 stretch stretch; background-attachment: fixed;background-repeat: no-repeat;  background-position: center;")
    bgf=QFrame(appWindow,objectName='bgfObj')
    bgf.move(0,0)
    bgf.resize(WIDTH,HEIGHT)
    #bgf.setStyleSheet("background-color:rgb(255, 255, 255)")
    bgf.show()

    sidebarFrame=QFrame(appWindow,objectName='sideBarObj')
    sidebarFrame.move(1,1)
    sidebarFrame.resize(250,HEIGHT)
    #sidebarFrame.setStyleSheet("background-color:rgb(243, 243, 243);border-width: 1;border-style: solid;border-color: rgb(10, 10, 10)")
    sidebarFrame.show()
    

    
    
    frame=QFrame(appWindow,objectName='contentFrameObj')
    #frame.setStyleSheet("background-color:rgb(243, 243, 243)")
    frame.resize(WIDTH-250,HEIGHT)
    frame.move(250,0)

    #frame.setStyleSheet("border-image: url(bg.jpg) 0 0 0 0 stretch stretch;  background-attachment: fixed;background-repeat: no-repeat;  background-position: center;")
    #vbox = QVBoxLayout(frame)
    #layout = QGridLayout()
    
    for i in range(5):
        
        tmpLabel = QLabel(frame)
        tmpLabel.setText('hello'+str(i))
        tmpLabel.setFixedHeight(40)
        tmpLabel.setFixedWidth(500)
        tmpLabel.setStyleSheet("padding :10px")
        tmpLabel.setAlignment(QtCore.Qt.AlignLeft)
        tmpLabel.move(50,50+i*60)
        

    #appWindow.setLayout(vbox)
    #vbox.setSpacing(0)
    button = QPushButton('PyQt5 button', frame)
    button.setToolTip('This is an example button')
    button.move(frame.frameGeometry().width()-200,frame.frameGeometry().height()-200)
    appWindow.show()
    sys.exit(app.exec_())
  



if __name__ == "__main__":
    suppress_qt_warnings()
    startProgram()