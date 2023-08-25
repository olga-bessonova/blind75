# Write a function map_by_key that takes an list of dictionaries and a key string. 
# The function should return a new list containing the values from each dictionary for the given key.

def map_by_key(dict_list, key):
    # res = []
    # for el in dict_list:
    #     res.append(el[key])
    # return res
  return [x[key] for x in dict_list]
    
locations = [
  {"city": "New York City", "state": "New York", "coast": "East"},
  {"city": "San Francisco", "state": "California", "coast": "West"},
  {"city": "Portland", "state": "Oregon", "coast": "West"},
]

print(map_by_key(locations, "state")) #["New York", "California", "Oregon"]
print(map_by_key(locations, "city")) #["New York City", "San Francisco", "Portland"]