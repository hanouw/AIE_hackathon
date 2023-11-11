import pandas as pd
from major_checker import read_major, get_additional_majors
from SingleMajor import single_major
from MultiMajor import multi_majors

if __name__ == "__main__":
    main_major = read_major()
    print(main_major)
    major_list, minor_list, advanced_list = get_additional_majors()
    multi_majors(main_major, major_list, minor_list, advanced_list)
    single_major(main_major)



