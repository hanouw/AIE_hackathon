import pandas as pd
import numpy as np

from major_checker import read_major, get_additional_majors

def analyze_major():
    main_major = read_major()
    print(main_major)
    get_additional_majors()


if __name__ == "__main__":
    analyze_major()