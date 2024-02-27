import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# 1. Show first 5 rows.
df = pd.read_csv("world_happiness_report.csv")
print(df.head())

# 2. Display data types of all columns.
df.info()

# # 3. What country has the highest 'GDP per capita'?
# print(df['GDP per capita'].value_counts().sort_index())
# # Replace na and '-' to missing value.
# df['GDP per capita'] = df['GDP per capita'].replace(['-', 'na'], [None, None])
# df['GDP per capita'] = pd.to_numeric(df['GDP per capita'], errors='coerce')
# print(df['GDP per capita'].describe())

# print(df['Country or region'].value_counts().sort_index())
# df['Country or region'] = df['Country or region'].replace(['_switzerland', 'switzerland'],'Switzerland')
# print(df['Country or region'].value_counts().sort_index())

# max_gdp = df['GDP per capita'].max()
# print('max_gdp: ', max_gdp)
# print(df.loc[df['GDP per capita'] == max_gdp, 'Country or region'])

# 4. What's the average score of happiness in Switzerland?
# Assuming 'df' is your DataFrame
average_score_switzerland = df[df['Country or region'] == 'Switzerland']['Score of Happiness'].mean()
print("Average Score of Happiness in Switzerland:", average_score_switzerland)

# 5. Display 'Score of Happiness' for every year for Norway sorted by year. What's the trend of happiness of Norway?
df = df.rename(columns={' year': 'year'})
print(df['year'].value_counts())

format1 = "%b-%y"
format2 = "%Y"

error_dates = []
for i in range(df.shape[0]):
    date_string = df.iloc[i]['year']
    try:
        parsed_date = datetime.strptime(date_string, format1)
    except ValueError:
        try:
            parsed_date = datetime.strptime(date_string, format2)
        except ValueError:
            error_dates.append(i)
            continue 
    # Add converted date column 
    df.at[i, 'converted_year'] = parsed_date

print("error_dates: ", error_dates)
df['converted_year'] = df['converted_year'].dt.year
print(df['converted_year'].value_counts())
print(df.head())

norway = df[df['Country or region'] == 'Norway']
print(norway.sort_values(by='converted_year'))

plt.figure(figsize=(10, 6))
plt.bar(norway['converted_year'], norway['Score of Happiness'], color='skyblue')
plt.xlabel('Year')
plt.ylabel('Score of Happiness')
plt.title('Happiness Score in Norway Over the Years')
plt.show()


# data = {
#     'Country or region': ['Norway', 'Norway', 'Norway', 'Norway', 'Norway'],
#     'Score of Happiness': [7.522, 7.498, 7.537, 7.594, 7.554],
#     'year': [2015, 2016, 2017, 2018, 2019]
# }