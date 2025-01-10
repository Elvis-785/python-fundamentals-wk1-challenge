def merge_dicts(dict1, dict2):
    merged_dict = {}

    # Add all key-value pairs from the dict1 to merged_dict
    for key, value in dict1.items():
        merged_dict[key] = value

    # Add all key-value pairs from the dict2 to merged_dict
    for key, value in dict2.items():
        if key in merged_dict:
            # If the key is already in the merged dict, add the values
            merged_dict[key] += value
        else:
            # If the key is not in the merged dict, add the key-value pair
            merged_dict[key] = value

    return merged_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2)) 
