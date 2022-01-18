from random import randint

print("\t Chon Keo, Bua, Bao")

player = input()
computer = randint(1,3)

if computer == 1:
    computer = "Keo"
elif computer == 2:
    computer = "Bua"
elif computer == 3:
    computer = "Bao"

if player == computer:
    print("Draw")
else:
    if player == "Keo":
        if computer == "Bua":
            str = "You Lose!"
        else:
            str = "You Win!"
        
    elif player == "Bua":
        if computer == "Keo":
            str = "You Win!"
        else:
            str = "You Lose!"

    elif player == "Bao":
        if computer == "Keo":
            str = "You Lose!"
        else:
            str = "You Win!"
    else:
        str = "Nhap sai"
print("---")
print("Ban chon: " + player)
print("May tinh chon: " + computer)
print(str)
print("---")