# ----- Method 1: Read in file as a whole -----
# f = open('testfile.txt','r') #open file stream
# lines = f.read() #read form it
# f.close() #close stream
#
# print(lines) #print contents
# print(type(lines))

# ----- Method 2: Read in file line by line -----
f = open('testfile.txt','r')

for line in f: #read from stream line by line
    # print(line, end=" ")
    # You can also do operations on each line, e.g., print length of line
    print("LENGTH:" , len(line), '; TEXT:', line)

f.close() #close file stream
