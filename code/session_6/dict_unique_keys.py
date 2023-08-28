# Imagine we have a dictionary for the university enrollment system:
# Each key is the name of a student,
# and the associated value is the enrollment-number of that student.

# enrollment_num = {
#     "Amy.Smith": 10001,
#     "Bob.Steve": 10002,
#     "Cathy.Davis": 10003
# }

# Imagine that a new student with the same name "Amy Smith" is enrolled.
# She is assigned the enrollment-number "10004".
# Note what happens below if we try to add the second "Amy Smith" into the dictionary:

# enrollment_num["Amy.Smith"] = 10004
# print(enrollment_num)

# So always keep every key unique.
# The following works without the rewritting-problem:

# enrollment_num = {
#     "Amy.Smith": 10001,
#     "Bob.Steve": 10002,
#     "Cathy.Davis": 10003
# }
#
# enrollment_num["Amy.2.Smith"] = 10004
# print(enrollment_num)