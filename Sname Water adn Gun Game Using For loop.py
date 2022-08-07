import random
# Import random to use random.choice and Used for loop for maximum of 10 trails. 
print("This is Snake (S), Water(W) and  Gun(G) Game")
# A list is created named as Player2
Player2 = ["S","W","G"]
tabulate_wins = 0
tabulate_ties = 0
tabulate_losses = 0
for i in range(1,11):
    print("Trial number by the user", i)
    P1 = input()
    P2 = random.choice(Player2)
    print(P2)
    if P1 == "S":
        if P2 == P1:
            print("Match is tie")
            tabulate_ties += 1
        elif P2 == "G":
            print("P1 losses the match")
            tabulate_losses += 1
        else:
            print("P1 wins the match")
            tabulate_wins += 1
    elif P1 == "G":
        if P2 == P1:
            print("Match is tie")
            tabulate_ties += 1
        elif P2 == "W":
            print("P1 losses the match")
            tabulate_losses += 1
        else:
            print("P1 wins the match")
            tabulate_wins += 1
    elif P1 == "W":
        if P2 == P1:
            print("Match is tie")
            tabulate_ties += 1
        elif P2 == "S":
            print("P1 losses the match")
            tabulate_losses += 1
        else:
            print("P1 wins the match")
            tabulate_wins += 1



print(tabulate_losses)
print(tabulate_wins)
print(tabulate_ties)






