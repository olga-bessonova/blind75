import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

# 1. Show first 5 rows.
df = pd.read_csv("house_imdb.csv", skiprows=9)
print(df.head())

# 2. Display data types of all columns.
df.info()

# 3. Find and display how many episodes each season has, ordered by the column 'season'.
print(df['season'].value_counts())
# Replace variations of '4' in 'season' column
df['season'] = df['season'].replace(['4Season', '4 Season'], '4')
print(df['season'].value_counts().sort_index())

# 4. Find and disply average imdb_rating for every season. Make a scatter plot and bar plot to reflect the trend.
print(df['imdb_rating'].value_counts())
# the data has 3 missing imdb ratings. Remove '-' and convert to numeric:
df['imdb_rating'] = pd.to_numeric(df['imdb_rating'], errors='coerce')
# df_filtered = df[df['imdb_rating'] != '-']
print(df['imdb_rating'].describe())
average_imdb_rating = df.groupby('season')['imdb_rating'].mean().reset_index(name='average_imdb_rating')
print(average_imdb_rating)
# Bar Plot
plt.figure(figsize=(8, 5))
plt.bar(average_imdb_rating['season'], average_imdb_rating['average_imdb_rating'], color='blue', alpha=0.7)
plt.xlabel('Season')
plt.ylabel('Average IMDb Rating')
plt.title('Average IMDb Rating by Season (Bar Plot)')
plt.show()

# Scatter Plot with Line
plt.figure(figsize=(8, 5))
plt.scatter(df['season'], df['imdb_rating'], color='green', alpha=0.7, label='Individual Ratings')
plt.plot(average_imdb_rating['season'], average_imdb_rating['average_imdb_rating'], color='red', linewidth=2, label='Average Rating Line')
plt.xlabel('Season')
plt.ylabel('IMDb Rating')
plt.title('IMDb Ratings by Season (Scatter Plot with Line)')
plt.legend()
plt.show()

# 5. Using the column 'original_air_date' find how many episodes were released each year.
# Convert original_air_date to date type:
print(df['original_air_date'].value_counts())
format1 = "%d %b. %Y"
format2 = "%d-%b-%y"
format3 = "%m/%d/%Y"

error_dates = []
for i in range(df.shape[0]):
    date_string = df.iloc[i]['original_air_date']
    try:
        parsed_date = datetime.strptime(date_string, format1)
    except ValueError:
        try:
            parsed_date = datetime.strptime(date_string, format2)
        except ValueError:
            try:
                parsed_date = datetime.strptime(date_string, format3)
            except ValueError:
                error_dates.append(i)
                continue 
    # Add converted date column 
    df.at[i, 'converted_date'] = parsed_date

print("error_dates: ", error_dates)

df.info()
print('=='*20)
print(df.head())
# Extract YEAR for every row
df['year'] = df['converted_date'].dt.year
print(df['year'].describe())
print(df.head())
# Group by 'year' and get the count of rows for each year
year_result = df.groupby('year').size().reset_index(name='count')

# Sort the year_result by 'year'
year_result = year_result.sort_values('year')

# Print the year_result
print("=="*20)
print(year_result)
