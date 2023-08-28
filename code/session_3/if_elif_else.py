import random

# ----- 1. if-statement -----
# print("""
#     This program generates a random number between 1 and 3.
#     If you get the number 3, you win.
# """)
#
# num = random.randint(1, 3)
# print("The random number generated for you is:", num)
# if num == 3:
#     print("You win!")


# ----- 2. Using else-clause -----
# print("""
#     This program generates a random number between 1 and 3.
#     If you get the number 3, you win.
# """)
#
# num = random.randint(1, 3)
# print("The random number generated for you is:", num)
# if num == 3:
#     print("You win!")
# else:
#     print("You lose!")


# ----- 3. Using elif-clause -----
# print("This program helps you to make decision for your leisure activities.")
#
# user_input = input("""Choose the weather and check what to do:
#
#                    1 - sunny
#                    2 - rainy
#                    3 - snowy
#                    4 - cloudy
#
#                    """)
#
# if user_input == "1":
#     print("Go for a walk!")
# elif user_input == "2":
#     print("Work, work, work!")
# elif user_input == "3":
#     print("Maybe it's time for skiing...")
# elif user_input == "4":
#     print("Go get some dessert.")
# else:
#     print("Your input is not valid.")


# ----- 4. You can also nest the if-elif-else braching, i.e., using one branching inside another -----
print("This program helps you to make decision for your leisure activities.")

user_input = input("""Choose the weather and check what to do:

                   1 - sunny
                   2 - rainy

                   """)

if user_input == "1":
    day = input("""
        Is your homework done?
        Enter "y" if yes, and "n" if not.
    """)

    # An if-else block nested within an if-statement:
    if day == "y":
        print("Go for a walk!")
    else:
        print("Firstly finish your work! Then go for a walk.")

else:
    print("It is rainy. Staying at home is the best activity...")