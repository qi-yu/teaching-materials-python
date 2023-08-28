# ----- 1. Concatenate and repeat lists -----
word_categories_1 = ["verb", "noun", "adjective"]
word_categories_2 = ["adverb"]

# print(word_categories_1 + word_categories_2)
# print(word_categories_2 * 5)

# ----- 2. Get length of list -----
# word_categories = ["verb", "noun", "adjective"]
# print(len(word_categories))

# ----- 3. Check if an element is in the list -----
# word_categories = ["verb", "noun", "adjective"]
# is_in_categories = "adjective" in word_categories
# print(is_in_categories)


## Comparing the lines above to what we did in tuples_operators_functions.py, Part 3:
## Here we assigned the evaluation result of using operator "in" to a variable "is_in_categories".

# ----- 4. max() and min() -----
## Same as with tuples:
## They also only work when all elements of the lists are of the same data type!

# word_categories = ["verb", "noun", "adjective"]
# print(max(word_categories))
# print(min(word_categories))

# ----- 5. Indexing and slicing -----
## 5.1 Use indexing and slicing to get element(s)
# word_categories = ["verb", "noun", "adjective"]
#
# print(word_categories[0])
# print(word_categories[:2])

# ----- 6. Use "del" to delete an element or a slice -----

## 6.1 Delete an element
# word_categories = ["verb", "noun", "adjective", "adverb"]
# print("My list:", word_categories)
#
# del word_categories[2]
# print("New list:", word_categories)

### 5.2.2 Delete a slice
word_categories = ["verb", "noun", "adjective", "adverb"]
print("My list:", word_categories)

del word_categories[2:]
print("New list:", word_categories)