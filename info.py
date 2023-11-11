import pandas as pd

# 엑셀 파일 불러오기
excel_file_path = '파일경로/파일이름.xlsx'
df = pd.read_excel(excel_file_path)

# 특정 row 불러오기
row_index = 0  # 원하는 행의 인덱스
selected_row = df.iloc[row_index]
print("Selected Row:")
print(selected_row)

# 특정 column 불러오기
column_name = 'ColumnName'  # 원하는 열의 이름
selected_column = df[column_name]
print("\nSelected Column:")
print(selected_column)
