import pandas as pd
from major_checker import read_major, get_additional_majors
from SingleMajor import single_major
from MultiMajor import multi_majors

if __name__ == "__main__":
    main_major = read_major()
    # print(main_major)
    major_list, minor_list, advanced_list= get_additional_majors()
    if (len(major_list) != 0):
        multi_majors(main_major,major_list, minor_list, advanced_list)
    else:
        single_major(main_major, minor_list, advanced_list)



