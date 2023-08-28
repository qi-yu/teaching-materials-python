# ----- 1. Iterate over a string (AUTHOR: Dawson(2003) -----
# word = input("Enter a word: ")
#
# print("\nHere's each letter in your word:")
# for letter in word:
#     print(letter)
#
# input("\n\nPress the enter key to exit.")

# ----- 2. Recap: Using "continue" to do finer control of the loop -----
# word = input("Enter a word: ")
#
# print("\nHere's all letter in your word that do not equal to 'a' or 'e':")
# for letter in word:
#     if letter == "a" or letter == "e":
#         continue
#     print(letter)

# ----- 2. Recap: Using "break" to do finer control of the loop -----
# word = input("Enter a word with more than 3 letters: ")
#
# print("\nHere's the first three letters in your word:")
# count = 0
#
# for letter in word:
#     print(letter)
#     count += 1
#     if count > 2:
#         break