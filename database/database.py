import sqlite3

DATABASE_NAME = "database/certificates.db"


def connect():
    return sqlite3.connect(DATABASE_NAME)


def create_database():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS certificates (

        certificate_id TEXT PRIMARY KEY,

        student_name TEXT NOT NULL,

        course TEXT NOT NULL,

        issue_date TEXT,

        duration TEXT,

        level TEXT,

        email TEXT,

        phone TEXT,

        status TEXT

    )
    """)

    conn.commit()
    conn.close()

    print("✅ Database Ready")


def add_certificate(data):

    conn = connect()
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
    """, data)

    conn.commit()
    conn.close()


def get_certificate(certificate_id):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM certificates
    WHERE certificate_id = ?
    """, (certificate_id,))

    data = cursor.fetchone()

    conn.close()

    return data


def get_all():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM certificates
    ORDER BY student_name
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def delete_certificate(certificate_id):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM certificates
    WHERE certificate_id = ?
    """, (certificate_id,))

    conn.commit()
    conn.close()


def update_status(certificate_id, status):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE certificates
    SET status = ?
    WHERE certificate_id = ?
    """, (status, certificate_id))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_database()