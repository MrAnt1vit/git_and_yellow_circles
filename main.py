import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import QtCore


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(735, 761)
        self.btn = QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(50, 50, 85, 26))
        self.btn.setObjectName("btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn.setText(_translate("Form", "Circle"))


class YellowCircles(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            self.painter.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
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
