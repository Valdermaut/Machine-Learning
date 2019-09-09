Read and write CSV and XLS files
[ ]

import pandas as pd
df = pd.read_csv('weather_data.csv'df.to_csv('new.csv') )
df


[ ]

#INSTALL: pip3 install xlrd
​
#read excel file 
df = pd.read_excel('weather_data.xlsx')
df


[ ]

#write DF to csv
df.to_csv('new.csv') 
df.to_csv('new_noIndex.csv', index=False)
[ ]

# INSTALL: pip3 install openpyxl
​
#write DF to Excel
df.to_excel('new.xlsx', sheet_name='weather_data')
GROUP-BY
[ ]

import pandas as pd
df = pd.read_csv('weather_data_cities.csv')
df #weather by cities


[ ]

g = df.groupby('city')
g

[ ]

for city, city_df in g:
    print(city)
    print(city_df)


[ ]

#or to get specific group
g.get_group('new york')
​


[ ]

#Find maximum temperature in each of the cities
print(g.max())


[ ]

print(g.mean())
​


[ ]

print(g.describe())


Concatinate Data Frames
[ ]

import pandas as pd
india_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})
​
india_weather


[ ]

us_weather = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
})
us_weather


[ ]

#concate two dataframes
df = pd.concat([india_weather, us_weather])
df


[ ]

#if you want continuous index
df = pd.concat([india_weather, us_weather], ignore_index=True)
df


[ ]

df = pd.concat([india_weather, us_weather],axis=1)
df


Merge DataFrames
[ ]

temperature_df = pd.DataFrame({
    "city": ["mumbai","delhi","banglore", 'hyderabad'],
    "temperature": [32,45,30,40]})
temperature_df


[ ]

humidity_df = pd.DataFrame({
    "city": ["delhi","mumbai","banglore"],
    "humidity": [68, 65, 75]})
humidity_df


[ ]

#merge two dataframes with out explicitly mention index
df = pd.merge(temperature_df, humidity_df, on='city')
df


[ ]

#OUTER-JOIN
df = pd.merge(temperature_df, humidity_df, on='city', how='outer')
df


[ ]

