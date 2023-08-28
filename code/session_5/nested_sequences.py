# ----- Example 1 -----
# employee_infos = [("Dr. Cat", 0, "researcher"),
#                   ("Anna", 5, "lab manager"),
#                   ("Eva", 1, "student assistant")]
#
# print(employee_infos[0][-1])
# print(employee_infos[1][2])

# ----- Example 2: even more nested sequences -----
# employee_infos = [
#     ["Dr. Cat", 0, ("researcher", "linguistics")],
#     ["Anna", 5, ("lab manager", "psychology")],
#     ["Eva", 1, ("student assistant", "psychology")]
# ]

## Print out only the research discipline of Dr. Cat, i.e., "linguistics"
# print(employee_infos[0][2][1])