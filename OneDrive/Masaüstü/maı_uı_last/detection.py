from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


class Detection(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("background-color: #d9d9d9;")
        self.image_label.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)

        analiz_goruntu_yenile_button = QPushButton("Analiz Görüntü Yenile")

        image_v_box = QVBoxLayout()
        image_v_box.addWidget(self.image_label)
        image_v_box.addWidget(analiz_goruntu_yenile_button,
                              alignment=Qt.AlignCenter)
        image_widget = QWidget()
        image_widget.setLayout(image_v_box)

        log_v_box = QVBoxLayout()
        log_v_box.addWidget(QLabel("LOG:"), alignment=Qt.AlignBottom)
        log_widget = QWidget()
        log_widget.setLayout(log_v_box)

        info_v_box = QVBoxLayout()
        info_v_box.addWidget(QLabel("INFO:"), alignment=Qt.AlignBottom)
        info_widget = QWidget()
        info_widget.setLayout(info_v_box)

        splitter_v = QSplitter(Qt.Vertical)
        splitter_v.addWidget(image_widget)
        splitter_v.addWidget(log_widget)
        splitter_v.addWidget(info_widget)
        splitter_v.setHandleWidth(10)

        central_layout = QHBoxLayout()
        central_layout.addWidget(splitter_v)
        self.setLayout(central_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    detection = Detection()
    detection.show()
    sys.exit(app.exec())
