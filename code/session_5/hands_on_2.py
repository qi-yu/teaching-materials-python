numbers = (1, 2, 3, 4, 5, 6, 7)

# ----- Method 1 -----
# for i in numbers:
#     if i % 2 == 0:
#         print(i)

# ----- Method 2: Not robust for EVERY tuple, but works for this special case -----
# for i in range(1, len(numbers), 2): # 1, 3, 5
#     print(numbers[i])