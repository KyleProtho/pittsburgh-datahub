
# Load necessary packages
import censusdata
import pandas as pd
import numpy as np 


def FetchCensusData():
    # Select variables of interest for county subdivision in Allegheny County, PA
    list_of_variables = [
        "COUSUB",  # FIPS of county subdivision
        "S0101_C01_001E",  # Total population
        "S0101_C01_002E",  # Under 5 years
        "S0101_C01_003E",  # 5 to 9 years
        "S0101_C01_004E",  # 10 to 14 years
        "S0101_C01_005E",  # 15 to 19 years
        "S0101_C01_006E",  # 20 to 24 years
        "S0101_C01_007E",  # 25 to 29 years
        "S0101_C01_008E",  # 30 to 34 years
        "S0101_C01_009E",  # 35 to 39 years
        "S0101_C01_010E",  # 40 to 44 years
        "S0101_C01_011E",  # 45 to 49 years
        "S0101_C01_012E",  # 50 to 54 years
        "S0101_C01_013E",  # 55 to 59 years
        "S0101_C01_014E",  # 60 to 64 years
        "S0101_C01_015E",  # 65 to 69 years
        "S0101_C01_016E",  # 70 to 74 years
        "S0101_C01_017E",  # 75 to 79 years
        "S0101_C01_018E",  # 80 to 84 years
        "S0101_C01_019E",  # 85 years and over
        "S0601_C01_048E",  # Population for whom poverty status is determined
        "S0102_C01_070E",  # Population 16 years and over in civilian labor force that is unemployed
        "S2801_C01_011E",  # No computer in household
        "S2801_C01_019E",  # No internet subscription
        "S2703_C02_001E",  # Civilian noninstitutionalized population with private health insurance
        "S2704_C02_001E",  # Civilian noninstitutionalized population with public health insurance
        "S0801_C01_009E",  # Workers 16 years and over that take public transportation to work
        "S2501_C01_001E",  # Occupied housing units
        "S2501_C01_002E",  # Occupied housing units - 1-person household
        "S2501_C01_003E",  # Occupied housing units - 2-person household
        "S2501_C01_004E",  # Occupied housing units - 3-person household
        "S2501_C01_005E",  # Occupied housing units - 4-person household
        "S2501_C04_001E",  # Percent of owner-occupied housing units
        "S2501_C06_001E",  # Percent of renter-occupied housing units
        "S2503_C04_024E",  # Median monthly housing costs
        "S2504_C01_005E",  # Occupied housing units with 3 or 4 apartment units in structure
        "S2504_C01_006E",  # Occupied housing units with 5 to 9 apartment units in structure
        "S2504_C01_007E",  # Occupied housing units with 10 or more apartment units in structure
        "S1501_C01_059E"  # Median earnings over past 12 months of population 25 years and over with earnings
    ]


    # Download data
    print("Retrieving socioeconomic data from the U.S. Census Bureau...")
    df_census_data = censusdata.download(
        src = 'acs5',
        year = 2018,
        geo = censusdata.censusgeo([('state', '42'), ('county', '003'), ('county subdivision', '*')]),
        var = list_of_variables,
        tabletype = 'subject'
    )  


    # Get name GEOIDs of county subdivisions
    print("Getting readable names of county subdivisions...")
    dict_cousub_reference = censusdata.geographies(
        within = censusdata.censusgeo([('state', '42'), ('county', '003'), ('county subdivision', '*')]),
        src = 'acs5',
        year = 2018
    ) 
    df_cousub_reference = pd.DataFrame(dict_cousub_reference.keys(),
                                    index = dict_cousub_reference.values()) 
    del dict_cousub_reference


    # Merge county subdivision names to dataframe of census data
    df_census_data = pd.merge(
        df_census_data,  # "Left" table
        df_cousub_reference,
        how = 'left',
        left_index = True,
        right_index = True
    )
    df_census_data = df_census_data.rename(
        columns = {0: "NAME"}
    )
    df_census_data = df_census_data.reset_index(drop = True)
    names = df_census_data["NAME"]
    df_census_data.drop(
        labels = ["NAME"], 
        axis = 1, 
        inplace = True
    )
    names = names.to_list()
    list_of_county_sub_names = []
    for name in names:
        name = name.split(", ")
        list_of_county_sub_names.append(name[0].title())
    del names
    df_census_data.insert(0, "NAME", list_of_county_sub_names)


    # Add county and state columns
    df_census_data.insert(2, "COUNTY", "Allegheny")
    df_census_data.insert(3, "STATE", "Pennsylvania")


    # Export as .csv and/or upload to server
    print("Socioeconomic data pull from Census completed! Primary key is county subdivision.")
    return df_census_data