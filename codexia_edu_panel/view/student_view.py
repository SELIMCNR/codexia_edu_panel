from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QListWidget, QSpacerItem, QSizePolicy, QFormLayout
)
from core.theme import apply_input_style

class StudentView(QWidget):
    def __init__(self):
        super().__init__()

        # Ana dikey layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        # Başlık
        self.title = QLabel("📋 Öğrenci Listesi")
        layout.addWidget(self.title)

        # Liste
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        # Giriş alanları için form layout
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Ad Soyad")
        apply_input_style(self.name_input)

        self.grade_input = QLineEdit()
        self.grade_input.setPlaceholderText("Sınıf")
        apply_input_style(self.grade_input)

        form_layout = QFormLayout()
        form_layout.setSpacing(10)
        form_layout.addRow("Ad Soyad:", self.name_input)
        form_layout.addRow("Sınıf:", self.grade_input)
        layout.addLayout(form_layout)

        # Spacer: butonları alta sabitlemek için
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        layout.addItem(spacer)

        # Butonlar
        self.btn_add = QPushButton("➕ Ekle")
        self.btn_delete = QPushButton("❌ Sil")
        layout.addWidget(self.btn_add)
        layout.addWidget(self.btn_delete)