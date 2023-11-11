import pandas as pd

# Load the Excel file
df = pd.read_excel("path_to_file.xlsx")

# Define required credits for each category
required_credits = {"전공기초": 20, "전공필수": 30, ...}  # Fill in the correct numbers

# Calculate the sum of credits in each category
completed_credits = df.groupby("Category")["Credits"].sum()

# Calculate remaining credits
remaining_credits = {category: required_credits[category] - completed_credits.get(category, 0) for category in required_credits}

# Create a DataFrame for the output
output_df = pd.DataFrame(list(remaining_credits.items()), columns=["Category", "Remaining Credits"])

# Write to an Excel file
output_df.to_excel("remaining_credits.xlsx", index=False)
