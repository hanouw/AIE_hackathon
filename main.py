import pandas as pd
from major_checker import read_major, get_additional_majors
from SingleMajor import SingleMajor

if __name__ == "__main__":
    main_major = read_major()
    print(main_major)
    get_additional_majors()


if __name__ == "__main__":
    analyze_major()
    
