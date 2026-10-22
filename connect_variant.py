from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap

class ConnectVariant(QWidget):
    sign = Signal(str)

    def __init__(self, label_text, btn_text, picture, parent = None):
        super().__init__(parent)

        self.label_text = label_text
        self.btn_text = btn_text
        self.picture = picture
        
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        self.label = QLabel(self.label_text)

        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Например, 1234567")
        self.edit.setMaximumWidth(3000)

        self.btn = QPushButton(self.btn_text)
        self.btn.setFixedSize(120, 30)

        pixmap = QPixmap(self.picture)
        self.image = QLabel()
        self.image.setPixmap(pixmap)
        self.image.setScaledContents(True)


        self.status_label = QLabel("")
        self.status_label.hide()


        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.edit, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.btn, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.status_label, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addStretch(1)

        layout.addWidget(self.image, alignment=Qt.AlignmentFlag.AlignRight)

        layout.addStretch(0.5)

        self.btn.clicked.connect(self.btn_click)

    def btn_click(self):
        val = self.edit.text().strip()
        if val:
            self.sign.emit(val)