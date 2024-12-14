from psycopg2.extras import RealDictCursor

from db_config import get_connection


def add_student(name, email, password):
    connection = get_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                query = """
                INSERT INTO students (name, email, password_hash) 
                VALUES (%s, %s, %s)
                """
                cursor.execute(query, (name, email, password))
                connection.commit()
                print("Student added successfully.")
        except Exception as e:
            print("Error adding student:", e)
        finally:
            connection.close()


def view_students():
    connection = get_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM students")
                students = cursor.fetchall()
                for student in students:
                    print(student)
        except Exception as e:
            print("Error viewing students:", e)
        finally:
            connection.close()


def update_student(student_id, name, email):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            if name:
                cursor.execute(
                    "UPDATE students SET name = %s WHERE id = %s",
                    (name, student_id)
                )
            if email:
                cursor.execute(
                    "UPDATE students SET email = %s WHERE id = %s",
                    (email, student_id)
                )
            connection.commit()
            print("Student updated successfully.")
    except Exception as e:
        print("Error updating student:", e)
    finally:
        connection.close()


def delete_student(student_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
            connection.commit()
            print("Student deleted successfully.")
    except Exception as e:
        print("Error deleting student:", e)
    finally:
        connection.close()


def get_teachers(student_id):
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            query = """
                SELECT t.id, t.name, t.email 
                FROM teachers t
                JOIN student_teacher st ON t.id = st.teacher_id
                WHERE st.student_id = %s
            """
            cursor.execute(query, (student_id,))
            teachers = cursor.fetchall()
            print(teachers)
    except Exception as e:
        print("Error get teachers :", e)
    finally:
        conn.close()
