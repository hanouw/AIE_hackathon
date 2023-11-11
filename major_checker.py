import pandas as pd
from openpyxl import load_workbook

def read_major():
    excel_file_path = 'report.xlsx'
    workbook = load_workbook(excel_file_path)
    sheet = workbook['Table 1']
    df_major = sheet['L3'].value
    first_major = df_major[8:]
    return first_major


def get_additional_majors():
    major_num, minor_num, advanced_num = map(int, input("Enter the number of 복수전공, 부전공, 심화전공 you have, separated by space (e.g., 1 0 1 for one 복수전공 and one 심화전공): ").split())
    major_list=[]
    minor_list=[]
    advanced_list=[]

    for a in range (major_num):
        major_list.append(input())

    for b in range (minor_num):
        minor_list.append(input())

    for c in range (advanced_num):
        advanced_list.append(input())

    return major_num, minor_num, advanced_num, major_list, minor_list, advanced_list

