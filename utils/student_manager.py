import sqlite3
from openpyxl import load_workbook

EXCEL_FILE = "students/students.xlsx"
DATABASE_FILE = "database/certificates.db"


def add_student(student):
    """
    Saves a student to both SQLite Database and Excel.
    """

    # -----------------------------
    # Save to SQLite Database
    # -----------------------------
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO certificates (
        certificate_id,
        student_name,
        course,
        issue_date,
        duration,
        level,
        email,
        phone,
        status
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        student["certificate_id"],
        student["student_name"],
        student["course"],
        student["issue_date"],
        student["duration"],
        student["level"],
        student["email"],
        student["phone"],
        student["status"]

    ))

    conn.commit()
    conn.close()

    # -----------------------------
    # Save to Excel
    # -----------------------------
    workbook = load_workbook(EXCEL_FILE)
    sheet = workbook.active

    sheet.append([
        student["student_name"],
        student["course"],
        student["certificate_id"],
        student["issue_date"],
        student["duration"],
        student["level"],
        student["email"],
        student["phone"],
        student["status"]
    ])

    workbook.save(EXCEL_FILE)

    print("\n✅ Student saved successfully!")
    print("   ✔ Database Updated")
    print("   ✔ Excel Updated")