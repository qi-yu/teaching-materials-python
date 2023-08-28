# ----- 1. range() function and for-loops -----
## 1.1  range() function with only one argument:
## The argument is automatically interpreted as the value of "stop".
## The values of "start" and "step" will be set to the default values:
## start = 0, step = 1

# for i in range(11):
#     print(i)

## 1.2 range() function with two arguments:
## The two argument are interpreted as the value of "start" and "stop".
## The values of "step" will be set to the default value 1

# for i in range(2, 10):
#     print(i)

## 1.3 range() function with three arguments:

# for i in range(2, 10, 2):
#     print(i) # Note that each generated number is increased by 2

# ----- 2. Using range() to count backwards: -----
## Example 1:
# for i in range(10, 2, -1):
#     print(i)

## Example 2:
## Note two things here:
## 1) Each generated number is decreased by 2. This is decided by the argument stop = -2.
## 2) The value of argument "stop", i.e., 2, is not included.

# for i in range(10, 2, -3):
#     print(i)

## Example 3:
## Note that this will not generate an error,
## but it won't print anything, neither.

# for i in range(10, 20, -2):
#     print(i)