length = 10
width = 5
for i in range(1, width + 1):
    if i == 1 or i == width:
        print("*"*length)
    else:
        print("*" + " "*(length-2) + "*")