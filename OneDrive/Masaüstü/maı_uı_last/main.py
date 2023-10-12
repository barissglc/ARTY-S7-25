from topbar import TopBar
from toolbar import ToolBar
from camera import Camera
from detection import Detection

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.topbar = TopBar()
        self.toolbar = ToolBar()
        self.camera = Camera()
        self.detection = Detection()

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)

        splitter_h = QSplitter(Qt.Horizontal)
        splitter_h.addWidget(self.camera)
        splitter_h.addWidget(self.detection)
        splitter_h.setHandleWidth(10)
        splitter_h.setStretchFactor(0, 1)

        v_box = QVBoxLayout()
        v_box.addWidget(self.topbar)
        v_box.addWidget(line)
        v_box.addWidget(self.toolbar)
        v_box.addWidget(splitter_h, 1)

        centralWidget = QWidget()
        centralWidget.setContentsMargins(0, 0, 0, 0)
        centralWidget.setLayout(v_box)
        self.setCentralWidget(centralWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
