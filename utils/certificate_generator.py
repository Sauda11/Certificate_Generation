from config import TEMPLATE, SIGNATURE
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os


# =====================================================
# OUTPUT FOLDER
# =====================================================

OUTPUT = "generated/certificates"


# =====================================================
# COLORS
# =====================================================

BLUE = (10, 24, 78)
LIGHT_BLUE = (25, 95, 210)
GOLD = (196, 137, 20)
BLACK = (40, 40, 40)


# =====================================================
# POSITIONS
# =====================================================

NAME_Y = 520

COURSE_Y = 680

DATE_POS = (150, 535)

DURATION_POS = (150, 632)

LEVEL_POS = (150, 728)

CERTIFICATE_ID_POS = (150, 820)

SIGNATURE_POS = (650, 825)

SIGNATURE_SIZE = (190, 100)

QR_POS = (1220,750)

QR_SIZE = (150, 150)


# =====================================================
# FONT LOADER
# =====================================================

def load_font(path, size):

    try:
        return ImageFont.truetype(path, size)

    except Exception:
        return ImageFont.load_default()


# =====================================================
# AUTO FONT RESIZE
# =====================================================

def fit_font(draw, text, font_path, start_size, max_width):

    size = start_size

    while size >= 28:

        font = load_font(font_path, size)

        left, top, right, bottom = draw.textbbox(
            (0, 0),
            text,
            font=font
        )

        width = right - left

        if width <= max_width:
            return font

        size -= 2

    return load_font(font_path, 28)


# =====================================================
# CENTER TEXT
# =====================================================

def center_text(draw, text, font, y, image_width, color):

    left, top, right, bottom = draw.textbbox(
        (0, 0),
        text,
        font=font
    )

    width = right - left

    x = (image_width - width) // 2

    draw.text(
        (x, y),
        text,
        fill=color,
        font=font
    )
def generate_certificate(
        student_name,
        course,
        certificate_id,
        issue_date,
        duration,
        level,
        qr_path):

    # ---------------------------------------
    # Open Template
    # ---------------------------------------

    image = Image.open(TEMPLATE).convert("RGBA")

    draw = ImageDraw.Draw(image)

    width, height = image.size

    # ---------------------------------------
    # Fonts
    # ---------------------------------------

    name_font = fit_font(
        draw,
        student_name,
        "fonts/Cinzel-Bold.otf",
        65,
        980
    )

    course_font = fit_font(
        draw,
        course,
        "fonts/Poppins-Regular.ttf",
        60,
        900
    )

    info_font = load_font(
    "fonts/Poppins-Regular.ttf",
    21
    )

    cert_font = load_font(
    "fonts/Poppins-Regular.ttf",
    18
    )

    # ---------------------------------------
    # Student Name
    # ---------------------------------------

    center_text(
        draw,
        student_name,
        name_font,
        NAME_Y,
        width,
        BLUE
    )

    # ---------------------------------------
    # Course Name
    # ---------------------------------------

    center_text(
        draw,
        f'"{course}"',
        course_font,
        COURSE_Y,
        width,
        LIGHT_BLUE
    )

    # ---------------------------------------
    # Left Panel Information
    # ---------------------------------------

    draw.text(
        DATE_POS,
        issue_date,
        fill=BLUE,
        font=info_font
    )

    draw.text(
        DURATION_POS,
        duration,
        fill=BLUE,
        font=info_font
    )

    draw.text(
        LEVEL_POS,
        level,
        fill=BLUE,
        font=info_font
    )

    draw.text(
        CERTIFICATE_ID_POS,
        certificate_id,
        fill=BLUE,
        font=cert_font
    )

    # ---------------------------------------
    # Signature
    # ---------------------------------------

    sign = Image.open(SIGNATURE).convert("RGBA")

    sign = sign.resize(SIGNATURE_SIZE)

    image.paste(
        sign,
        SIGNATURE_POS,
        sign
    )

    # ---------------------------------------
    # QR Code
    # ---------------------------------------

    qr = Image.open(qr_path).convert("RGBA")

    qr = qr.resize(QR_SIZE)

    image.paste(
        qr,
        QR_POS,
        qr
    )
    # ---------------------------------------
    # Save Certificate
    # ---------------------------------------

    os.makedirs(OUTPUT, exist_ok=True)

    output_path = os.path.join(
        OUTPUT,
        f"{certificate_id}.png"
    )

    image.save(
        output_path,
        dpi=(300, 300)
    )

    print("\n========================================")
    print("     FERACODE CERTIFICATE GENERATED")
    print("========================================")
    print(f"Student Name   : {student_name}")
    print(f"Certificate ID : {certificate_id}")
    print(f"Saved To       : {output_path}")
    print("========================================")

    return output_path