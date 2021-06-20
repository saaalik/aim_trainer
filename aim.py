from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys
import random
from PyQt5 import QtWidgets, QtGui, QtCore
from random import randrange

added=True
xpos,ypos = 0,0


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Drawing Rectangle"
        self.top = 100
        self.left = 100
        self.width = 1000
        self.height = 500
        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setAutoFillBackground(True)
        self.setGeometry(self.top, self.left, self.width, self.height)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)
        self.show()


    def paintEvent(self, e):
        global xpos, ypos, w
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 0, Qt.SolidLine))
        #painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))

        top = random.randint(0,420)
        left = random.randint(0,920)
        side = random.choice([30,40,50,60,70,80])
        width = side #680
        height = side #500
        xpos,ypos = left, top
        w = side
        #print("Position -",left,top)
        #print("Size -",width)
        painter.drawRect(left, top, width, height)

class AimTrainer(QtWidgets.QWidget):
    def __init__(self, ):
        super().__init__()
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.yellow)
        self.setPalette(p)
        
        self.count=10
        self.timeUp = False

        # CANVAS WINDOW
        self.canvas = Window()

        # COMMAND BOX
        self.commandbox = QtWidgets.QWidget()
        try:
            self.score
        except:
            self.initializeScore()
        self.ScoreLabel = QtWidgets.QLabel(self.commandbox)
        self.ScoreLabel.setGeometry(QtCore.QRect(20, 110, 251, 81))
        self.ScoreLabel.setStyleSheet("font-size: 40px;\n"
"font-family:\"Times New Roman\";")
        self.ScoreLabel.setObjectName("ScoreLabel")
        
        self.TimerLabel = QtWidgets.QLabel(self.commandbox)
        self.TimerLabel.setGeometry(QtCore.QRect(20, 30, 251, 81))
        self.TimerLabel.setStyleSheet("font-size: 40px;\n"
"background-color: red;\n"
"color: white;\n"
"font-family:\"Times New Roman\";")
        self.TimerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TimerLabel.setObjectName("TimerLabel")

        self.InstrLabel = QtWidgets.QLabel(self.commandbox)
        self.InstrLabel.setGeometry(QtCore.QRect(310, 110, 361, 81))
        self.InstrLabel.setStyleSheet("font-size: 30px;\n"
"font-family:\"Times New Roman\";")
        self.InstrLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.InstrLabel.setText("Click on the red boxes")
        self.InstrLabel.setObjectName("InstrLabel")
        self.RestartButton = QtWidgets.QPushButton(self.commandbox)
        self.RestartButton.setGeometry(QtCore.QRect(810, 30, 171, 71))
        self.RestartButton.setStyleSheet("background-color: #000;\n"
"color:#fff;\n"
"font-size: 17px;")
        self.RestartButton.setText("Restart")
        self.RestartButton.setObjectName("RestartButton")
        self.QuitButton = QtWidgets.QPushButton(self.commandbox)
        self.QuitButton.setGeometry(QtCore.QRect(810, 120, 171, 61))
        self.QuitButton.setStyleSheet("background-color: #000;\n"
"color:#fff;\n"
"font-size: 17px;")
        self.QuitButton.setText("Quit")
        self.QuitButton.setObjectName("QuitButton")   
        self.GameOverLabel = QtWidgets.QLabel(self.commandbox)
        self.GameOverLabel.setGeometry(QtCore.QRect(320, 30, 361, 81))
        self.GameOverLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GameOverLabel.setObjectName("GameOverLabel")

        self.RestartButton.clicked.connect(self.initializeScore)
        self.QuitButton.clicked.connect(self.exit)

        self.timer = QtCore.QTimer(self.commandbox)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        # QtCore.QTimer.singleShot(1000, lambda: self.exit())

        
        # DISPLAY ON SCREEN
        self.layout = QtWidgets.QVBoxLayout(self)
        # RATIO - 70:30
        self.layout.addWidget(self.canvas,71)
        self.layout.addWidget(self.commandbox,29)
        self.resize(1000,700)

    def showTime(self):
        # incrementing the counter
        if self.count > 0:
            self.count -= 1
        # timer is completed
        if self.count == 0 or self.score == 0:
            self.TimerLabel.setText("0 s")
            self.timeUp = True
        else:
            text = str(self.count) + " s"
            self.timeUp = False
            # showing text
            self.TimerLabel.setText(text)
        self.retranslateUi(self.commandbox)

    def exit(self):
        sys.exit()
        
    def retranslateUi(self, inputscale):
        _translate = QtCore.QCoreApplication.translate
        inputscale.setWindowTitle(_translate("commandbox", "MainWindow"))
        self.ScoreLabel.setText(_translate("commandbox", "Score: {}".format(self.score)))
        if self.score==0 or self.timeUp:
            self.GameOverLabel.setText(_translate("commandbox", "GAME OVER"))
            self.GameOverLabel.setStyleSheet(_translate("commandbox", "font-size: 50px;\n"
"color:red;\n"
"border: 2px solid red;\n"
"font-family:\"Times New Roman\";"))
        else:
            self.GameOverLabel.setText(_translate("commandbox", ""))
            self.GameOverLabel.setStyleSheet(_translate("commandbox", "font-size: 50px;\n"
"color:red;\n"))

    def initializeScore(self):
        self.timeup = False
        self.count = 10
        self.score = 10
        try:
            self.retranslateUi(self.commandbox)
        except:
            pass
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.timeUp==False:
            self.current = event.pos()
            #print("MOUSE POSITION - ",self.current)
            if self.current.x()>xpos+10 and self.current.y()>ypos+10 and self.current.x()<xpos+20+w and self.current.y()<ypos+20+w:
                self.add_rectangle()
                self.score+=2
                #print("INSIDE BOX")
            else:
                if self.score-2>0:
                    self.score-=2
                else:
                    self.score = 0

                #print("OUTSIDE")
            self.retranslateUi(self.commandbox)
            

    def add_rectangle(self):
        global added
        if added:
            self.resize(1000,700)
            added=False
        else:
            self.resize(1000,701)
            added=True





def Start():
    app = QApplication(sys.argv)
    window = AimTrainer()
    window.show()
    app.exec()

Start()