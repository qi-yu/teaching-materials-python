# ----- 1. Write a file -----
# file_1 = open('my_important_notes.txt','w') #open file stream
#
# #write two lines to the file
# file_1.write('important message 1\n')
# file_1.write('important message 2\n')
#
# #close file stream
# file_1.close()


# ----- 2. Now open a new file stream "file_2",
# but the file to write to has the same name as above -----
file_2 = open('my_important_notes.txt','w')

file_2.write('NEW text 1\n')
file_2.write('NEW text 2\n')

file_2.close()