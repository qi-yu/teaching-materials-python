import random

# ----- 1. Concatenate and repeat tuples -----
# employee_names = ("Dr. Cat", "Anna", "Eva")
# new_employee_names = ("Amy", "Kate")

# all_employees = employee_names + new_employee_names
# print(all_employees)

# print(new_employee_names * 3)
# print(new_employee_names * 3 * 2)

# This won't work!
# print(new_employee_names * employee_names)

# ----- 2. Get length of tuple -----
# employee_names = ("Dr. Cat", "Anna", "Eva")
# print(len(employee_names))

# ----- 3. Check if an element is in the tuple -----
# employee_names = ("Dr. Cat", "Anna", "Eva")
# print("Dr. Cat" in employee_names)
# print("Kate" in employee_names)


# ----- 4. max() and min() -----
# employee_names = ("Dr. Cat", "Anna", "Eva")
# print(max(employee_names))
# print(min(employee_names))

# employment_length = (1, 2, 10)
# print(max(employment_length))
# print(min(employment_length))

# employee_infos = (("Dr. Cat", 0, "researcher"),
#                   ("Anna", 5, "lab manager"),
#                   ("Eva", 1, "student assistant"))
# print(min(employee_infos))

# # Note that the following cases won't work!
# random_tuple = ("Dr. Cat", 30, ("Anna", 5.5, "lab manager"), False)
# print(max(random_tuple))


# ----- 5. Indexing and slicing -----
## Example 1
# work_days_cat = ("Dr. Cat", 30, 0, 0)
# print("Name:", work_days_cat[0])
# print("Working day amount: ", work_days_cat[1:])

## Example 2: A small recap of the module "random"
# employee_names = ("Dr. Cat", "Anna", "Eva")
# index = random.randint(0, len(employee_names))
# print("Get a random employer: ")
# print(employee_names[index])