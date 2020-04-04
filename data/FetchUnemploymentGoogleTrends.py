
# Import packages
from pytrends.request import TrendReq

# Log into Google
pytrend = TrendReq(
    hl = 'en-US',
    tz = 360
)

# Define unployment phrase list
unemployment_phrase_list = ["file for unemployment"]

# Fetch Google trends data for Pennsylvania regions
pytrend.build_payload(
    unemployment_phrase_list, 
    cat = 0, 
    timeframe = 'today 12-m', 
    geo = 'US-PA'
)

# Interest Over Time
print("Fetching unemployment-related Google search volume over time...")
interest_over_time_df = pytrend.interest_over_time()

# Interest by Region
print("Fetching unemployment-related Google search volume by region...")
interest_by_region_df = pytrend.interest_by_region()