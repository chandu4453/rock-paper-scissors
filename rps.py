money=5
def balance():
    global user_input
    print(f"you have {money} rs")
    print("you need 5 rs to play")
    user_input=input("enter choice: ROCK,PAPER OR SCISSORS: ")

def player_move():
    if user_input in ("ROCK","rock","r","R") :
         return "Rock"
    elif user_input in ("PAPER","Paper","P","p") :
         return "Paper"
    elif user_input in ("SCISSORS","Scissors","s","S"):
         return "Scissors"
    else :
         return print("Enter correct option")
            
def comp_move():
    import random
    r=["Rock","Scissors","Paper"]
    c=random.choice(r)
    return c

    
def winner() :
    player=player_move()
    comp=comp_move()
    global money
    if player =="Rock" and comp=="Rock" :
        print(f"player choice is {player}")
        print(f"computer choice is {comp}")
        print("its a draw")
    elif player=="Rock" and comp=="Scissors" :
        money+=5
        print(f"player choice is {player}")
        print(f"computer choice is {comp}")
        print("player has won")
    elif player=="Rock" and comp=="Paper" :
        money-=5
        print(f"player choice is {player}")
        print(f"computer choice is {comp}")
        print("comp has won")
    elif player=="Scissors" and comp=="Paper" :
        money+=5
        print(f"player choice is {player}")
        print(f"computer choice is {comp}")
        print("player has won")
    elif player=="Scissors" and comp=="Rock" :
        money-=5
        print(f"player choice is {player}")
        print(f"computer choice is {comp}")
        print("comp has won")
    elif player=="Scissors" and comp=="Scissors" :
        print(f"player choice is {player}")
        print(f"computer choice is {comp}")
        print("its a draw")
    elif player=="Paper" and comp=="Paper" :
        print(f"player choice is {player}")
        print(f"computer choice is {comp}")
        print("its a draw")
    elif player=="Paper" and comp=="Rock" :
        money+=5
        print(f"player choice is {player}")
        print(f"computer choice is {comp}")
        print("player has won")
    elif player=="Paper" and comp=="Scissors" :
        money-=5
        print(f"player choice is {player}")
        print(f"computer choice is {comp}")
        print("comp has won")
        


while money>=5 :
    balance()
    player_move()
    comp_move()
    winner()
else :
    print("you dont have enough money to play")
    





