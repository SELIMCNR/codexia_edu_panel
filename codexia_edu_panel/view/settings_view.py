from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox
from core.language import get_text

class SettingsView(QWidget):
    def __init__(self):
        super().__init__()
        self.lang = "tr"
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        self.title = QLabel(get_text("title", self.lang))
        layout.addWidget(self.title)

        self.theme_label = QLabel(get_text("theme", self.lang))
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Açık Tema", "Koyu Tema"])
        layout.addWidget(self.theme_label)
        layout.addWidget(self.theme_combo)

        self.lang_label = QLabel(get_text("language", self.lang))
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["Türkçe", "English"])
        layout.addWidget(self.lang_label)
        layout.addWidget(self.lang_combo)