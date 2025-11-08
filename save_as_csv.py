import pandas as pd
from pathlib import Path
from datetime import datetime

XLSX_PATH = Path("excel") / "Praxisnachbereitung.xlsx"
SHEET = "Ausleihen_gesamt"
OUT_PATH = Path(f"exports/gesamttabelle_{datetime.now():%Y-%m-%d}.csv")

def main():
    df = pd.read_excel(XLSX_PATH, sheet_name=SHEET, engine="openpyxl")
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False, sep=";", encoding="utf-8")
    print(f"Export ok -> {OUT_PATH.resolve()}")

if __name__ == "__main__":
    main()
