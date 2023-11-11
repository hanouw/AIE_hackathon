import pandas as pd
import numpy as np

from major_checker import get_additional_majors

major_list, minor_list, advanced_list = get_additional_majors()

def single_major(main_major):
    
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
    df_filtered_과목종별_전기 = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == '전기') & (df['개설전공'] == main_major)]
    df_filtered_과목종별_전선 = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == '전선') & (df['개설전공'] == main_major)]
    df_filtered_과목종별_전필 = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == '전필') & (df['개설전공'] == main_major)]
    df_filtered_과목종별_RC = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == 'RC') & df['교과목명'].str.startswith("YONSEI", na=False)]
    df_filtered_과목종별_GLC교양 = df[(~df['평가'].isin(['W', 'NP', 'F', 'U'])) & (df['과목 종별'] == '대교') & (df['학정번호'].str[:3] == 'GLC')]
    df_filtered_과목종별_34000단위 = df[(~df['평가'].isin(['W', 'NP', 'F', 'U'])) & (df['학정번호'].str[3:5] == '3천, 4천 단위')]
    df_filtered_과목종별_채플 = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['학정번호'].str[:3] == 'YCA') & (df['과목 종별'] == '공기')]
    df_filtered_과목종별_기독교의이해 = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['학정번호'].str[:3] == 'YCA') & (df['과목 종별'] == '교기')]
    df_filtered_과목종별_GLC영어 = df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['학정번호'].str[:3] == 'GLC') & (df['과목 종별'] == '교기')]

    def GLC영어_학점():
        #GLC영어 이수 유무
        GLC영어_학점 = 6

        # GLC영어1 과목을 찾고, 그 학점이 0인지 확인 후, 조건이 참이면 GLC영어_학점에서 3을 뺍니다.
        if ((df['교과목명'] == 'GLC영어1') & (df['학점'] == 0)).any():
            GLC영어_학점 -= 3

        # GLC영어2 과목을 찾고, 그 학점이 0인지 확인 후, 조건이 참이면 GLC영어_학점에서 3을 뺍니다.
        if ((df['교과목명'] == 'GLC영어2') & (df['학점'] == 0)).any():
            GLC영어_학점 -= 3
        return GLC영어_학점

    # Define required credits for each category
    required_credits_dict = {
        "국제통상전공": {"전공기초": 6, "전공선택": 42, "3-4000단위": 45},
        "한국어문화교육전공": {"전공필수": 42, "전공선택": 6, "3-4000단위": 45},
        "문화미디어전공": {"전공기초": 6, "전공선택": 42, "3-4000단위": 45},
        "바이오생활공학전공": {"전공기초": 18, "전공필수": 12, "전공선택": 24, "3-4000단위": 45},
        "응용정보공학전공": {"전공기초": 18, "전공필수": 12, "전공선택": 24, "3-4000단위": 45}
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

    required_credits = required_credits_dict[main_major]

    completed_credits = {
        "구분":"이수",
        "채플":int(df_filtered_과목종별_채플['학점'].sum()),
        "기독교의 이해":int(df_filtered_과목종별_기독교의이해['학점'].sum()),
        "GLC영어": int(df_filtered_과목종별_GLC영어['학점'].sum()),
        "GLC교양":int(df_filtered_과목종별_GLC교양['학점'].sum()),
        "RC":int(df_filtered_과목종별_RC['학점'].sum()),
        "소계": int(df_filtered_과목종별_채플["학점"].sum()+
                df_filtered_과목종별_기독교의이해['학점'].sum()+
                df_filtered_과목종별_GLC영어['학점'].sum()+
                df_filtered_과목종별_GLC교양['학점'].sum()+
                df_filtered_과목종별_RC['학점'].sum()),
        " ":" ",
        "전기":int(df_filtered_과목종별_전기['학점'].sum()),
        "전필":int(df_filtered_과목종별_전필["학점"].sum()),
        "전선":int(df_filtered_과목종별_전선['학점'].sum()),
        "GLC교양":int(df_filtered_과목종별_GLC교양["학점"].sum()),
        "3-4000단위":int(df_filtered_과목종별_34000단위["학점"].sum()),
    }


    total_credits = {
        "구분":"요건",
        "GLC영어": GLC영어_학점(),
        "채플":common_subject["채플"],
        "기독교의 이해":common_subject["기독교의 이해"],
        "GLC교양":common_subject["GLC교양"],
        "RC":common_subject["RC"],
        "소계": (common_subject["채플"]+
            common_subject["기독교의 이해"]+
            common_subject["GLC교양"]+
            common_subject["RC"])+
            GLC영어_학점(),
        " ":" ",
        "전기": required_credits["전공기초"],
        "전필": required_credits["전공필수"],
        "전선": required_credits["전공선택"],
        "GLC교양": common_subject["GLC교양"],
        "3-4000단위": required_credits["3-4000단위"],
    }

    remaining_credits = {
        "구분":"필요",
        "채플":common_subject["채플"] - completed_credits["채플"],
        "기독교의 이해":common_subject["기독교의 이해"] - completed_credits["기독교의 이해"],
        "GLC영어": GLC영어_학점() - completed_credits["GLC영어"],
        "GLC교양":common_subject["GLC교양"] - completed_credits["GLC교양"],
        "RC":common_subject["RC"] - completed_credits["RC"],
        "소계": (common_subject["채플"] - completed_credits["채플"]+
            common_subject["기독교의 이해"] - completed_credits["기독교의 이해"]+
            GLC영어_학점() - completed_credits["GLC영어"]+
            common_subject["GLC교양"] - completed_credits["GLC교양"]+
            common_subject["RC"] - completed_credits["RC"]),
        " ":" ",
        "전기": required_credits["전공기초"] - completed_credits["전기"],
        "전필": required_credits["전공필수"] - completed_credits["전필"],
        "전선": required_credits["전공선택"] - completed_credits["전선"],
        "GLC교양": common_subject["GLC교양"] - completed_credits["GLC교양"],
        "3-4000단위": required_credits["3-4000단위"] - completed_credits["3-4000단위"],
    }

    output_columns = {
        "구분":" ",
        "채플":common_subject["채플"],
        "기독교의 이해":common_subject["기독교의 이해"],
        "GLC영어":" ",
        "GLC교양":common_subject["GLC교양"],
        "RC":common_subject["RC"],
        "소계": (common_subject["채플"]+common_subject["기독교의 이해"]+common_subject["GLC교양"]+common_subject["RC"]),
        " ": " ",
        "전기":" ",
        "전선":" ",
        "전필":" ",
        "GLC교양":" ",
        "3-4000단위":" ",
    }

    minor_requirements = {
    "응용정보공학": {"전공기초": 6, "전공필수": 6, "전공선택": 9},
    "바이오생활공학": {"전공기초": 6, "전공필수": 6, "전공선택": 9},
    "문화미디어": {"전공기초": 6, "전공필수": 0, "전공선택": 15},
    "국제통상": {"전공기초": 6, "전공필수": 6, "전공선택": 9},
    "한국어문화교육": {"전공기초": 6, "전공필수": 6, "전공선택": 9},
    }

    if len(minor_list) == 0 and len(advanced_list) == 0:
        output_df = pd.DataFrame([total_credits, completed_credits, remaining_credits], columns=output_columns.keys())
    else:
        # 먼저 output_df 초기화
        output_df = pd.DataFrame([total_credits, completed_credits, remaining_credits], columns=output_columns.keys())

        # 그 다음, minor_list를 순회하며 새로운 열 추가
        for a in minor_list:
            output_df.insert(len(output_columns), " ", " ", allow_duplicates=True)
            output_df[f"{a} 부전공 전기"] = minor_requirements[a]["전공기초"] - \
                df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == '전기') & (df['개설전공'] == a)].sum()
            output_df[f"{a} 부전공 전필"] = minor_requirements[a]["전공필수"] - \
                df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == '전필') & (df['개설전공'] == a)].sum()
            output_df[f"{a} 부전공 전선"] = minor_requirements[a]["전공선택"] - \
                df[~df['평가'].isin(['W', 'NP', 'F', 'U']) & (df['과목 종별'] == '전선') & (df['개설전공'] == a)].sum()

    # 모든 수정 사항 반영 후 DataFrame을 Excel 파일로 저장
    output_df = output_df.apply(lambda x: np.where(x < 0, 0, x) if x.dtype.kind in 'biufc' else x)
    output_df.to_excel("result_file.xlsx", index=False)

