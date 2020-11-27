from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 50)
        size.setWidth(max(size.width(), size.height()))
        return size

class RPSGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Rock-Paper-Scissors Layout creation
        rpsLayout = QGridLayout()

        # Balance display window
        self.balanceWindow = QLineEdit()
        self.balanceWindow.setReadOnly(True)
        self.balanceWindow.setAlignment(Qt.AlignCenter)
        rpsLayout.addWidget(self.balanceWindow, 0, 1, 1, 2)

        self.balanceLabel = QLabel()
        self.balanceLabel.setText('                잔액:')
        rpsLayout.addWidget(self.balanceLabel, 0, 0, 1, 1)

        # Result display window
        self.resultWindow = QTextEdit()  # 결과를 출력하는 페이지, 추후 이미지를 넣을지 글자만 넣을지 결정
        self.resultWindow.setReadOnly(True)  # 연결을 읽기 전용으로 함
        self.resultWindow.setAlignment(Qt.AlignCenter)
        rpsLayout.addWidget(self.resultWindow, 1, 0, 1, 3)

        # Rock Button
        self.rockButton = Button('바위', self.rockButtonClicked)  #  추후 이미지로 설정
        rpsLayout.addWidget(self.rockButton, 2, 1, 1, 1)

        # Paper Button
        self.paperButton = Button('보', self.paperButtonClicked)
        rpsLayout.addWidget(self.paperButton, 2, 2, 1, 1)

        # Scissors Button
        self.scissorsButton = Button('가위', self.scissorsButtonClicked)
        rpsLayout.addWidget(self.scissorsButton, 2, 0, 1, 1)

        # Button for check the result
        self.checkResultButton = Button('결과 확인하기', self.checkResultButtonClicked)
        self.checkResultButton.setMaximumHeight(30)  #  세로 길이 수정
        rpsLayout.addWidget(self.checkResultButton, 3, 0, 1, 3)

        # window output
        rpsLayout.setSizeConstraint(QLayout.SetFixedSize)  # 사이즈 고정
        self.setLayout(rpsLayout)
        self.setWindowTitle("Rock-Paper-Scissors Game")

    def rockButtonClicked(self):
        return 0

    def paperButtonClicked(self):
        return 0

    def scissorsButtonClicked(self):
        return 0

    def checkResultButtonClicked(self):
        return 0






if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    main = RPSGame()
    main.show()
    sys.exit(app.exec_())