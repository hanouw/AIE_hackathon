import pandas as pd

# 엑셀 파일 불러오기
excel_file_path = 'report.xlsx'
df = pd.read_excel(excel_file_path)

# Filter out courses with 'W' grade
df_filtered = df[df['Grade'] != 'W' and df['Grade'] != 'NP']

# Define required credits for each category
required_credits = {"전공기초": 20, "전공필수": 30, "전공선택": 15, "일반교양": 20, "교양기초": 10, "대학교양": 5, "공통기초": 10}

# Calculate the sum of completed credits in each category
completed_credits = df_filtered.groupby("Category")["Credits"].sum()

# Calculate remaining credits
remaining_credits = {category: required_credits[category] - completed_credits.get(category, 0) for category in required_credits}

# Create a DataFrame for the output
output_df = pd.DataFrame(list(remaining_credits.items()), columns=["Category", "Remaining Credits"])

# Write to an Excel file
output_df.to_excel("AIE_hackathon/report_xlsx.xlsx", index=False)

