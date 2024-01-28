def map_by_key(list_of_dicts, key_string):
  mapped_values = []
  for dictionary in list_of_dicts:
    if key_string in dictionary:
      value = dictionary[key_string]
      if isinstance(value, list):
        mapped_values.extend(value)
      else:
        mapped_values.append(value)

  return mapped_values

dict_list = [
    {"name": "John", "roles": ["admin", "user"]},
    {"name": "Jane", "roles": ["user"]},
]

result = map_by_key(dict_list, "roles")

print(result)
