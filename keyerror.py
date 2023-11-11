import pandas as pd

# 엑셀 파일 불러오기
excel_file_path = 'report.xlsx'
df = pd.read_excel(excel_file_path)
#print(df.columns)

# Filter out courses with 'W' grade
df_filtered_평가 = df[(df['Unnamed: 17'] != 'W') & (df['Unnamed: 17'] != 'NP') & (df['Unnamed: 17'] != 'F')]
df_filtered_과목종별_전기 = df[df['Unnamed: 11'] == '전기']
df_filtered_과목종별_전선 = df[df['Unnamed: 11'] == '전선']
df_filtered_과목종별_전필 = df[df['Unnamed: 11'] == '전필']
df_filtered_과목종별_RC = df[df['Unnamed: 11'] == 'RC']
df_filtered_과목종별_GLC교양 = df[df['Unnamed: 11'] == '대교' and df['학정번호'].str[:3] == 'GLC']
# filtered_df = df[df['학정번호'].str[:3] == 'GLC']

# Define required credits for each category
required_credits = {"전공기초": 20, "전공필수": 30, "전공선택": 15, "일반교양": 20, "교양기초": 10, "대학교양": 5, "공통기초": 10}

# Calculate the sum of completed credits in each category
completed_credits = df_filtered.groupby("Category")["Credits"].sum()

# Calculate remaining credits
remaining_credits = {category: required_credits[category] - completed_credits.get(category, 0) for category in required_credits}

# Create a DataFrame for the output
output_df = pd.DataFrame(list(remaining_credits.items()), columns=["Category", "Remaining Credits"])

# Write to an Excel file
output_df.to_excel("result_file.xlsx", index=False)