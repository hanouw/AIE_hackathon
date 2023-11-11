import pandas as pd

class Major:
    def __init__(self, name, course_codes, required_credits):
        self.name = name
        self.course_codes = course_codes
        self.required_credits = required_credits
        self.completed_credits = 0

    def calculate_completed_credits(self, df):
        filtered_df = df[df['학정번호'].isin(self.course_codes) & ~df['평가'].isin(['W', 'NP', 'F', 'U'])]
        self.completed_credits = filtered_df['학점'].sum()

    def calculate_remaining_credits(self):
        return {category: self.required_credits[category] - self.completed_credits for category in self.required_credits}

# Load the Excel file
excel_file_path = 'report.xlsx'
df = pd.read_excel(excel_file_path, header=3)  # Adjust the header row as needed

# Define required credits for each category (common for all majors)
required_credits = {"전공기초": 20, "전공필수": 30, "전공선택": 15, "일반교양": 20, "교양기초": 10, "대학교양": 5, "공통기초": 10}

# Define the unique course codes for each major
majors = [
    Major("응용정보공학", ["APL101", "APL102", ...], required_credits),  # Replace with actual course codes
    Major("바이오생명공학", ["BIO201", "BIO202", ...], required_credits),  # Replace with actual course codes
    # Add other majors similarly
]

# Calculate completed and remaining credits for each major
for major in majors:
    major.calculate_completed_credits(df)
    remaining_credits = major.calculate_remaining_credits()

    # Create a DataFrame for the output
    output_df = pd.DataFrame(list(remaining_credits.items()), columns=["Category", "Remaining Credits"])

    # Write to an Excel file
    output_file_name = f"{major.name}_result_file.xlsx"
    output_df.to_excel(output_file_name, index=False)

    print(f"Results for {major.name} written to {output_file_name}")
