from view.settings_view import SettingsView
from core.theme import apply_light_theme, apply_dark_theme
from core.language import get_text

class SettingsController:
    def __init__(self):
        self.view = SettingsView()
        self.view.theme_combo.currentIndexChanged.connect(self.change_theme)
        self.view.lang_combo.currentIndexChanged.connect(self.change_language)

    def change_theme(self, index):
        if index == 0:
            apply_light_theme(self.view)
        else:
            apply_dark_theme(self.view)

    def change_language(self, index):
        self.view.lang = "tr" if index == 0 else "en"
        self.view.title.setText(get_text("title", self.view.lang))
        self.view.theme_label.setText(get_text("theme", self.view.lang))
        self.view.lang_label.setText(get_text("language", self.view.lang))