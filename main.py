import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.flag = False

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()

    def drawing(self, qp):
        x = randint(1, 200)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(randint(0, 800), randint(0, 600), x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.D_x, self.D_y = -1, -1
        self.x, self.y = -1, -1
        self.GOG = None

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawing(qp)
        qp.end()

    def drawing(self, qp):
        leigt = randint(20, 100)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        if self.x > -1 and self.y > -1 and self.GOG == 1:
            qp.setBrush(QColor(r, g, b))

            qp.drawRect(self.x - leigt // 2, self.y - leigt // 2, leigt, leigt)

        elif self.x > -1 and self.y > -1 and self.GOG == -1:
            qp.setBrush(QColor(r, g, b))

            qp.drawEllipse(self.x - leigt // 2, self.y - leigt // 2, leigt,
                           leigt)

        elif self.D_x > -1 and self.D_y > -1 and self.GOG == 2:
            qp.setBrush(QColor(r, g, b))

            points = QPolygon(
                [QPoint(int(self.D_x + leigt * 0.75), int(self.D_y + leigt * 0.5)),
                 # Правая
                 QPoint(int(self.D_x), int(self.D_y - leigt)),  # Верхушка
                 QPoint(int(self.D_x - leigt * 0.75),
                        int(self.D_y + leigt * 0.5))])  # Левая
            qp.drawPolygon(points)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Suprematism()
    ex.show()
    exit(app.exec())
