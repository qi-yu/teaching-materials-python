# ----- 1. Evaluating an expression using comparison operators: -----
## The evaluation returns a boolean value
# print(10 >= 9)
# print("leopard" < "bear")

# ----- 2. Using bool() to evaluate a value -----
## 2.1 Examples with numbers
# print(bool(10))
# print(bool(0))

## 2.2 Examples with strings
# print(bool("leopard"))
# print(bool(""))

## ----- 3. Evaluating a value as a condition -----
user_input = input("Please enter your name: ")
if user_input:
    print("Hello, " + user_input + "!")
else: # If you only hits the enter-key instead of writting anything, the else-block will be called.
    print("Your input is not valid.")