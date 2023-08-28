# ----- 1. Slicing - Basics: -----
# mystring = "Gaming with Python"

# slice_1 = mystring[0:8] # Note that the position 8 is NOT included!
# print(slice_1)
#
# slice_2 = mystring[2:5]
# print(slice_2)

# ----- 2. Using positive position numbers and negative position numbers: -----
## 2.1 Positive index:
# mystring = "Gaming with Python"
# print(mystring[2:5])
# print(mystring[3:9])

## 2.2 Negative index:
# mystring = "Gaming with Python"
# print(mystring[-5:-1])

# Note that this won't work:
# mystring = "Gaming with Python"
# print(mystring[-1:-5])


# ----- 3. Out-of-bound index is not a problem for slicing: -----
# mystring = "Gaming with Python"
# print(mystring[80:90])

# ----- 4. Shorthand for slicing: -----
mystring = "Gaming with Python"

## 4.1 Leaving the start point unspecified:
## equivalent to starting from the beginning (i.e., index 0)
# print(mystring[:5])

## 4.2 Leaving the cut-off point unspecified: equivalent to slicing until the end
# print(mystring[5:])

## 4.3 Leaving both ends unspecified:
## equvalent to slice everything from the beginning to the end;
## This is in turn equivalent to getting the whole string.

print(mystring[:])