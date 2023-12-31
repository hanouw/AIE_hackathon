import pandas as pd
import numpy as np

from read_major import read_major

# Filter out courses
df_filtered_과목종별_전기 = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == '전기') & (df['개설전공'] == read_major())]
df_filtered_과목종별_전선 = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == '전선') & (df['개설전공'] == read_major())]
df_filtered_과목종별_전필 = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == '전필') & (df['개설전공'] == read_major())]
df_filtered_과목종별_RC = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == 'RC')]
df_filtered_과목종별_GLC교양 = df[(~df['평가'].isin(['W', 'NP', 'F', 'U'])) & (df['과목 종별'] == '대교') & (df['학정번호'].str[:3] == 'GLC')]
df_filtered_과목종별_34000단위 = df[(~df['평가'].isin(['W', 'NP', 'F', 'U'])) & (df['학정번호'].str[3:5] == '3천, 4천 단위')]

# Define required credits for each category
required_credits_dict = {
    "국제통상전공": {"전공기초": 6, "전공선택": 42, "3-4000단위": 45, "GLC교양": 9},
    "한국어문화교육전공": {"전공필수": 42, "전공선택": 6, "3-4000단위": 45, "GLC교양": 9},
    "문화미디어전공": {"전공기초": 6, "전공선택": 42, "3-4000단위": 45, "GLC교양": 9},
    "바이오생활공학전공": {"전공기초": 18, "전공필수": 12, "전공선택": 24, "3-4000단위": 45, "GLC교양": 9},
    "응용정보공학전공": {"전공기초": 18, "전공필수": 12, "전공선택": 24, "3-4000단위": 45, "GLC교양": 9}
}

common_subject = {
    "RC": 1, 
    "채플": 2,
    "기독교의 이해": 3,
    "GLC영어 0": 0,
    "GLC영어 1": 3,
    "GLC영어 2": 6,
}

required_credits = required_credits_dict[read_major()]

def completed_credits():
    completed_credits_전기 = int(df_filtered_과목종별_전기['학점'].sum())
    completed_credits_전선 = int(df_filtered_과목종별_전선['학점'].sum())
    completed_credits_전필 = int(df_filtered_과목종별_전필["학점"].sum())
    completed_credits_RC = int(df_filtered_과목종별_RC["학점"].sum())
    completed_credits_GLC교양 = int(df_filtered_과목종별_GLC교양["학점"].sum())
    completed_credits_34000단위 = int(df_filtered_과목종별_34000단위["학점"].sum())
    completed_credits = (completed_credits_전기+
                        completed_credits_전선+ 
                        completed_credits_전필+ 
                        completed_credits_RC+
                        completed_credits_GLC교양)
    return completed_credits_전기, completed_credits_전선, completed_credits_전필, completed_credits_RC, completed_credits_GLC교양, completed_credits_34000단위, completed_credits


remaining_credits = {
    "전기": required_credits["전공기초"] - completed_credits_전기,
    "전선": required_credits["전공선택"] - completed_credits_전선,
    "전필": required_credits["전공필수"] - completed_credits_전필,
    "RC": common_subject["RC"] - completed_credits_RC,
    "GLC교양": required_credits["GLC교양"] - completed_credits_GLC교양,
    "3-4000단위": required_credits["3-4000단위"] - completed_credits_34000단위,
}

total_credits = {
    "전기": required_credits["전공기초"],
    "전선": required_credits["전공선택"],
    "전필": required_credits["전공필수"],
    "RC": common_subject["RC"],
    "GLC교양": required_credits["GLC교양"],
    "3-4000단위": required_credits["3-4000단위"],
}