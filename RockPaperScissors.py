import random
gameStart = int(input("Press 1 to start game, 2 to quit game\n"))
while gameStart == 1 :
    
    choicesList = ((1,"Rock"),(2,"Paper"),(3,"Scissors")) 
    computerChoice = random.choice(choicesList)   
    userChoice = int(input("""Enter your choice:
      1.Rock
      2.Paper
      3.Scissors\n"""))
       #first possibility
    if userChoice == 1 and computerChoice[0]==1 :
        print("Draw"+" Computer choice is " + computerChoice[1])
    elif userChoice == 1 and computerChoice[0]==2 :
        print("Computer won" +" Computer choice is " + computerChoice[1])
    elif userChoice==1 :
        print("You won"+" Computer choice is" + computerChoice[1])
       #second possibility
    if userChoice == 2 and computerChoice[0]==1 :
        print("You won"+" Computer choice is " + computerChoice[1])
    elif userChoice == 2 and computerChoice[0]==2 :
        print("Draw"+" Computer choice is " + computerChoice[1])
    elif userChoice==2 :
        print("Computer won" +" Computer choice is " + computerChoice[1])
        #third possibility
    if userChoice == 3 and computerChoice[0]==1 :
        print("Computer won" +" Computer choice is " + computerChoice[1])
    elif userChoice == 3 and computerChoice[0]==2 :
        print("You won"+" Computer choice is " + computerChoice[1])
    elif userChoice==3 :
        print("Draw"+" Computer choice is " + computerChoice[1])
    print()
    gameStart = int(input("Press 1 to restart game, 2 to quit game\n"))  
print("""Thanks for playing
      -Yusuf Süsin""")             
      