from openpyxl import load_workbook

def read_major():
    excel_file_path = 'report.xlsx'
    workbook = load_workbook(excel_file_path)
    sheet = workbook['Table 1']
    df_major = sheet['L3'].value
    first_major = df_major[8:]
    return first_major


def get_additional_majors():
    additional_programs_count = input("Enter the number of 복수전공, 부전공, 심화전공 you have, separated by space (e.g., 1 0 1 for one 복수전공 and one 심화전공): ")
    counts = additional_programs_count.split()

    double_majors = []
    minors = []
    advanced_majors = []

    if len(counts) >= 1 and int(counts[0]) > 0:
        double_majors.extend([input(f"Enter 복수전공 {i+1}: ").strip() for i in range(int(counts[0]))])
    if len(counts) >= 2 and int(counts[1]) > 0:
        minors.extend([input(f"Enter 부전공 {i+1}: ").strip() for i in range(int(counts[1]))])
    if len(counts) >= 3 and int(counts[2]) > 0:
        advanced_majors.extend([input(f"Enter 심화전공 {i+1}: ").strip() for i in range(int(counts[2]))])

    return double_majors, minors, advanced_majors

if __name__ == "__main__":
    # Example usage
    primary_major = read_major()
    additional_majors_dict = get_additional_majors()

    # Accessing majors by type
    double_majors = additional_majors_dict["복수전공"]
    minors = additional_majors_dict["부전공"]
    advanced_majors = additional_majors_dict["심화전공"]

    print(double_majors)
    print(minors)
    print(advanced_majors)