

# ----- Method 1: It works, but definitely not elegant-----
# mystring = "auto"
# for letter in mystring:
#     if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
#         mystring = mystring.replace(letter, "x")
#
# print(mystring)

# ----- Method 2: more elegant -----
mystring = "auto"
VOWEL = "aeiou"
# Write the variable name in all caps if its value is constant,
# i.e., it won't change during the run of the program.

for i in mystring:
    if i in VOWEL:
        mystring = mystring.replace(i, "x")

print(mystring)
