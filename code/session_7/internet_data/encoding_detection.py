import chardet
from bs4 import UnicodeDammit

file1 = open('russian.txt','rb')
text1 = file1.read()

file2 = open('dh.html','rb')
text2 = file2.read()

# ----- 1. Detecting encoding using chardet -----
# print(chardet.detect(text1))
# print(chardet.detect(text2))

# ----- 2. Detecting encoding using UnicodeDammit -----
enc_text1 = UnicodeDammit(text1)
print(enc_text1.original_encoding)

enc_text2 = UnicodeDammit(text2)
print(enc_text2.original_encoding)