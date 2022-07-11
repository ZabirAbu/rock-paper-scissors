import random,time

userScore = 0
compScore = 0

choices = ["r","p","s"]

rnd = 1

while True:
    print("Round: ", rnd)
    userChoice = input("What do you pick (r)ock, (p)aper, (s)cissors?")
    compChoice = random.choice(choices)

    if len(userChoice) == 0:
        print("Invalid answer. Try again.")
        time.sleep(1)
        continue

    print("Computer chose: ", compChoice)

    if userChoice[0].lower() == compChoice:
        print("Draw!")
        time.sleep(1)
        continue

    elif userChoice[0].lower() == "r" and compChoice == "s":
        print("User wins this round!")
        time.sleep(1)
        userScore = userScore + 1
    elif userChoice[0].lower() == "r" and compChoice == "p":
        print("Computer wins this round!")
        time.sleep(1)
        compScore = compScore + 1
    elif userChoice[0].lower() == "s" and compChoice == "p":
        print("User wins this round")
        time.sleep(1)
        userScore = userScore + 1
    elif userChoice[0].lower() == "s" and compChoice == "r":
        print("Computer wins this round")
        time.sleep(1)
        compScore = compScore + 1
    elif userChoice[0].lower() == "p" and compChoice == "s":
        print("Computer wins this round")
        time.sleep(1)
        compScore = compScore + 1
    elif userChoice[0].lower() == "p" and compChoice == "r":
        print("User wins this round")
        time.sleep(1)
        userScore = userScore + 1
    else:
        print("Invalide answer. Try again!!")
        continue

    rnd = rnd + 1
    if rnd == 6:
        break

print("User wins:" , userScore)
print("Computer wins:" , compScore)

if userScore > compScore:
    print("User wins the game!")
elif compScore > userScore:
    print("Computer wins the game!")
else:
    print("Draw!!")