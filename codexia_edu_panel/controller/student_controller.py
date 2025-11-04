from model.student_model import StudentModel
from view.student_view import StudentView
from PyQt6.QtWidgets import QMessageBox

class StudentController:
    def __init__(self):
        self.model = StudentModel()
        self.view = StudentView()

        self.view.btn_add.clicked.connect(self.add_student)
        self.view.btn_delete.clicked.connect(self.delete_student)

        self.load_students()

    def load_students(self):
        self.view.list_widget.clear()
        for s in self.model.get_all():
            self.view.list_widget.addItem(f"{s[0]} - {s[1]} ({s[2]})")

    def add_student(self):
        name = self.view.name_input.text().strip()
        grade = self.view.grade_input.text().strip()
        if name and grade:
            self.model.add(name, grade)
            self.load_students()
            self.view.name_input.clear()
            self.view.grade_input.clear()
            QMessageBox.information(self.view, "Başarılı", "Öğrenci başarıyla eklendi.")
        else:
            QMessageBox.warning(self.view, "Eksik Bilgi", "Lütfen ad ve sınıf girin.")

    def delete_student(self):
        selected = self.view.list_widget.currentItem()
        if selected:
            student_id = selected.text().split(" - ")[0]
            self.model.delete(student_id)
            self.load_students()
            QMessageBox.information(self.view, "Silindi", "Öğrenci başarıyla silindi.")
        else:
            QMessageBox.warning(self.view, "Seçim Yok", "Lütfen silmek için bir öğrenci seçin.")