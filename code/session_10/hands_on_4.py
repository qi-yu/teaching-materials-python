import re

# ----- Task 1: -----
f = open("peterpan.txt", "r")

cleaned_lines = []
for line in f.readlines():
    line = line.strip()
    cleaned_lines.append(line)

print(cleaned_lines)

# ----- Task 2: -----
for line in cleaned_lines:
    if re.fullmatch("[A-Z\s]+", line):
        print(line)

# ----- Task 3: -----
for line in cleaned_lines:
    match = re.findall("\s\w*(aa|ee|ii|oo|uu)\w*\s?", line)
    if match:
        print(match)