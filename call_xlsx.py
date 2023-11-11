import pandas as pd
import numpy as np

from read_major import read_major
from major_checker import get_additional_majors

#복수, 부, 심화 전공 여부 및 어떠한 전공인지 확인
# majors_dict, double_majors, minors, advanced_majors = get_additional_majors()----------------------------------------나중에 키기


import os
os.system('cls')

# 엑셀 파일 불러오기
excel_file_path = 'report.xlsx'
df = pd.read_excel(excel_file_path, header=3)
df["개설전공"] = "기타"

# '학정번호' 열에서 NA/NaN 값을 가진 행을 무시하고 'GAI'로 시작하는 행의 '개설전공'을 '응용정보공학전공'으로 설정
df.loc[df["학정번호"].str.startswith("GAI", na=False), "개설전공"] = "응용정보공학전공"
# 'GBL'로 시작하는 경우 '바이오생활공학전공'으로 설정
df.loc[df["학정번호"].str.startswith("GBL", na=False), "개설전공"] = "바이오생활공학전공"
# 'GKE' 또는 'GKC'로 시작하거나 'GKE2404'인 경우 '한국어문화교육전공'으로 설정
df.loc[df["학정번호"].str.startswith("GKE", na=False) | df["학정번호"].str.startswith("GKC", na=False) | (df["학정번호"] == "GKE2404"), "개설전공"] = "한국어문화교육전공"
# 'GCM'으로 시작하는 경우 '문화미디어전공'으로 설정
df.loc[df["학정번호"].str.startswith("GCM", na=False), "개설전공"] = "문화미디어전공"
# 'GIC'로 시작하는 경우 '국제통상전공'으로 설정
df.loc[df["학정번호"].str.startswith("GIC", na=False), "개설전공"] = "국제통상전공"


# Filter out courses
df_filtered_과목종별_전기 = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == '전기') & (df['개설전공'] == read_major())]
df_filtered_과목종별_전선 = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == '전선') & (df['개설전공'] == read_major())]
df_filtered_과목종별_전필 = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == '전필') & (df['개설전공'] == read_major())]
df_filtered_과목종별_RC = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == 'RC')]
df_filtered_과목종별_GLC교양 = df[(~df['평가'].isin(['W', 'NP', 'F', 'U'])) & (df['과목 종별'] == '대교') & (df['학정번호'].str[:3] == 'GLC')]
df_filtered_과목종별_34000단위 = df[(~df['평가'].isin(['W', 'NP', 'F', 'U'])) & (df['학정번호'].str[3:5] == '3천, 4천 단위')]


# Define required credits for each category
required_credits_dict = {
    "국제통상전공": {"전공기초": 6, "전공선택": 42, "3-4000단위": 45},
    "한국어문화교육전공": {"전공필수": 42, "전공선택": 6, "3-4000단위": 45},
    "문화미디어전공": {"전공기초": 6, "전공선택": 42, "3-4000단위": 45},
    "바이오생활공학전공": {"전공기초": 18, "전공필수": 12, "전공선택": 24, "3-4000단위": 45},
    "응용정보공학전공": {"전공기초": 18, "전공필수": 12, "전공선택": 24, "3-4000단위": 45}
}

# Define 복수전공 (double major) requirements for each major
double_major_requirements = {
    "응용정보공학": {"1전공": {"전공기초": 9, "전공필수": 12, "전공선택": 15, "3-4000단위": 45},
                   "2전공": {"전공기초": 9, "전공필수": 12, "전공선택": 15}},
    "국제통상": {"1전공": {"전공기초": 6, "전공선택": 30, "3-4000단위": 45},
               "2전공": {"전공기초": 6, "전공선택": 30}},
    "바이오생활공학": {"1전공": {"전공기초": 9, "전공필수": 12, "전공선택": 15, "3-4000단위": 45},
                    "2전공": {"전공기초": 9, "전공필수": 12, "전공선택": 15}},
    "한국어문화교육": {"1전공": {"전공기초": 39, "전공필수": 6, "3-4000단위": 45},
                   "2전공": {"전공기초": 39, "전공필수": 6}},
    "문화미디어": {"1전공": {"전공기초": 6, "전공선택": 30, "3-4000단위": 45},
                 "2전공": {"전공기초": 6, "전공선택": 30}}
}

# Define 부전공 (minor) requirements for each major
minor_requirements = {
    "응용정보공학": {"전공기초": 6, "전공필수": 6, "전공선택": 9},
    "바이오생활공학": {"전공기초": 6, "전공필수": 6, "전공선택": 9}
    # Define for other majors if available...
}



common_subject = {
    "RC": 1, 
    "채플": 2,
    "기독교의 이해": 3,
    "GLC영어 0": 0,
    "GLC영어 1": 3,
    "GLC영어 2": 6,
    "GLC교양": 9,
}

required_credits = required_credits_dict[read_major()]

completed_credits = {
    "구분":"이수",
    "전기":int(df_filtered_과목종별_전기['학점'].sum()),
    "전선":int(df_filtered_과목종별_전선['학점'].sum()),
    "전필":int(df_filtered_과목종별_전필["학점"].sum()),
    "RC":int(df_filtered_과목종별_RC["학점"].sum()),
    "GLC교양":int(df_filtered_과목종별_GLC교양["학점"].sum()),
    "3~4000단위":int(df_filtered_과목종별_34000단위["학점"].sum()),
    # "completed_credits":(int(df_filtered_과목종별_전기['학점'].sum()) + 
    #                     int(df_filtered_과목종별_전선['학점'].sum()) +
    #                     int(df_filtered_과목종별_전필['학점'].sum())+
    #                     int(df_filtered_과목종별_RC["학점"].sum())+
    #                     int(df_filtered_과목종별_GLC교양["학점"].sum())
    #                     )
}

remaining_credits = {
    "구분":"필요",
    "전기": required_credits["전공기초"] - completed_credits["전기"],
    "전선": required_credits["전공선택"] - completed_credits["전선"],
    "전필": required_credits["전공필수"] - completed_credits["전필"],
    "RC": common_subject["RC"] - completed_credits["RC"],
    "GLC교양": common_subject["GLC교양"] - completed_credits["GLC교양"],
    "3-4000단위": required_credits["3-4000단위"] - completed_credits["3~4000단위"],
}

output_columns = {
    "구분":" ",
    "채플":common_subject["채플"],
    "기독교":common_subject["기독교의 이해"],
    "GLC 영어":1,
    "GLC교양":common_subject["GLC교양"],
    "RC필수":common_subject["RC"],
    "소계": (common_subject["채플"]+common_subject["기독교의 이해"]+common_subject["GLC교양"]+common_subject["RC"]),
    " ": " ",
    "전기":" ",
    "전선":" ",
    "전필":" ",
    "RC":" ",
    "GLC교양":" ",
    "3~4000단위":" ",
}


# Create a DataFrame for the output
output_df = pd.DataFrame([completed_credits,remaining_credits], columns=output_columns.keys()) #전체, 이수, 잔여
output_df = output_df.apply(lambda x: np.where(x < 0, 0, x) if x.dtype.kind in 'biufc' else x)

# Write to an Excel file
output_df.to_excel("result_file.xlsx", index=False)







# {common_subject, required_credits}

