from utils.certificate_generator import generate_certificate

generate_certificate(
    student_name="John Doe",
    course="Python Programming",
    certificate_id="FERA202600001",
    issue_date="13 July 2026",
    duration="40 Hours",
    level="Beginner",
    qr_path="generated/qr/FERA202600001.png"
)