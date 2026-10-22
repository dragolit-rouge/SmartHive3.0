import sys
import sqlite3
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QHBoxLayout, QLabel, QLineEdit,
    QTableWidgetItem, QVBoxLayout, QWidget, QMessageBox, QPushButton
)
from tab_construct import TabConstruct
from connect_variant import ConnectVariant

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Умный улей 3.0 Панель управления")
        self.resize(950, 650)

        self.container = TabConstruct(
            db_name = "uley3_0.db",
            table_a = "pasek",
            name_table = "name",
            key_column = "id"
        )
        

        self.setCentralWidget(self.container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())