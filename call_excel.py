import pandas as pd
import numpy as np

from read_major import read_major
from major_checker import get_additional_majors

def analyze_major():
    main_major = read_major()
    print(main_major)

    