def apply_theme(widget):
    widget.setStyleSheet("""
        QWidget {
            background-color: #ffffff;
            font-family: 'Segoe UI';
        }
        QPushButton {
            padding: 10px;
            font-size: 14px;
            border-radius: 6px;
            background-color: #0078D4;
            color: white;
        }
        QPushButton:hover {
            background-color: #005A9E;
        }
        QLabel {
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        QLineEdit {
            padding: 8px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }
        QListWidget {
            border: 1px solid #ddd;
            padding: 6px;
            font-size: 14px;
        }
    """)
def apply_input_style(widget):
    widget.setStyleSheet("""
        padding: 8px;
        font-size: 14px;
        border: 2px solid #0078D4;
        border-radius: 6px;
    """)    
def apply_light_theme(widget):
    widget.setStyleSheet("""
        QWidget { background-color: #ffffff; font-family: 'Segoe UI'; }
        QPushButton { background-color: #0078D4; color: white; padding: 10px; border-radius: 6px; }
        QPushButton:hover { background-color: #005A9E; }
        QLabel { font-size: 16px; font-weight: bold; }
        QLineEdit { padding: 8px; border: 1px solid #ccc; border-radius: 6px; }
    """)

def apply_dark_theme(widget):
    widget.setStyleSheet("""
        QWidget { background-color: #1e1e1e; color: #ffffff; font-family: 'Segoe UI'; }
        QPushButton { background-color: #3a3a3a; color: white; padding: 10px; border-radius: 6px; }
        QPushButton:hover { background-color: #555555; }
        QLabel { font-size: 16px; font-weight: bold; color: #ffffff; }
        QLineEdit { padding: 8px; border: 1px solid #555; border-radius: 6px; background-color: #2e2e2e; color: white; }
    """)    