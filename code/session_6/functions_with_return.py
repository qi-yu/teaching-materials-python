# ----- 1. Keyword "return" ------
## We start with an example of simple function:
# def myfunc():
#     mystr = 'Colorless green ideas sleep furiously'
#     print(mystr)
#
# myfunc()

## This won't work:
# mystr += "."

## With return:
# def myfunc_2():
#     mystr = 'Colorless green ideas sleep furiously'
#     print(mystr)
#     return mystr
#
# x = myfunc_2()
# print(x)
# x += "!!!"
# print(x)

# ----- 2. Statement after "return" will be ignored ------
# def myfunc():
#     mystr = 'Colorless green ideas sleep furiously'
#     print(mystr)
#     return mystr
#     print("Print out this line, too.")
#
# myfunc()

# ----- 3. Return multiple values -----
# def myfunc():
#     # #collect two strings from the user:
#     x = input('First string: ')
#     y = input('Second string: ')
#
#     # concatenate strings:
#     z = x + ' ' + y
#
#     # Now the function returns three different values:
#     # Length of x, length of y, and the concatenated string
#     return len(x), len(y), z
#
# a, b, c = myfunc() # Assign the 3 returned values respectively to a, b, c
#
# ##print the 3 values
# print('LENGTH OF THE FIRST STRING:',a)
# print('LENGTH OF THE SECOND STRING:',b)
# print('THE CONCATENATED STRING:',c)
