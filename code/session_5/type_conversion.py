# ----- 1. list() -----
# names = ("Dr. Cat", "Anna", "Eva")
# print(type(names))
#
# names = list(names)
# print(names)
# print(type(names))

## Now you have converted the tuple to a list,
## And all list methods are now applicable:
# names[0] = "Prof. Dr. Cat"
# print(names)

# ----- 2. tuple() -----
# names = ["Dr. Cat", "Anna", "Eva"]
# names = tuple(names)
# print(names)

## Now you have converted the list to a tuple.
## It is now immutable: The following line will invoke an error.
# names[0] = "Prof. Dr. Cat"

# ----- 3. tuple() and list() can be used to any interable types: -----
# name = "Anna"
# print(tuple(name))
# print(list(name))

# numbers = range(10)
# print(tuple(numbers))
# print(list(numbers))
