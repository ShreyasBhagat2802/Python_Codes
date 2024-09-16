# ...Open file indifferent modes such as "r", "w", "a" , "x"
# ...write into the file : 1) Discard all and write from start
#                          2) Write form the next to file pointer

# ...read content from the file : 1) All content from file
#                                 2) Specified content from the file
# ...Deleting existing file
# ...Renaming existing file

import os

# ...Opening existing file
f = open("Shreyas.txt")

# ...Reading and display content from file
print(f.read())
# ...Reading and display specific content from file
print(f.read(4))
# ...Closing the opened file
f.close()

# ...opening file in append mode and writing something to file
f = open("Shreyas.txt","a")
f.write("How are you?")
f.close()

f = open("Shreyas.txt")
print(f.read())

# ...opening file in write mode and writing something to file
f = open("Shreyas1.txt","w")
f.write("Hii")
f.close()

f = open("Shreyas.txt")
print(f.read())
print(f.readline())
f.close()

# ...Creating new file and writing something into the file
f1 = open("New_File.txt", "x")
print("File crated")
f1.write("Hello New User.")
f1.close()

# ...Reading content from newly created file
f1 = open("New_File.txt")
print(f1.read())
f1.close()

# ...Usign with(), read data
with  open("New_File.txt") as f2:
    data = f2.read()
print(data)
f2.close()

# ...Appending string into the file
str1 = " Bridgelabz Solution"
f3 = open("New_File.txt", "a")
f3.write(str1)
f3.close
f3 = open("New_File.txt")
print(f3.read())


# ...Deleting existing file (New_File.txt)
os.remove("New_File.txt")

# ...Renaming Existing file
os.rename("New_File1.txt", "New_File2.txt")