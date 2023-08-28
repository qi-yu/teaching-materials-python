# ----- 1. Add elements -----
## 1.1 .append()
# employee_names = [] # Construct an empty list
# print(employee_names)
# employee_names.append("Dr. Cat")
# print(employee_names)
# employee_names.append("Anna")
# print(employee_names)

## 1.2 .insert()
# employee_names = ["Dr. Cat", "Anna", "Eva"]
# employee_names.insert(1, "Kate")
# print(employee_names)

## Note that the index marks the boundary
## (Recall Dawson's figure 4.10 about the position numbering system for slicing - It is the same system here)
# employee_names.insert(-1, "Bob")
# print(employee_names)

# ----- 2. Remove elements -----
## 2.1 .remove()
# employee_names = ["Dr. Cat", "Anna", "Eva", "Kate"]
# employee_names.remove("Dr. Cat")
# print(employee_names)

## Note that if an element occurs more than one time in a list,
## .remove() will only remove the first occurence.
# employee_names = ["Dr. Cat", "Anna", "Dr. Cat", "Eva", "Kate"]
# employee_names.remove("Dr. Cat")
# print(employee_names)

## 2.2 .pop()
## 2.2.1 If no argument passed to .pop(), the last element will be removed
# employee_names = ["Dr. Cat", "Anna", "Eva", "Kate"]
# employee_names.pop()
# print(employee_names)

## 2.2.1 .pop() can also take an index as an argument.
## It will then remove the element with the corresponding index.
# employee_names = ["Dr. Cat", "Anna", "Eva", "Kate"]
# employee_names.pop(2)
# print(employee_names)


# ----- 3. Operate on the order of elements -----
## 3.1 .sort()
# employee_names = ["Dr. Cat", "Anna", "Eva"]
# print("Original list:", employee_names)
# employee_names.sort()
# print("Sorted list:", employee_names)

## Note that in the above lines you don't need to re-assign the sorted value back to the variable by using "employee_names = employee_names.sort()".
## The method ".sort()" operates directly on the value.
## Instead, if you do this, you'll get a None value back - You can try this out with the following lines:
# employee_names = ["Dr. Cat", "Anna", "Eva"]
# employee_names = employee_names.sort()
# print(employee_names)


## Using the argument "reverse=True", you can sort the list in descending order.
## The default value of the argument "reverse" is "False".
# employee_names = ["Dr. Cat", "Anna", "Eva"]
# print("Original list:", employee_names)
# employee_names.sort(reverse=True)
# print("Sorted list:", employee_names)

## 3.2 .reverse()
# employer_names = ["Dr. Cat", "Anna", "Eva", "Kate"]
# employer_names.reverse()
# print(employer_names)


# ----- 4. .count() : Count the occurrence of a certain element -----
# names = ["Dr. Cat", "Anna", "Eva", "Anna", "Anna", "Kate", "Dr. Cat"]
# print(names.count("Anna"))
# print(names.count("Kate"))
# print(names.count("Bob")) # Note that .count() will return 0 if the element is not in the list

# ----- 5. .index() : returns the index of the first occurrence of the element.-----
# names = ["Dr. Cat", "Anna", "Eva", "Anna", "Anna", "Kate", "Dr. Cat"]
# print(names.index("Anna"))
# print(names.index("Dr. Cat"))

# Note that you cannot use .index() to get the index of an element that does not exist:
# names = ["Dr. Cat", "Anna", "Eva", "Anna", "Anna", "Kate", "Dr. Cat"]
# print(names.index("Bob"))