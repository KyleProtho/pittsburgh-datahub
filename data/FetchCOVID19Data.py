
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
    item = GIS(verify_cert = False).content.get("a0a47e3bff754268b2c4316fff8cbb6b")
    flayer = item.layers[0]
    df_covid19_case_counts = pd.DataFrame.spatial.from_layer(flayer)
    df_covid19_case_counts = pd.DataFrame(df_covid19_case_counts)
    
    
    # Convert from spatial dataframe to normal dataframe
    df_covid19_case_counts = df_covid19_case_counts[["LABEL", "Join_Count"]]
    
    
    # Rename county subdivision name and count columns
    df_covid19_case_counts = df_covid19_case_counts.rename(
        columns = {"LABEL": "NAME",
                   "Join_Count": "Numberofcases"}
    )
    
    # Add last updated date
    print("Adding updated date...")
    today_date = date.today()
    df_covid19_case_counts["UpdatedDate"] = today_date
    df_covid19_case_counts["UpdatedDate"] = pd.to_datetime(df_covid19_case_counts["UpdatedDate"])
    
    
    # Add county and state columns
    df_covid19_case_counts["COUNTY"] = "Allegheny"
    df_covid19_case_counts["STATE"] = "Pennsylvania"
    
    
    # Export as .csv
    print("Exporting COVID-19 cases by county subdivision as .csv...")
    filename = str(today_date) + ".csv"
    filepath = path.join("C:\\Users\\oneno\\Documents\\GitHub\\pittsburgh-datahub\\data\\covid19", filename)
    df_covid19_case_counts.to_csv(filepath,
                                  index = False,
                                  header = True)
    
    print("COVID-19 case pull completed! Primary key determinants are Location and UpdatedDate")
    return df_covid19_case_counts
