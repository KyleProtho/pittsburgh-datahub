
# Load necessary packages and functions
import pandas as pd
import numpy as np

def FetchPittsburghArrestData(): 
    # Import data from Western Pennsylvania Regional Data Center
    print("Importing arrest data from the Western Pennsylvania Regional Data Center...")
    df_arrest_data = pd.read_csv("https://data.wprdc.org/datastore/dump/e03a89dd-134a-4ee8-a2bd-62c40aeebc6f")


    # Format dataframe
    ## Covert arrest time to a timestamp data type
    print("Converting ARRESTTIME to a timestamp...")
    df_arrest_data["ARRESTTIME"] = df_arrest_data["ARRESTTIME"].str.replace('T',' ')
    df_arrest_data["ARRESTTIME"] = pd.to_datetime(df_arrest_data["ARRESTTIME"])
    ## Remove records with no offenses
    print("Removing records with no offenses...")
    df_arrest_data = df_arrest_data.dropna(subset=["OFFENSES"])
    ## Ensure that offenses are separated into their own row (normalize table)
    print("Normalizing arrest data table by separating list of offenses...")
    ### Start by separating out rows that need adjusted, which should ones where OFFENSES column has ' / ' in it
    df_multiple_offense_arrests = df_arrest_data[df_arrest_data["OFFENSES"].str.contains(" / ", regex = False)]
    df_arrest_data = df_arrest_data[~df_arrest_data["OFFENSES"].str.contains(" / ", regex = False)]
    ### Explode dataframe multiple offense records...
    df_multiple_offense_arrests["OFFENSES"] = df_multiple_offense_arrests["OFFENSES"].str.split(" / ").tolist()
    df_multiple_offense_arrests = df_multiple_offense_arrests.explode("OFFENSES")
    ### Append arrest records back together now that they are normalized
    df_arrest_data = df_arrest_data.append(df_multiple_offense_arrests)
    del df_multiple_offense_arrests
    ## Sort by arrest time in descending order
    df_arrest_data = df_arrest_data.sort_values(by = "ARRESTTIME",
                                                ascending = False)
    print("Table normalized! Primary key determinants are ARRESTTIME, ARRESTLOCATION, and OFFENSES")


    # Export to .csv and/or server
    return df_arrest_data
