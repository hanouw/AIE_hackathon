import pandas as pd

# 엑셀 파일 불러오기
excel_file_path = 'report.xlsx'
df = pd.read_excel(excel_file_path, header=3)



# Filter out courses
df_filtered_과목종별_전기 = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == '전기')]
df_filtered_과목종별_전선 = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == '전선')]
df_filtered_과목종별_전필 = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == '전필')]
df_filtered_과목종별_RC = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == 'RC')]
df_filtered_과목종별_GLC교양 = df[(~df['평가'].isin(['W', 'NP', 'F', 'U'])) & (df['과목 종별'] == '대교') & (df['학정번호'].str[:3] == 'GLC')]


# Define required credits for each category
required_credits = {"전공기초": 20, "전공필수": 30, "전공선택": 15, "일반교양": 20, "교양기초": 10, "대학교양": 5, "공통기초": 10}

# Calculate the sum of completed credits in each category
completed_credits_전기 = df_filtered_과목종별_전기.groupby("학점").sum()
completed_credits_전선 = df_filtered_과목종별_전선.groupby("학점").sum()
completed_credits_전필 = df_filtered_과목종별_전필.groupby("학점").sum()
completed_credits_RC = df_filtered_과목종별_RC.groupby("학점").sum()
completed_credits_GLC교양 = df_filtered_과목종별_GLC교양.groupby("학점").sum()

remaining_credits = {
    "전기": required_credits["전기"] - completed_credits_전기,
    "전선": required_credits["전선"] - completed_credits_전선,
    "전필": required_credits["전필"] - completed_credits_전필,
    "RC": required_credits["RC"] - completed_credits_RC,
    "GLC교양": required_credits["GLC교양"] - completed_credits_GLC교양
}

# Create a DataFrame for the output
output_df = pd.DataFrame(list(remaining_credits.items()), columns=["Category", "Remaining Credits"])

# Write to an Excel file
output_df.to_excel("result_file.xlsx", index=False)

