import pandas as pd
from detector import is_me_present

def scan_excel(file_path: str) -> bool:
    try:
        # Works for xlsx, xls, csv
        df = pd.read_excel(file_path, header=None)

        for row in df.itertuples(index=False):
            row_text = " ".join(map(str, row))
            if is_me_present(row_text):
                return True

    except Exception as e:
        print("Excel scan error:", e)

    return False
