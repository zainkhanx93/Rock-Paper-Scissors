
user1 = input("What is Player 1 Name \n")
user2 = input("What is Player 2 Name \n")

print ("Enter p for Paper, r for Rock and s for Scissors")

print ("\n")
player1 = input("Player 1 do you want paper, rock or scissors \n")
player2 = input("Player 2 do you want paper, rock or scissors \n")

def game(p1, p2):

    if (p1 == p2):
        return ("It's a Tie")
    
    elif p1 =='r':
        if p2 == 's':
            return ("Rock Wins")
        else:
            return ("Paper Wins")

    
    elif p1 == 'p':
        if p2 == 'r':
            return ("Paper Wins")
        else:
           return ("Scissors Wins")

    elif p1 == 's':
        if p2 == 'p':
           return ("Scissors Wins")
        else:
            return ("Rock Wins")


    else:
        return ("Invalid input. Try Again.")
        sys.exit()
print (game(player1,player2))
