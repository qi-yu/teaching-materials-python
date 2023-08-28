# mydict = {"x": [1, 2],
#           "y": [3, 4],
#           "z": [5, 6]}

# all_keys = ["x", "y", "z"]
# mydict[all_keys] =  [1, 2, 3, 4, 5, 6]
## The lines above don't work:
## List is a mutable type, but dictionary keys should be of immutable type


# On the contrary, this works:
# all_keys = ("x", "y", "z")
# mydict[all_keys] =  [1, 2, 3, 4, 5, 6]
# print(mydict)
# Reason: Tuple is a immutable type