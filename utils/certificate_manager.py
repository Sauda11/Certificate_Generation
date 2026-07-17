import os

from utils.excel_reader import (
    read_students,
    update_student_status
)

from utils.qr_generator import generate_qr
from utils.certificate_generator import generate_certificate
from utils.pdf_generator import generate_pdf


def search_student(search_term):
    """
    Search student by Certificate ID or Student Name.
    Returns student dictionary if found.
    """

    students = read_students()

    search_term = search_term.strip().lower()

    for student in students:

        if (
            student["certificate_id"].lower() == search_term
            or student["student_name"].lower() == search_term
        ):
            return student

    return None


def display_student(search_term):
    """
    Display student details.
    """

    student = search_student(search_term)

    if student is None:

        print("\n❌ Student not found.")
        return

    print("\n========================================")
    print("            Student Details")
    print("========================================")
    print(f"Name          : {student['student_name']}")
    print(f"Course        : {student['course']}")
    print(f"Certificate ID: {student['certificate_id']}")
    print(f"Issue Date    : {student['issue_date']}")
    print(f"Duration      : {student['duration']}")
    print(f"Level         : {student['level']}")
    print(f"Email         : {student['email']}")
    print(f"Phone         : {student['phone']}")
    print(f"Status        : {student['status']}")
    print("========================================")


def build_certificate(student, output_format="png"):
    """
    Generates certificate.

    output_format:
        png
        pdf
        both
    """

    os.makedirs("generated/pdf", exist_ok=True)

    # -------------------------
    # Generate QR Code
    # -------------------------

    qr_path = generate_qr(student["certificate_id"])

    # -------------------------
    # Generate PNG Certificate
    # -------------------------

    png_path = generate_certificate(

        student_name=student["student_name"],
        course=student["course"],
        certificate_id=student["certificate_id"],
        issue_date=student["issue_date"],
        duration=student["duration"],
        level=student["level"],
        qr_path=qr_path

    )

    # -------------------------
    # Generate PDF
    # -------------------------

    if output_format in ("pdf", "both"):

        pdf_path = f"generated/pdf/{student['certificate_id']}.pdf"

        generate_pdf(

            certificate_png_path=png_path,
            output_pdf_path=pdf_path

        )

    # -------------------------
    # Update Excel Status
    # -------------------------

    update_student_status(

        student["certificate_id"],
        "Generated"

    )

    # -------------------------
    # Success Message
    # -------------------------

    print("\n========================================")
    print("     Certificate Generated Successfully")
    print("========================================")
    print(f"Student Name   : {student['student_name']}")
    print(f"Certificate ID : {student['certificate_id']}")
    print(f"Output Format  : {output_format.upper()}")
    print(f"Status         : Generated")
    print("========================================")


def generate_single_certificate(search_term, output_format="png"):
    """
    Generate certificate for one student.
    """

    student = search_student(search_term)

    if student is None:

        print("\n❌ Student not found.")
        return

    build_certificate(student, output_format)


def generate_all_certificates(output_format="png"):
    """
    Generate certificates for all students.
    """

    students = read_students()

    if len(students) == 0:

        print("\n❌ No students found.")
        return

    print(f"\nGenerating {len(students)} certificate(s)...")

    for student in students:

        build_certificate(student, output_format)

    print("\n🎉 All certificates generated successfully!")