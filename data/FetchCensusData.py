
# Load necessary packages
import censusdata
import pandas as pd
import numpy as np 


# Select variables of interest
# Search for ACS 2011-2015 5-year estimate variables where the specific variable label includes the text 'unemploy'.
results = censusdata.search('acs5', 2018, 'label', 'population')
for result in results:
    index = 0
    print(str(index) + ":", result)
    index += 1