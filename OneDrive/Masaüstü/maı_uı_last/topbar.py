from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys

icon_size = 30
button_size = 40


class TopBar(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def goruntu_ve_kaynak_func(self) -> None:
        goruntuKaynagiButton = QPushButton("CANLI")

        goruntuKaynagihbox = QHBoxLayout()
        goruntuKaynagihbox.addWidget(QLabel("GÖRÜNTÜ KAYNAĞI:"))
        goruntuKaynagihbox.addWidget(goruntuKaynagiButton)

        kaynakButton = QPushButton("OBS Virtual Camera")

        kaynakhbox = QHBoxLayout()
        kaynakhbox.addWidget(QLabel("KAYNAK:"))
        kaynakhbox.addWidget(kaynakButton)

        self.goruntu_ve_kaynak_vbox = QVBoxLayout()
        self.goruntu_ve_kaynak_vbox.addLayout(goruntuKaynagihbox)
        self.goruntu_ve_kaynak_vbox.addLayout(kaynakhbox)

    def ayarlar_ve_fps_func(self) -> None:
        ayarlarButton = QPushButton()
        ayarlarButton.setIcon(QIcon("images/ayarlar.png"))
        ayarlarButton.setIconSize(QSize(icon_size, icon_size))
        ayarlarButton.setFixedSize(button_size, button_size)

        ayarlarvbox = QVBoxLayout()
        ayarlarvbox.addWidget(ayarlarButton, alignment=Qt.AlignCenter)
        ayarlarvbox.addWidget(QLabel("Ayarlar"), alignment=Qt.AlignCenter)

        self.fpslabel = QLabel(str(0))

        fpshbox = QHBoxLayout()
        fpshbox.addWidget(QLabel("CİHAZ FPS:"))
        #kamera fps değeri buraya gelecek
        #fps = kamera.get(cv2.CAP_PROP_FPS)
        fpshbox.addWidget(self.fpslabel)
        self.ayarlar_ve_fps_hbox = QHBoxLayout()
        self.ayarlar_ve_fps_hbox.addLayout(ayarlarvbox)
        self.ayarlar_ve_fps_hbox.addLayout(fpshbox)

    def kayit_ve_kayit_durdur_func(self) -> None:
        kayitButton = QPushButton()
        kayitButton.setIcon(QIcon("images/kayit.png"))
        kayitButton.setIconSize(QSize(icon_size, icon_size))
        kayitButton.setFixedSize(button_size, button_size)

        kayit_vbox = QVBoxLayout()
        kayit_vbox.addWidget(kayitButton, alignment=Qt.AlignCenter)
        kayit_vbox.addWidget(QLabel("Kayıt"), alignment=Qt.AlignCenter)

        kayitdurdurButton = QPushButton()
        kayitdurdurButton.setIcon(QIcon("images/kayitdurdur.png"))
        kayitdurdurButton.setIconSize(QSize(icon_size, icon_size))
        kayitdurdurButton.setFixedSize(button_size, button_size)

        kayitdurdur_vbox = QVBoxLayout()
        kayitdurdur_vbox.addWidget(kayitdurdurButton, alignment=Qt.AlignCenter)
        kayitdurdur_vbox.addWidget(
        QLabel("Kayıt Durdur"), alignment=Qt.AlignCenter)

        self.kayit_ve_kayit_durdur_hbox = QHBoxLayout()
        self.kayit_ve_kayit_durdur_hbox.addLayout(kayit_vbox)
        self.kayit_ve_kayit_durdur_hbox.addLayout(kayitdurdur_vbox)

    def baslat_duraklat_func(self) -> None:
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.zamaniGuncelle)
        self.is_running = False

        baslatButton = QPushButton("BAŞLAT")
        self.timer_label = QLabel("0:00")
        duraklatButton = QPushButton("DURAKLAT")

        hbox1 = QHBoxLayout()
        hbox1.addWidget(baslatButton)
        baslatButton.clicked.connect(self.start_timer)
        hbox1.addWidget(self.timer_label)
        hbox1.addWidget(duraklatButton)
        duraklatButton.clicked.connect(self.timer.stop)

        self.checkbox = QCheckBox()
        self.lcd = QLCDNumber()
        self.lcd.display(120)
        sifirlaButton = QPushButton("SIFIRLA")
        resetleButton = QPushButton("RESETLE")
        resetleButton.clicked.connect(self.reset_timer)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.checkbox)
        hbox2.addWidget(self.lcd)
        hbox2.addWidget(sifirlaButton)

        self.baslat_duraklat_vbox = QVBoxLayout()
        self.baslat_duraklat_vbox.addLayout(hbox1)
        self.baslat_duraklat_vbox.addLayout(hbox2)

    def start_timer(self):
        self.timer.start(1000)
        self.is_running = True  

    def reset_timer(self):
        self.timer.stop()
        self.timer_label.setText("0:00")
        self.is_running = False

    def zamaniGuncelle(self):
        current_time = self.timer_label.text()
        time = QTime.fromString(current_time, "m:ss")
        time = time.addSecs(1)  
        self.timer_label.setText(time.toString("m:ss"))

    def initUI(self) -> None:
        self.logo = QLabel()

        self.goruntu_ve_kaynak_func()
        self.ayarlar_ve_fps_func()
        self.kayit_ve_kayit_durdur_func()
        self.baslat_duraklat_func()

        resetleButton = QPushButton("RESETLE")
        resetleButton.setFont(QFont("Arial", 8, QFont.Bold))

        widgets_and_layouts = [
            self.logo,
            self.goruntu_ve_kaynak_vbox,
            self.ayarlar_ve_fps_hbox,
            self.kayit_ve_kayit_durdur_hbox,
            self.baslat_duraklat_vbox,
            resetleButton,
        ]

        lines = []
        for i in range(len(widgets_and_layouts)):
            lines.append(QFrame())
            lines[i].setFrameShape(QFrame.VLine)
            lines[i].setFrameShadow(QFrame.Sunken)

        hbox = QHBoxLayout()
        for i, layout_or_widget in enumerate(widgets_and_layouts):
            try:
                hbox.addWidget(layout_or_widget)
            except TypeError:
                hbox.addLayout(layout_or_widget)
            hbox.addWidget(lines[i])

        self.setLayout(hbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    topbar = TopBar()
    topbar.show()
    sys.exit(app.exec())
