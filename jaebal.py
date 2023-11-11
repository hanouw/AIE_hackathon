import pandas as pd
from major_checker import read_major, get_additional_majors

def multi_majors(main_major, major_list, minor_list, advanced_list):
    # Load the excel file and process it
    excel_file_path = 'report.xlsx'
    df = pd.read_excel(excel_file_path, header=3)
    # Process the DataFrame 'df' as per your existing logic

    # Define your existing dictionaries: required_credits_dict, double_major_requirements, etc.

    # Function to calculate credits for a given major
    def calculate_credits_for_major(major, requirements, df):
        # Initialize a dictionary to store completed credits
        completed_credits = {category: 0 for category in requirements.keys()}

        # Process each category in the requirements
        for category, required_credits in requirements.items():
            # Filter DataFrame for the current category and major
            df_filtered = df[(df['개설전공'] == major) & (df['과목 종별'] == category)]

            # Sum the credits for this category
            completed_credits[category] = df_filtered['학점'].sum()

        # Calculate remaining credits
        remaining_credits = {category: max(0, required_credits - completed)
                             for category, completed in completed_credits.items()}

        return completed_credits, remaining_credits

    # Process Primary Major (제 1 전공)
    primary_major_completed, primary_major_remaining = calculate_credits_for_major(
        main_major, required_credits_dict[main_major], df)

    # Process Secondary Majors (제 2 전공)
    secondary_major_results = {}
    for secondary_major in major_list:
        completed, remaining = calculate_credits_for_major(
            secondary_major, double_major_requirements[secondary_major], df)
        secondary_major_results[secondary_major] = {'completed': completed, 'remaining': remaining}

    # Combine and format results for output
    combined_results = {
        'Primary Major': {
            'Completed': primary_major_completed,
            'Remaining': primary_major_remaining
        },
        'Secondary Majors': secondary_major_results
    }

    # Output the final results (for example, printing or writing to an Excel file)
    # Example: print(combined_results)
    # You can modify this part to output the data as needed

# Example usage
if __name__ == "__main__":
    main_major = read_major()
    # print(main_major)
    major_list, minor_list, advanced_list= get_additional_majors()
    main_major = 'Your Main Major'
    major_list = ['Secondary Major 1', 'Secondary Major 2']  # Example secondary majors
    minor_list = []  # Example minor list
    advanced_list = []  # Example advanced majors list
    multi_majors(main_major, major_list, minor_list, advanced_list)
