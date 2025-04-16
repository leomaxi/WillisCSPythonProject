
valid_choices = {"Rock", "Paper", "Scissors"}
#Get Player 1 input sand validate it
player1 = (input("Player 1 - Enter your choice ("+str(valid_choices).replace("{","").replace("}","")+"): ").capitalize())
if player1 not in valid_choices:
    print("Invalid input from Player 1. Please enter Rock, Paper, or Scissors.")
    exit()

# Get Player 2 input and validate it
player2 = (input("Player 2 - Enter your choice ("+str(valid_choices).replace("{","").replace("}","")+"): ").capitalize())
if player2 not in valid_choices:
    print("Invalid input from Player 2. Please enter Rock, Paper, or Scissors.")
else:
    # Step 3: Determine result
    if player1 == player2:
        print("Draw; You both chose the same thing")
    elif (player1 == "Rock" and player2 == "Scissors") or \
         (player1 == "Paper" and player2 == "Rock") or \
         (player1 == "Scissors" and player2 == "Paper"):
        print("Player 1 wins")
    else:
        print("Player 2 wins")
