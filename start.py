import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QCoreApplication

from main import RPSGame


class Start(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('start', self)
        btn.setStyleSheet('color:green; background:yellow')
        btn.clicked.connect(self.startButtonClicked)
        btn.resize(300, 50)
        btn.move(150, 400)

        self.resize(600, 550)
        self.setWindowTitle("Rock-Paper-Scissors Game")
        self.show()

    def startButtonClicked(self):
        self.close()
        self.mainWindow = RPSGame()
        self.mainWindow.outputMainWindow()

        #  연결 된 창 띄우기

    def outputStartWindow(self):
        return super().exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = Start()
    start.show()
    app.exec()