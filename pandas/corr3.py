import pandas as pd

# Create the students hashtable as a pandas DataFrame
students = pd.DataFrame({
    'name': ['John', 'Jane', 'Peter', 'Susan', 'Michael'],
    'grades': [85, 90, 75, 80, 95],
    'hours_studied': [5, 7, 3, 4, 8]
})

# Print the students DataFrame
print(students)

# Calculate the correlation between grades and number of hours studied
correlation = students['grades'].corr(students['hours_studied'])

# Print the correlation
print(correlation)
print([85, 90, 75, 80, 95].corr([5, 7, 3, 4, 8]))