def mapping_name(dict):
  names = []
  for d in dict:
    if "name" in d:
       name = d["name"]
       names.append(name)
  return names


# Example

dict = [
    {"age": 17, "job": "unemployed"},
    {"name": "Brie", "age": 16, "job": "singer"},
    {"name": "Stan", "age": 50, "job": "doctor"},
]

print(mapping_name(dict))
# Output: ['A', 'Brie', 'Stan']