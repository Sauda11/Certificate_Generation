from config import QR_FOLDER
import os
import qrcode



def generate_qr(certificate_id):
    """
    Generate a QR code containing only the certificate ID.
    Returns the saved image path.
    """

    os.makedirs(QR_FOLDER, exist_ok=True)

    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    # Offline verification data
    qr.add_data(certificate_id)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    qr_path = os.path.join(QR_FOLDER, f"{certificate_id}.png")

    img.save(qr_path)

    return qr_path


if __name__ == "__main__":
    cid = "FERA202600001"

    path = generate_qr(cid)

    print("QR Code Saved:")
    print(path)