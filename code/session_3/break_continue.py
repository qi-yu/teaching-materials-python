# # ----- 1. break-statement -----
# password = input("This is a password-protected system. Please type in the password to log in: ")
# count = 1
#
# while password != "python12345":
#     print("Your password is wrong.")
#     password = input("Please enter the password again: ")
#     count += 1
#
#     if password == "python12345":
#         print("\nYou've successfully logged into the system.")
#         break
#
#     if count > 2:
#         print("You've input wrong password for two many times. Now you are blocked by the system.")
#         break


# ----- 2. continue-statement -----
# count = 5
#
# while count > 0:
#    count -= 1   # Recap: augmented assignment operators
#    # current value of count: 2
#    if count == 3:
#       continue
#    print(count)


# ----- 3. Using break and continue together -----
# count = 0
#
# while True:
#    count += 1
#
#    if count % 2 == 0:
#       continue
#
#    if count > 10:
#        break
# 
#    print(count)