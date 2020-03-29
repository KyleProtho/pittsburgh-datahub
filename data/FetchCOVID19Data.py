
# Load necessary packages
from arcgis import GIS
from arcgis.features import SpatialDataFrame
import pandas as pd
import numpy as np
from lxml import html
import requests
from datetime import date, timedelta
from os import path, mkdir


# Import dataframe of case counts from Allegheny County Department of Health
def FetchCOVID19Data():
    print("Retrieving COVID-19 case data from the Allegheny County Department of Health")
    item = GIS().content.get("e7fc66943d6f43bcba0c5d0294681d8d")
    flayer = item.layers[0]
    df_covid19_case_counts = pd.DataFrame.spatial.from_layer(flayer)


    # Add last updated date
    print("Adding updated date...")
    yesterday_date = date.today() - timedelta(days = 1)
    df_covid19_case_counts["UpdatedDate"] = yesterday_date
    df_covid19_case_counts["UpdatedDate"] = pd.to_datetime(df_covid19_case_counts["UpdatedDate"])


    # Export as .csv
    print("Exporting COVID-19 cases by county subdivision as .csv...")
    filename = str(yesterday_date) + ".csv"
    filepath = path.join("C:\\Users\\oneno\\Documents\\GitHub\\pittsburgh-datahub\\data\\covid19", filename)
    df_covid19_case_counts.to_csv(filepath,
                                  index = False,
                                  header = True)
    
    return df_covid19_case_counts