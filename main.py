from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout
from PyQt5.QtGui import QPixmap, QPainter, QPen

import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.drawing = False
        self.firstPoint = QPoint()
        self.lastPoint = QPoint()
        self.image = QPixmap("data.jpeg")
        self.pix = QPixmap(self.rect().size())
        self.pix.fill(Qt.white)
        self.resize(self.image.width(), self.image.height())
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(QPoint(), self.image)

        if not self.firstPoint.isNull() and not self.lastPoint.isNull():
            rect = QRect(self.firstPoint, self.lastPoint)
            painter.setPen(QPen(Qt.green, 2))
            painter.drawRect(rect.normalized())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.firstPoint = event.pos()
            self.lastPoint = self.firstPoint
            self.update()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:

            rect = QRect(self.firstPoint, self.lastPoint)
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.red, 2))
            painter.drawRect(rect.normalized())
            self.firstPoint, self.lastPoint = QPoint(),QPoint()
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Datable")

    window = MainWindow()
    app.exec_()