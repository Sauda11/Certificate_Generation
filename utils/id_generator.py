import pandas as pd

EXCEL_FILE = "students/students.xlsx"

PREFIX = "FERA2026"


def generate_certificate_id():
    """
    Generates the next Certificate ID.
    Example:
        FERA202600001
        FERA202600002
    """

    try:
        df = pd.read_excel(EXCEL_FILE)

        if df.empty:
            return PREFIX + "00001"

        ids = df["Certificate ID"].dropna().astype(str)

        numbers = []

        for cert_id in ids:

            if cert_id.startswith(PREFIX):
                try:
                    numbers.append(int(cert_id.replace(PREFIX, "")))
                except ValueError:
                    pass

        if not numbers:
            return PREFIX + "00001"

        next_number = max(numbers) + 1

        return f"{PREFIX}{next_number:05d}"

    except FileNotFoundError:

        return PREFIX + "00001"