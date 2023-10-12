from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import cv2
import time
import numpy as np

class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    change_fps_signal = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self._run_flag = True
        self.fps = 0
        self.start_time = time.time()

    def run(self):
        cap = cv2.VideoCapture(0)
        while self._run_flag:
            ret, cv_img = cap.read()
            if ret:
                self.change_pixmap_signal.emit(cv_img)
                self.fps += 1
            elapsed_time = time.time() - self.start_time
            if elapsed_time >= 1.0:
                self.start_time = time.time()
                self.change_fps_signal.emit(self.fps)
                self.fps = 0
        cap.release()

    def stop(self):
        self._run_flag = False
        self.wait()

class Camera(QMainWindow):
    def __init__(self):
        super().__init__()
        self.display_width, self.display_height = 640, 480
        self.initUI()

    def initUI(self):
        self.camera_label = QLabel(self)
        self.camera_label.resize(self.display_width, self.display_height)
        self.camera_label.setAlignment(Qt.AlignCenter)

        self.fps_label = QLabel("FPS: 0", self)
        self.fps_label.move(10, 10)
        self.fps_label.setStyleSheet("color: white; background-color: rgba(0, 0, 0, 100); padding: 5px;")

        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.change_fps_signal.connect(self.update_fps)
        self.thread.start()

        self.setCentralWidget(self.camera_label)

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.camera_label.setPixmap(qt_img)

    @pyqtSlot(int)
    def update_fps(self, fps):
        self.fps_label.setText(f"FPS: {fps}")

    def resizeEvent(self, a0: QResizeEvent) -> None:
        self.display_width = self.camera_label.width()
        self.display_height = self.camera_label.height()

    def convert_cv_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(
            rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        p = QPixmap.fromImage(convert_to_Qt_format).scaled(
            self.display_width, self.display_height, Qt.AspectRatioMode.KeepAspectRatio)
        return p

if __name__ == "__main__":
    app = QApplication(sys.argv)
    camera = Camera()
    camera.show()
    sys.exit(app.exec())
