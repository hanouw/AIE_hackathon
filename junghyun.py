import pandas as pd
import numpy as np

# Assuming read_major and get_additional_majors are defined in these modules
from read_major import read_major
from major_checker import get_additional_majors

def calculate_credits(major_type, major_name, df, required_credits):
    # Function to calculate remaining credits for a major
    # Here you should implement the logic to calculate completed and remaining credits
    # based on the major type and the data frame
    # This is a placeholder function
    completed_credits = {}  # Replace with actual calculation
    remaining_credits = {}  # Replace with actual calculation
    return completed_credits, remaining_credits

# Fetch primary and additional major information
primary_major = read_major()
additional_majors_info = get_additional_majors()  # Expects a dict or list of major types and names

# Define required credits for each category for primary and additional majors
required_credits_dict = {
    # Define the required credits for each major
    # Example:
    "응용정보공학": {"전공기초": 18, "전공필수": 12, "전공선택": 24, "3-4000단위": 45},
    # Add other majors...
}

# Define 복수전공 and 부전공 requirements
double_major_requirements = {
    # Define double major requirements
    # Example:
    "응용정보공학": {"전공기초": 9, "전공필수": 12, "전공선택": 15},
    # Add other majors...
}
minor_requirements = {
    # Define minor requirements
    # Example:
    "응용정보공학": {"전공기초": 6, "전공필수": 6, "전공선택": 9},
    # Add other majors...
}

# Load the Excel file
excel_file_path = 'report.xlsx'
df = pd.read_excel(excel_file_path, header=3)

# Insert your logic to filter and categorize the courses based on '학정번호'
# Example:
# df.loc[df["학정번호"].str.startswith("GAI", na=False), "개설전공"] = "응용정보공학전공"
# ...

# Initialize containers for total credits
total_completed_credits = {}
total_remaining_credits = {}

# Calculate for primary major
primary_completed, primary_remaining = calculate_credits("1전공", primary_major, df, required_credits_dict[primary_major])
total_completed_credits.update(primary_completed)
total_remaining_credits.update(primary_remaining)

# Calculate for additional majors
for major_type, major_name in additional_majors_info.items():
    if major_type == "복수전공":
        required_credits = double_major_requirements.get(major_name, {})
    elif major_type == "부전공":
        required_credits = minor_requirements.get(major_name, {})
    else:  # Other types can be added here
        required_credits = {}

    completed, remaining = calculate_credits(major_type, major_name, df, required_credits)
    # Aggregate results
    for key in completed:
        total_completed_credits[key] = total_completed_credits.get(key, 0) + completed[key]
        total_remaining_credits[key] = total_remaining_credits.get(key, 0) + remaining[key]

# Ensure no negative remaining credits
total_remaining_credits = {k: max(v, 0) for k, v in total_remaining_credits.items()}

# Create a DataFrame for the output
output_df = pd.DataFrame([total_completed_credits, total_remaining_credits])

# Write to an Excel file
output_df.to_excel("result_file.xlsx", index=False)
