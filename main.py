from data.FetchPittsburghArrestData import FetchPittsburghArrestData
from data.FetchCOVID19Data import FetchCOVID19Data
from data.FetchCensusData import FetchCensusData

# Get Pittsburgh arrest data
df_PIT_arrests = FetchPittsburghArrestData()
df_PIT_covid19 = FetchCOVID19Data()
df_PIT_census = FetchCensusData()
