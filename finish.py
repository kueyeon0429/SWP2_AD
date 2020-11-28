import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QDialog
from PyQt5.QtCore import Qt, QCoreApplication

class Finish_Win(QDialog):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('거지가 되었습니다ㅠㅠ', self)
        label1.setAlignment(Qt.AlignCenter)

        font1 = label1.font()
        font1.setPointSize(35)

        font1.setFamily('Times New Roman')
        font1.setBold(True)

        label1.setFont(font1)


        layout = QVBoxLayout()
        layout.addWidget(label1)

        self.setLayout(layout)

        btn = QPushButton('Close', self)
        btn.setStyleSheet('color:white; background:black')
        btn.resize(150, 70)
        btn.move(450, 450)
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Rock-Paper-Scissors Game')
        self.resize(600, 550)
        self.show()


    def outputFinishWindow(self):
        return super().exec_()


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = Finish_Win()
    sys.exit(app.exec_())