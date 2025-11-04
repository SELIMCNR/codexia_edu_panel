from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QStackedWidget, QWidget,
    QVBoxLayout, QPushButton, QHBoxLayout
)
from controller.student_controller import StudentController
from controller.settings_controller import SettingsController
from core.theme import apply_theme
from core.database import init_db

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎓 Eğitim Paneli")
        self.setGeometry(100, 100, 1000, 600)

        # Veritabanı başlat
        init_db()

        # Tema uygula
        apply_theme(self)

        # Merkez widget ve ana layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # Sidebar (sol menü)
        sidebar = QWidget()
        sidebar.setFixedWidth(180)
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(10, 10, 10, 10)
        sidebar_layout.setSpacing(15)
        sidebar.setStyleSheet("background-color: #f3f3f6;")

        # İçerik alanı (modül geçişleri için)
        self.stack = QStackedWidget()

        # Öğrenci modülü
        self.student_controller = StudentController()
        self.stack.addWidget(self.student_controller.view)

        btn_student = QPushButton("👨‍🎓 Öğrenciler")
        btn_student.setStyleSheet("""
            QPushButton {
                background-color: #0078D4;
                color: white;
                padding: 10px;
                font-size: 14px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
        """)
        btn_student.clicked.connect(lambda: self.stack.setCurrentWidget(self.student_controller.view))
        sidebar_layout.addWidget(btn_student)

        # Ayarlar modülü
        self.settings_controller = SettingsController()
        self.stack.addWidget(self.settings_controller.view)

        btn_settings = QPushButton("⚙️ Ayarlar")
        btn_settings.setStyleSheet("""
            QPushButton {
                background-color: #1e1e1e;
                color: white;
                padding: 10px;
                font-size: 14px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #333333;
            }
        """)
        btn_settings.clicked.connect(lambda: self.stack.setCurrentWidget(self.settings_controller.view))
        sidebar_layout.addWidget(btn_settings)

        # Layoutları birleştir
        main_layout.addWidget(sidebar)
        main_layout.addWidget(self.stack)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()