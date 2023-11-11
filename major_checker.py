import pandas as pd
import numpy as np

from read_major import read_major


def get_additional_majors():
    additional_programs_count = input("Enter the number of 복수전공, 부전공, 심화전공 you have, separated by space (e.g., 1 0 1 for one 복수전공 and one 심화전공): ")
    counts = additional_programs_count.split()

    majors_dict = {"복수전공": [], "부전공": [], "심화전공": []}
    if len(counts) >= 1 and int(counts[0]) > 0:
        majors_dict["복수전공"].extend([input(f"Enter 복수전공 {i+1}: ").strip() for i in range(int(counts[0]))])
    if len(counts) >= 2 and int(counts[1]) > 0:
        majors_dict["부전공"].extend([input(f"Enter 부전공 {i+1}: ").strip() for i in range(int(counts[1]))])
    if len(counts) >= 3 and int(counts[2]) > 0:
        majors_dict["심화전공"].extend([input(f"Enter 심화전공 {i+1}: ").strip() for i in range(int(counts[2]))])

    double_majors = additional_majors_dict["복수전공"]
    minors = additional_majors_dict["부전공"]
    advanced_majors = additional_majors_dict["심화전공"]
    return majors_dict, double_majors, minors, advanced_majors

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