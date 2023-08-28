# ----- 1. Construct a dictionary -----
# deposit = {"Amy": 1000, "Bob": 1500, "Cathy": 2000000}
# print(deposit)

# A more sophisticated dictionary: Use lists as values
# xmas_wishes = {"Amy": ["book", "sweets"],
#                "Bob": ["wine", "chocolate", "new wallet"],
#                "Cathy": ["sweets"]}

# ----- 2. Operations and methods for dictionaries -----
## 2.1 Look up the value of a key:
# print(xmas_wishes["Amy"])

### Note that if the key is not in a dictionary,
## Looking up the value using the key will generate an error:
# print(xmas_wishes["John"])

### A safer way to retrieve the value,
### if you don't already know whether the key is in the dictionary:
# key = "John"
# if key in xmas_wishes:
#     print(xmas_wishes[key])
# else:
#     print('"' + key + '"', "is not in the dictionary!")


## 2.2 .get(): another safer way to retrieve the value:
## If the key is not in the dictionary,
## .get() will return a "None".
# print(xmas_wishes.get("Bob"))
# print(xmas_wishes.get("John"))

### You can also add a message to print out,
### when the key is not in the dictionary:
# print(xmas_wishes.get("Bob", "This key is not in the dictionary!"))
# print(xmas_wishes.get("John", "This key is not in the dictionary!"))


## 2.3 Modify the value of a key
# deposit = {"Amy": 1000, "Bob": 1500, "Cathy": 2000000}
# deposit["Amy"] += 500
# print(deposit)

## 2.4 Delete the value of a key
# del deposit["Bob"]
# print(deposit)

## 2.5 Get all keys, all values or all items of a dictionary:
# deposit = {"Amy": 1000, "Bob": 1500, "Cathy": 2000000}

### 2.5.1 Get all keys:
# print(deposit.keys())

### Or you can use a for-loop to print out all keys:
# for k in deposit.keys():
#     print(k)

### 2.5.2 Get all values:
# print(deposit.values())

# for v in deposit.values():
#     print(v)

### 2.5.3 Get all items:
# print(deposit.items())

### Using the comma-syntax to unpack sequences:
# for k, v in deposit.items():
#     print("KEY:", k, "--> VALUE:", v)