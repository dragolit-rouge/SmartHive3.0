import sqlite3
from PySide6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QMessageBox, QLabel

class TableConfig(QWidget):
    def __init__(self, db_name, column_name, table_name, parent=None):
        super().__init__(parent)
        self.db_name = db_name
        self.column_name = column_name
        self.table_name = table_name
        
        self.init_ui() #интерфейс строится после того, как задан класс и стопроцентно всё загрузилось, чтобы избежать ошибок
        self.load_data()

    def init_ui(self, label_text = None):
        layout = QVBoxLayout(self)
        
        self.label_text = None

        if label_text is not None:
            self.label_text = QLabel(str(label_text))
            layout.addWidget(self.label_text)
        
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)
        
        self.setLayout(layout)

    def load_data(self, resp = None):
        conn = sqlite3.connect(self.db_name)
        conn.execute("PRAGMA foreign_keys = ON")
        cur = conn.cursor()
        if self.table_name == "uley":
                if resp is not None:
                    cur.execute("SELECT * FROM uley WHERE id_pasek = ?", (resp,))

                else:
                    cur.execute("SELECT * FROM uley")
                    
            
        elif self.table_name == "sensor":
            if resp is not None:
                query = """
                        SELECT target.* 
                        FROM sensor AS target
                        JOIN uley AS middle ON target.id_uley = middle.id
                        WHERE middle.id_pasek = ?
                    """
                cur.execute(query, (resp,))
            else:
                    
                cur.execute(f"SELECT {self.column_name} FROM sensor")
                    
            
        else:
            cur.execute("")
            '''if resp is not None:
            query = """
                SELECT target.* 
                FROM sensor AS target
                JOIN uley AS middle ON target.id_uley = middle.id
                WHERE middle.id_pasek = ?
            """
            cur.execute(query, (resp,))
        else:
            cur.execute("SELECT * FROM uley")'''

        #cur.execute(f"SELECT {self.column_name} FROM {self.table_name}")
        rows = cur.fetchall()
        conn.close()
        columns = [desc[0] for desc in cur.description]
        
        self.table_widget.setColumnCount(len(columns)) #создание нужного количества колонок
        self.table_widget.setHorizontalHeaderLabels(columns) #подписи всех колонок
            
        if not rows:
            return

        self.table_widget.setRowCount(len(rows)) #создание нужного количества строк
        for row_idx, row_data in enumerate(rows):
            for col_idx, value in enumerate(row_data): #пары (индекс, значение)
                item_text = "" if value is None else str(value)
                self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(item_text)) #вставляем значения
                    