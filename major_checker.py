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

    # print("예) 응용정보공학, 바이오생활공학, 문화미디어, 국제통상, 한국어문화교육")

    if major_num != 0:
        for _ in range (major_num):
            major_list.append(input("복수 전공을 입력하세요: "))     

    if minor_num != 0:
        for _ in range (minor_num):
            minor_list.append(input("부전공을 입력하세요: "))

    if advanced_num != 0:
        for _ in range (advanced_num):
            advanced_list.append(input("심화융합전공을 입력하세요: "))

    return major_list, minor_list, advanced_list

