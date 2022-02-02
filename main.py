import sys
from random import randint

from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class YellowCircles(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Git и желтые окружности')
        self.btn.clicked.connect(self.draw)
        self.flag = False

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.painter = QPainter()
            self.painter.begin(self)
            self.painter.setBrush(QColor(255, 255, 0))
            r = randint(20, self.width() // 4)
            x, y = randint(r, self.width() - r), randint(r, self.height() - r)
            self.painter.drawEllipse(x - r // 2, y - r // 2, r, r)
            self.flag = False
            self.painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())
