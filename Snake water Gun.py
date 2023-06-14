import random
# Import random for random.choices() 
# The code is kept simple and long so that one can unerstand it easily.
# Contact me if you have any concerns. 
print("Welcome to Snake Water and Gun Game. \n")
"For snake, water and gun type s,w,g respectively. \n")
"The game is case sensitive. \n")
"This game will give you total of 10 iterations.")
l = ["s","w","g"]
k = random.choice(l)
Tie = 0
Computer_Won = 0
You_Won = 0
Wrong_input = 0
# initalising the parameters to count the wins and draws at the end of the game.
i = 1
while i <= 10:
    print("Enter the word you choose",l)
    G = input()
    if G == "s" and k == "s":
        print("The word choose by the computer",k)
        print("this game is tie.")
        Tie += 1
    elif G == "s" and k == "w":
        print("The word choose by the computer", k)
        print("You won the game.")
        You_Won += 1
    elif G == "s" and k == "g":
        print("The word choose by the computer", k)
        print("Computer won the game.")
        Computer_Won += 1
    elif G == "g" and k == "g":
        print("The word choose by the computer", k)
        print("This is tie.")
        Tie += 1
    elif G == "g" and k == "w":
        print("The word choose by the computer", k)
        print("Computer won the game.")
        Computer_Won += 1
    elif G == "g" and k == "s":
        print("The word choose by the computer", k)
        print("You won the game.")
        You_Won += 1
    elif G == "w" and k == "w":
        print("The word choose by the computer", k)
        print("This is tie.")
        Tie += 1
    elif G == "w" and k == "s":
        print("The word choose by the computer", k)
        print("Computer won the game.")
        Computer_Won += 1
    elif G == "w" and k == "g":
        print("The word choose by the computer", k)
        print("You won the game.")
        You_Won += 1
    else:
        print("You have given the wrong input.")
        Wrong_input += 1
    i += 1
# One can customize the if else statement to optimize the code more and shorter.
print("The number of times the game was draw",Tie)
print("The number of time you won", You_Won)
print("The number of time computer won", Computer_Won)
print("Count of wrong entries", Wrong_input)
