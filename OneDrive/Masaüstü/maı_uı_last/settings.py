import sys
from PyQt5.QtWidgets import *

class PencereAyarlari(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ayarlar")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.resolution_label = QLabel("Çözünürlük:")
        self.resolution_combobox = QComboBox()
        self.resolution_combobox.addItems(["1920x1080", "1280x720", "1024x768", "800x600"])

        save_button = QPushButton("Kaydet")
        save_button.clicked.connect(self.ayar_kaydet)

        
        layout.addWidget(self.resolution_label)
        layout.addWidget(self.resolution_combobox)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def ayar_kaydet(self):
        selected_resolution = self.resolution_combobox.currentText()
        
        print(f"Seçilen Çözünürlük: {selected_resolution}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    settings_window = PencereAyarlari()
    settings_window.show()
    sys.exit(app.exec_())
