# file = open('file.txt', mode = 'r+')

# Mode
# r: Read file (Default).
# r+: Read And Write file.
# w: Write file. Delete the content of the current file.
# w: Write and Read file. Delete the content of the current file.
# a: Write file. If file not exist then create new file.
# a+: Write and Read file. If file not exist then create new file.


#seek(n): Move the cursor to n.
# data = file.read(-1)
# data2 = file.read()
# print(data)
# # print(data2)
# file.close()

with open('file.txt') as file:
    data = file.read()

print(data)