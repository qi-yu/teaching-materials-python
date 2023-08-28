# ----- 1. Open a file written in Russian and encoded in utf-8 -----
# f = open('russian.txt','r')
# lines = f.read()
# f.close()
# print(lines)

# ----- 2. Open a file using Big-5 encoding instead of utf-8 -----
## Note that it won't work:
# f = open('cb5.txt','r')
# f.read()

# ----- 3. Convert the encoding -----
## 3.1 Read files that are not in UTF-8:
## We take a file using Big-5 encoding as example.

## First read in the file using Big-5 instead of UTF-8:
# f = open('cb5.txt','rb') # "rb" reads in file as bytes
# lines = f.read()
# print(lines)

## Then convert from big5 to UTF-8 characters:
# lines = lines.decode('big5')
# print(lines)

## 3.2 Write files in other encodings than UTF-8:
# mytext = '漢語'
# f = open('myfile_big5.txt', 'wb')
# f.write(mytext.encode('big5')) # write bytes in big5
# f.close()
