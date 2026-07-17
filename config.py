import os

# -----------------------------
# Project Paths
# -----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE = os.path.join(BASE_DIR, "database", "certificates.db")

TEMPLATE = os.path.join(BASE_DIR, "templates", "certificate.png")

LOGO = os.path.join(BASE_DIR, "templates", "logo.png")

SIGNATURE = os.path.join(BASE_DIR, "templates", "signature.png")

FONT_TITLE = os.path.join(BASE_DIR, "fonts", "Cinzel-Bold.ttf")

FONT_TEXT = os.path.join(BASE_DIR, "fonts", "Poppins-Regular.ttf")

QR_FOLDER = os.path.join(BASE_DIR, "generated", "qr")

CERTIFICATE_FOLDER = os.path.join(BASE_DIR, "generated", "certificates")

PDF_FOLDER = os.path.join(BASE_DIR, "generated", "pdf")

EXCEL_FILE = os.path.join(BASE_DIR, "students", "students.xlsx")

# -----------------------------
# Academy Information
# -----------------------------

ACADEMY_NAME = "FERACODE IT Learning Academy"

TAGLINE = "Coding for the Fearless Era"

CERTIFICATE_PREFIX = "FERA"