from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

class ToolBar(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lineEdit = QLineEdit()

        self.dateEdit = QDateEdit()
        self.dateEdit.setDate(QDate.currentDate())

        self.kayit_dosya_yolu_belirle_button = QPushButton("KAYIT DOSYA YOLU BELİRLE")
        self.kayit_dosya_yolu_belirle_button.setIcon(QIcon("images/kayit_dosya_yolu_belirle.png"))
        self.kayit_dosya_yolu_belirle_button.clicked.connect(self.open_file_dialog)

        self.path_label = QLabel(QDir.currentPath())

        self.combo_box = QComboBox()
        self.combo_box.addItem("Deney Seçiniz")

        hbox = QHBoxLayout()
        hbox.addWidget(self.lineEdit)
        hbox.addStretch()
        hbox.addWidget(QLabel("TARİH:"))
        hbox.addWidget(self.dateEdit)
        hbox.addStretch()
        hbox.addWidget(self.kayit_dosya_yolu_belirle_button)
        hbox.addWidget(self.path_label)
        hbox.addStretch()
        hbox.addWidget(self.combo_box)

        self.setLayout(hbox)

    def open_file_dialog(self): 
    
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "Dosya Aç", "", "Tüm Dosyalar (*)", options=options)

        self.path_label.setText(file_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    topbar = ToolBar()
    topbar.show()
    sys.exit(app.exec())
