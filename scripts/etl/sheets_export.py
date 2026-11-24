"""
Export winery data from Google Sheets to a local CSV.

Usage:
    python sheets_export.py

Requirements:
    pip install gspread pandas oauth2client
"""

import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

SPREADSHEET_ID = "1XKsUG9CJIyIYwuAOaMV60D1w9s3YaIk2kaMbhg3S3V0"
SHEET_NAME = "Wineries"
OUTPUT_PATH = "../../data/raw/wineries.csv"

def export():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    # Place your service account credentials JSON at the path below
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Exported {len(df)} rows to {OUTPUT_PATH}")

if __name__ == "__main__":
    export()
