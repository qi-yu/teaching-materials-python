import random # "Grab the toolkit 'random'"

# ----- 1. randint() -----
x = random.randint(3, 5)
print(x)

# Both the start-argument and the stop-argument in randint() are required.
# The following line won't work because one argument is missing:
# print(random.randint(3))


# ----- 2. randrange() -----
## 2.1 Passing only one argument to the function:
## This is automatically interpreted as the value for the "stop"-argument,
## as "stop" is the only required argument for the function randrange()
# print(random.randrange(3))

## 2.2 Passing two arguments to the function:
## The arguments will be automatically interpreted as the value for the "start" and the "stop"-argument
# print(random.randrange(3, 6))
# print(random.randrange(stop=3, step=6))

## 2.3 Passing three arguments ("start", "stop" and "step") to the function:
# print(random.randrange(3, 19, 5))

