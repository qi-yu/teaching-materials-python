# #function with unspecified number of unnamed and named arguments
# def func(*args,**kwargs):
#     for a in args:
#         print("AN ARGUMENT: ", a)  #print unnamed args
#     for k in kwargs:
#         print("A KEYWORDED ARGUMENT: ", k,'\t',kwargs[k])  #print named args

# #invoked with unnamed FOLLOWED by named arguments
# func(3, 6, 8, hat='wow', chair=3.5)

## Note that naming the unspecified number of arguments as "args" or "kwargs" is only a convention.
## The names of the arguments doesn't need to be "args" or "kwargs":
# def func(*x,**y):
#     for a in x:
#         print("AN ARGUMENT: ", a)
#     for k in y:
#         print("A KEYWORDED ARGUMENT: ", k,'\t',y[k])
#
# func(3, 6, 8, hat='wow', chair=3.5)