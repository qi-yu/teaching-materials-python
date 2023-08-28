#open file stream
outFile = open('my_output.txt','w') # Specify a stream

#write to it
outFile.write('some text!\n')
outFile.write('...and some more text!\n')

#close file stream
outFile.close()