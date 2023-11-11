import pandas as pd

class Major:
    def __init__(self, name, required_credits=None, course_numbers=None):
        self.name = name
        self.required_credits = required_credits if required_credits else {}
        self.course_numbers = course_numbers if course_numbers else {}

    def calculate_remaining_credits(self, completed_courses):
        completed_credits = {category: 0 for category in self.required_credits}

        for course in completed_courses:
            if course['평가'] not in ['NP', 'F', 'W']:
                for category, numbers in self.course_numbers.items():
                    if course['학정번호'] in numbers:
                        completed_credits[category] += course['학점']
                        break

        remaining_credits = {category: self.required_credits[category] - completed_credits[category]
                             for category in self.required_credits}

        return remaining_credits

# Read the Excel file into a DataFrame
excel_file_path = 'report.xlsx'
df = pd.read_excel(excel_file_path)

# Convert DataFrame rows into a list of dictionaries
completed_courses = df.to_dict('records')

# Example: Create an instance for the 응용정보공학 major
# Fill in the actual required credits and course numbers for this major
응용정보공학 = Major("응용정보공학", {"전공기초": 20, "전공필수": 30, ...}, {"전공기초": ["COURSE001", "COURSE002", ...], ...})

# Calculate remaining credits for a student in the 응용정보공학 major
remaining_credits = 응용정보공학.calculate_remaining_credits(completed_courses)

# Output the results
print(f"Remaining Credits for {응용정보공학.name}: {remaining_credits}")
