translations = {
    "tr": {
        "title": "⚙️ Ayarlar",
        "theme": "Tema Seçimi",
        "language": "Dil Seçimi"
    },
    "en": {
        "title": "⚙️ Settings",
        "theme": "Theme Selection",
        "language": "Language Selection"
    }
}

def get_text(key, lang="tr"):
    return translations.get(lang, translations["tr"]).get(key, key)