dict1 = {"x": 1, "y": 2, "z": 3}
dict2 = {"x": 4, "y": 5, "z": 6}


# ----- Method 1 -----
# We know that both dictionaries have the same keys.
# So we can just get all keys from one of the two dictionaries,
# and use these keys to retrieve the values.

# for k in dict1.keys():
#     print(dict1[k] + dict2[k])

# ----- Method 2 -----
# values1 = list(dict1.values())
# values2 = list(dict2.values())
#
# for i in range(0, len(values1)):
#     print(values1[i] + values2[i])
