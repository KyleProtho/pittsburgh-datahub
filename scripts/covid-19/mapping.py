import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns

# Define read_shapefile function
def read_shapefile(sf):
    """
    Read a shapefile into a Pandas dataframe with a 'coords' 
    column holding the geometry information. This uses the pyshp
    package
    """
    fields = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps = [s.points for s in sf.shapes()]
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)
    return df


# Import shapefile
shp_path = "./././data/pa_cousub_2019_shapefiles/tl_2019_42_cousub.shp"
sf = shp.Reader(shp_path)


# Create spatial dataframe from shapefile and filter to subdivisions in Allegheny County 
df = read_shapefile(sf)
df = df[df["COUNTYFP"]=="003"]
df["NAMELSAD"] = df["NAMELSAD"].str.title()