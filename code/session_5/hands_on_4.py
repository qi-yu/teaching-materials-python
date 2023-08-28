import random

# ----- Part 1) -----
user_input = int(input("Give me a number between 1 and 5: "))

while user_input < 1 or user_input > 5:
    user_input = int(input("Give me a number between 1 and 5: "))

# ----- Part 2) -----
## ----- Method 1: -----
# numbers = []
# while user_input > 0:
#     random_number = random.randint(20, 30)
#     numbers.append(random_number)
#     user_input -= 1
#
# print(numbers)

## ----- Method 2: -----
# numbers = []
#
# for i in range(user_input):
#     random_number = random.randint(20, 30)
#     numbers.append(random_number)
#
# print(numbers)
