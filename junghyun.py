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

def extract_major(소속):
    if '대학' in 소속 and '전공' in 소속:
        start = 소속.find('대학') + len('대학')
        end = 소속.find('전공')
        return 소속[start:end].strip()
    return None

# Load the Excel file
excel_file_path = 'report.xlsx'
df = pd.read_excel(excel_file_path)

# Extract the student's major
student_major_info = df.iloc[1]['소속']  # Assuming the major is in the second row
student_major = extract_major(student_major_info)

# Course data starts from the third row onward
course_data = df.iloc[2:]

# Define unique required credits for each major
# ...

# Define the unique course codes for each major
# ...

# Find the Major object for the student's major
major_obj = majors_dict.get(student_major)
if not major_obj:
    raise ValueError("Major not found in the defined majors")

# Calculate completed and remaining credits for the student's major
major_obj.calculate_completed_credits(course_data)
remaining_credits = major_obj.calculate_remaining_credits()

# Create a DataFrame for the output
output_df = pd.DataFrame(list(remaining_credits.items()), columns=["Category", "Remaining Credits"])

# Write to an Excel file
output_file_name = f"{major_obj.name}_result_file.xlsx"
output_df.to_excel(output_file_name, index=False)

print(f"Results for {major_obj.name} written to {output_file_name}")
