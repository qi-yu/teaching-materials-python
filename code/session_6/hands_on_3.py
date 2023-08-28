def concatenate(*args):
    concat = ""
    for i in args:
        concat += i

    return concat

concat1 = concatenate("hello", "world")
concat2 = concatenate("a", "b", "c", "d", "e")

print(concat1)
print(concat2)