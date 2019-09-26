import pandas as pd
import pickle

# display all columns
pd.set_option("display.max_columns", None)

# pull data from CSV to raw_data
raw_data = pd.read_csv("NY_HH_INCOME.csv", delimiter=',')

# extracting only relevant columns
raw_data = raw_data[['ZIP', 'COORDINATES', 'AVG_INC_HH']]

# splitting coordinates (str) into individual columns for Latitude & Longitude
raw_data[['LATITUDE', 'LONGITUDE']] = raw_data.COORDINATES.str.split(pat=', ', expand=True)

# converting strings to numeric values (floats)
raw_data.LATITUDE = pd.to_numeric(raw_data.LATITUDE, errors='coerce')
raw_data.LONGITUDE = pd.to_numeric(raw_data.LONGITUDE, errors='coerce')

# OPTIONAL: testing the dtypes for a value for each latitude and longitude
# number = raw_data.loc[5, 'LATITUDE']
# number2 = raw_data.loc[5, 'LONGITUDE']
# print(type(number), type(number2))

sorted_data = raw_data.sort_values(['AVG_INC_HH'], ascending=False)

top_10 = sorted_data.head(10)

print(top_10)

with open('top10income.pickle', 'wb') as to_write:
    pickle.dump(top_10, to_write)
