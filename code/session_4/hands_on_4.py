mystring = "Jennifer and her daughter in Berlin"

count = 0

for i in range(0, len(mystring)):
    if mystring[i: i+2] == "er":
        count += 1

print(count)