import pandas as pd
from openpyxl import load_workbook

def read_major():
    excel_file_path = 'report.xlsx'
    workbook = load_workbook(excel_file_path)
    sheet = workbook['Table 1']
    df_major = sheet['L3'].value
    first_major = df_major[8:]
    return first_major

