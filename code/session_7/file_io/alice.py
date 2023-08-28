# ----- 1. Read in alice.txt (Hands-On 1) -----
line_count = 0
all_lines = []

f = open("/Users/qiyu/PycharmProjects/Qi_LingGaming_WS22/session_7/file_io/alice.txt", "r")
for line in f:
    line_count += 1
    all_lines.append(line)

# print("TOTAL NUMBER OF LINES:", line_count)
# print("FIRST 100 LINES:")
# for i in all_lines[:100]:
#     print(i)

# ----- 2. Preprocessing -----
all_lines = all_lines[166:5407]
# print(all_lines) # check results

# ----- 3. Split each line into words -----
words = []
for line in all_lines:
    current_words = line.split() # break each line into words
    words += current_words #add the words to the list

# Check results:
# print("TOTAL AMOUNT OF WORDS: ", len(words))
# for w in words:
#     print(w)


# ----- 4. build the length-frequency dictionary -----
length_freq_dict = {} # {3: 2, 1: 1}
for w in words:
    length = len(w) # 3
    if length not in length_freq_dict:
        length_freq_dict[length] = 1
    else:
        length_freq_dict[length] += 1

print(length_freq_dict)
