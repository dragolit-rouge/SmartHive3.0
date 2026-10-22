from PySide6.QtWidgets import QTabWidget, QMessageBox
import sqlite3
from table_config import TableConfig        # Ваш первый готовый скрипт (таблица)
from connect_variant import ConnectVariant  # Ваш второй готовый скрипт (текст + кнопка)

class TabConstruct(QTabWidget):
    def __init__(self, db_name, table_a, name_table, key_column, parent=None):
        super().__init__(parent)
        self.db_name = db_name
        self.name_table = name_table
        self.key_column = key_column
        self.table_a = table_a

        self.tab_connect = ConnectVariant(label_text="Введите ваш ключ:", btn_text="Подключиться")
        
        self.tab_database = TableConfig(db_name, column_name = "*", table_name="uley")
        self.tab_database2 = TableConfig(db_name, column_name = "name, rtime, date, units", table_name="sensor")

        self.addTab(self.tab_connect, "Подключение") #0
        self.addTab(self.tab_database, "Доступные ульи") #1
        self.addTab(self.tab_database2, "Доступные датчики") #2

        self.setTabEnabled(1, False) 
        self.setTabEnabled(2, False)

        self.tab_connect.sign.connect(self.unlocker)

    def checker(self, key):
        try:
            conn = sqlite3.connect(self.db_name)
            cur = conn.cursor()

            q = f"SELECT {self.name_table} FROM {self.table_a} WHERE {self.key_column} = ?"
            cur.execute(q, (key,))
            result = cur.fetchone()
            conn.close()

            if result:
                return result[0] # Возвращаем чистый текст
            return None

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Ошибка БД", f"Не удалось проверить данные в БД:\n{e}")
            return False

    def unlocker(self, resp):
        if not self.checker(resp):
            QMessageBox.warning(self, "Ошибка доступа", "Значение не найдено в базе данных!")
            self.setTabEnabled(1, False) 
            self.setTabEnabled(2, False)
            return

        self.setTabEnabled(1, True) 
        self.setTabEnabled(2, True)
        success_message = f"Вы успешно подключились к {self.checker(resp)}!"
        
        self.tab_connect.status_label.setText(success_message) # Меняем пустой текст на нужный
        self.tab_connect.status_label.show()

        self.tab_database.load_data(resp = resp)
        self.tab_database2.load_data(resp = resp)
