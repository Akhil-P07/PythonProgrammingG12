def PrintStick(n):
    print("o " * n)
    print("| " * n)
    print("| " * n)
    print("| " * n)
    print("| " * n)

TotalStick = 21
win = False
humanPlayer = True

print("==== Welcome To Stick Picking Game :: Computer Vs User =====")
print("Rule: 1) Both User and Computer can pick sticks between 1 to 4 at a time")
print("2) Whosoever picks the last stick will be the looser")
print("==== Lets Begin ======")

playerName = input("Enter Your Name: ")
userPick = 0
PrintStick(TotalStick)

while win == False:
    if humanPlayer == True:
        print("You Can Pick stick between 1 to 4")
        userPick = 0
        while userPick <= 0 or userPick > 4:
            userPick = int(input(playerName + ": Enter Number of Stick to Pick: "))
        TotalStick = TotalStick - userPick
        humanPlayer = False
        PrintStick(TotalStick)
        print("*" * 60)
        input("Press any key...")
    else:
        computerPick = (5 - userPick)
        print("Computer Picks:", computerPick, "Sticks")
        TotalStick = TotalStick - computerPick
        PrintStick(TotalStick)
        
        if TotalStick == 1:
            print("## WINNER: COMPUTER ##")
            win = True
            print("*" * 60)
            input("Press any key...")
        
        humanPlayer = True
