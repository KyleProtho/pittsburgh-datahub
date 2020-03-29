
# Load necessary packages
from arcgis import GIS
from arcgis.features import SpatialDataFrame
import pandas as pd
import numpy as np
from datetime import date, timedelta
from os import path, mkdir


# Import dataframe of case counts from Allegheny County Department of Health
def FetchCOVID19Data():
    print("Retrieving COVID-19 case data from the Allegheny County Department of Health...")
    item = GIS().content.get("e7fc66943d6f43bcba0c5d0294681d8d")
    flayer = item.layers[0]
    df_covid19_case_counts = pd.DataFrame.spatial.from_layer(flayer)
    df_covid19_case_counts = pd.DataFrame(df_covid19_case_counts)


    # Add last updated date
    print("Adding updated date...")
    today_date = date.today()
    df_covid19_case_counts["UpdatedDate"] = today_date
    df_covid19_case_counts["UpdatedDate"] = pd.to_datetime(df_covid19_case_counts["UpdatedDate"])


    # Export as .csv
    print("Exporting COVID-19 cases by county subdivision as .csv...")
    filename = str(today_date) + ".csv"
    filepath = path.join("C:\\Users\\oneno\\Documents\\GitHub\\pittsburgh-datahub\\data\\covid19", filename)
    df_covid19_case_counts.to_csv(filepath,
                                  index = False,
                                  header = True)
    
    print("COVID-19 case pull completed! Primary key determinants are Location and UpdatedDate")
    return df_covid19_case_counts