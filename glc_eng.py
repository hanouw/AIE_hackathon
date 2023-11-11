import pandas as pd
excel_file_path = 'report.xlsx'
df = pd.read_excel(excel_file_path, header=3)

#GLC영어 이수 유무
GLC영어_학점 = 0
if df[df['교과목명'] == 'GLC영어1' & df['학점'] == 3]:
    GLC영어_학점 += 3
else: 
    pass
if df[df['교과목명'] == 'GLC영어2' & df['학점'] == 3]:
    GLC영어_학점 += 3
else:
    pass

