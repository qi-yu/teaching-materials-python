import re

# ----- 1. search() -----
# FUNCTION:
# Scanning through a string and find the first location where
# the regular expression pattern produces a match.

# RETURNS:
# If there is a match: returns a match() object
# If there is no match: returns "None"

# search1 = re.search("ab", "about our lab")
# search2 = re.search("a.*b", "hat")
# print("SEARCH 1:", search1)
# print("SEARCH 2:", search2)

## The match() object has several methods callable:
# search = re.search("a.*b", "carbon")
# # print(search)
#
# if search:
#     print(search.group()) # return the matched part
#     print(search.start()) # return the starting boundary index of the matched part
#                           # (boundary index: recall slicing using ":")
#     print(search.end())   # return the ending boundary index of the matched part
#     print(search.span())  # return both the starting and the ending boundary index

## Also note that the search is done in a greedy way:
## The matched part below is "an arabic art b", not only "an arab".

# print(re.search("a.*b", "an arabic art book"))


# ----- 2. findall() -----
# FUNCTION:
# Returning all non-overlapping matches of pattern in a string.

# RETURNS:
# If matched: returns all instances of the match as a list.
# If no match: returns an empty list.

# findall1 = re.findall("in", "Lina in China")
# findall2 = re.findall("in", "Luna in Chile")
# findall3 = re.findall("in", "Luna")
# print(findall1)
# print(findall2)
# print(findall3)


# ----- 3. fullmatch() -----
# FUNCTION:
# Checking if the whole string matches the regular expression pattern.

# RETURNS:
# If matched: returns a corresponding match object.
# If the string does not match the pattern: returns "None".

# pattern = "(the|a)\sstory\sof\s[Aa]lice"
# string1 = "the story of alice"
# string2 = "I read the story of alice"
#
# match1 = re.fullmatch(pattern, string1)
# print("RESULT 1:", match1)
#
# match2 = re.fullmatch(pattern, string2)
# print("RESULT 2:", match2)


# ----- 4. sub() -----
# FUNCTION:
# Replace the matches with another string.

mystr = "abc yyy abbc yyy abc xxx ac yyy"
mystr_replaced = re.sub("ab*c", "#", mystr)
print(mystr_replaced)