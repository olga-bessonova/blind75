# Write a function map_by_name that takes in an list of dictionaries and 
# returns a new list containing the names of each dictionary.

def map_by_name(dict_list):
    return list(map(lambda x: x['name'], dict_list ))
    # return ([x["name"] for x in dict_list])


pets = [
  {"type": "dog", "name": "Rolo"},
  {"type": "cat", "name": "Sunny"},
  {"type": "rat", "name": "Saki"},
  {"type": "dog", "name": "Finn"},
  {"type": "cat", "name": "Buffy"}
]

print(map_by_name(pets))
#['Rolo', 'Sunny', 'Saki', 'Finn', 'Buffy']

countries = [
 {"name": "Japan", "continent": "Asia"},
 {"name": "Hungary", "continent": "Europe"},
 {"name": "Kenya", "continent": "Africa"},
]

print(map_by_name(countries))
#['Japan', 'Hungary', 'Kenya']