from core.database import get_connection

class StudentModel:
    def get_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, grade FROM students")
        result = cursor.fetchall()
        conn.close()
        return result

    def add(self, name, grade):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (name, grade))
        conn.commit()
        conn.close()

    def delete(self, student_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        conn.close()