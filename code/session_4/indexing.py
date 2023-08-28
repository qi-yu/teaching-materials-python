# ----- 1. Indexing - Basics: -----
# word = input("Give me a word: ")
# first_char = word[0]
# second_char = word[1]
#
# print("The first letter of your word is:", first_char)
# print("The second letter of your word is:", second_char)


# ----- 2. Using positive position numbers and negative position numbers: -----
## 2.1 Positive index:
# mystring = "python"
# print(mystring[1])
# print(mystring[4])

## 2.2 Negative index:
# mystring = "python"
# print(mystring[-1])
# print(mystring[-2])


# ----- 3. Be careful of IndexError: -----
# mystring = "python"
#
# for i in range(0, 7):
#     print(mystring[i])


mystring = "python"
mystring = mystring.replace("p", "c")
print(mystring)