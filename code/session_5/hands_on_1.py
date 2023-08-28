tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)

# ----- Method 1 -----
# for i in range(0, 3): # 0 , 1, 2
#     print(tuple_1[i] + tuple_2[i])

# ----- Method 2 -----
# for i in range(len(tuple_1)): # equivalent to range(3) -> 0, 1, 2
#     print(tuple_1[i] + tuple_2[i])