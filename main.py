from utils.certificate_manager import (
    display_student,
    generate_single_certificate,
    generate_all_certificates
)

from utils.student_manager import add_student
from utils.id_generator import generate_certificate_id
from utils.date_validator import validate_date

from utils.input_validator import (
    validate_name,
    validate_course,
    validate_duration,
    validate_level,
    validate_email,
    validate_phone
)


def student_menu():

    while True:

        print("\n========== Student Management ==========")
        print("1. Search Student")
        print("2. Add Student")
        print("3. Edit Student")
        print("4. Delete Student")
        print("5. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            search = input("\nEnter Student Name or Certificate ID: ").strip()
            display_student(search)

        elif choice == "2":

            student = {}

            print("\n========== Add Student ==========\n")

            # Student Name
            while True:

                name = input("Student Name : ").strip()

                if validate_name(name):
                    student["student_name"] = name
                    break

                print("❌ Name cannot be empty.\n")

            # Course
            while True:

                course = input("Course       : ").strip()

                if validate_course(course):
                    student["course"] = course
                    break

                print("❌ Course cannot be empty.\n")

            # Issue Date
            while True:

                issue_date = input("Issue Date (DD-MM-YYYY): ").strip()

                if validate_date(issue_date):
                    student["issue_date"] = issue_date
                    break

                print("❌ Invalid date. Example: 13-07-2026\n")

            # Duration
            while True:

                duration = input("Duration     : ").strip()

                if validate_duration(duration):
                    student["duration"] = duration
                    break

                print("❌ Duration cannot be empty.\n")

            # Level
            while True:

                level = input("Level        : ").strip()

                if validate_level(level):
                    student["level"] = level
                    break

                print("❌ Level cannot be empty.\n")

            # Email
            while True:

                email = input("Email        : ").strip()

                if validate_email(email):
                    student["email"] = email
                    break

                print("❌ Invalid email address.\n")

            # Phone
            while True:

                phone = input("Phone        : ").strip()

                if validate_phone(phone):
                    student["phone"] = phone
                    break

                print("❌ Phone number must contain exactly 10 digits.\n")

            # Auto Generate Certificate ID
            student["certificate_id"] = generate_certificate_id()
            print("Generated Certificate ID:", student["certificate_id"])
            # Default Status
            student["status"] = "Pending"

            # Summary
            print("\n========================================")
            print("           Student Summary")
            print("========================================")

            print(f"Student Name   : {student['student_name']}")
            print(f"Course         : {student['course']}")
            print(f"Issue Date     : {student['issue_date']}")
            print(f"Duration       : {student['duration']}")
            print(f"Level          : {student['level']}")
            print(f"Email          : {student['email']}")
            print(f"Phone          : {student['phone']}")
            print(f"Certificate ID : {student['certificate_id']}")
            print(f"Status         : {student['status']}")

            print("========================================")

            confirm = input("\nSave Student? (Y/N): ").strip().lower()

            if confirm == "y":

                add_student(student)

            else:

                print("\n❌ Student not saved.")

        elif choice == "3":

            print("\n🚧 Edit Student - Coming Soon")

        elif choice == "4":

            print("\n🚧 Delete Student - Coming Soon")

        elif choice == "5":

            break

        else:

            print("\n❌ Invalid Choice.")


def certificate_menu():

    while True:

        print("\n========== Certificate Generation ==========")
        print("1. Generate PNG Certificate")
        print("2. Generate PDF Certificate")
        print("3. Generate PNG + PDF")
        print("4. Generate ALL Certificates")
        print("5. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            search = input("\nStudent Name or Certificate ID: ").strip()
            generate_single_certificate(search, "png")

        elif choice == "2":

            search = input("\nStudent Name or Certificate ID: ").strip()
            generate_single_certificate(search, "pdf")

        elif choice == "3":

            search = input("\nStudent Name or Certificate ID: ").strip()
            generate_single_certificate(search, "both")

        elif choice == "4":

            print("\nOutput Format")
            print("1. PNG")
            print("2. PDF")
            print("3. PNG + PDF")

            fmt = input("\nSelect Output Format: ").strip()

            if fmt == "1":

                generate_all_certificates("png")

            elif fmt == "2":

                generate_all_certificates("pdf")

            elif fmt == "3":

                generate_all_certificates("both")

            else:

                print("\n❌ Invalid Option.")

        elif choice == "5":

            break

        else:

            print("\n❌ Invalid Choice.")


def verification_menu():

    while True:

        print("\n========== Verification ==========")
        print("1. Verify Certificate (Coming Soon)")
        print("2. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            print("\n🚧 Verification module coming soon.")

        elif choice == "2":

            break

        else:

            print("\n❌ Invalid Choice.")


def reports_menu():

    while True:

        print("\n========== Reports ==========")
        print("1. View Reports (Coming Soon)")
        print("2. Back")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            print("\n🚧 Reports module coming soon.")

        elif choice == "2":

            break

        else:

            print("\n❌ Invalid Choice.")


def main():

    while True:

        print("\n========================================")
        print("     FERACODE CERTIFICATE SYSTEM")
        print("========================================")
        print("1. Student Management")
        print("2. Certificate Generation")
        print("3. Verification")
        print("4. Reports")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            student_menu()

        elif choice == "2":

            certificate_menu()

        elif choice == "3":

            verification_menu()

        elif choice == "4":

            reports_menu()

        elif choice == "5":

            print("\nThank you for using FERACODE!")
            print("Goodbye! 👋")
            break

        else:

            print("\n❌ Invalid Choice.")


if __name__ == "__main__":
    main()