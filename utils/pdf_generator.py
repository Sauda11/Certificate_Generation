from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import landscape, A4
import os


def generate_pdf(certificate_png_path, output_pdf_path):
    """
    Converts a PNG certificate into a PDF.
    """

    if not os.path.exists(certificate_png_path):
        raise FileNotFoundError(f"{certificate_png_path} not found.")

    pdf = canvas.Canvas(output_pdf_path, pagesize=landscape(A4))

    width, height = landscape(A4)

    image = ImageReader(certificate_png_path)

    pdf.drawImage(
        image,
        0,
        0,
        width=width,
        height=height
    )

    pdf.save()

    print(f"✅ PDF saved to {output_pdf_path}")