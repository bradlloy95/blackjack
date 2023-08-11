import random
Player_score = 0
Computer_score = 0
Players_Pot = 10
Deck_dict = {}
Players_hand = []
Computers_hand = []
Player_status = True
Bet = 0
PLayers_turn =True
#initalize deck 
def Deck():
    """
    creates a dictionary of a deck of cards and their black jack value
    """      
    #global Deck_dict
    for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]:
        for number in range(13):
            number +=1
            n = number
            
            number = str(number)
            if number == "1":
                number = "Ace"
                n = 11
            if number == "11":
                n = 10
                number = "Jack"
            if number == "12":
                n = 10
                number = "Queen"
            elif number == "13":
                n = 10
                number = "King"
            
              
            card = f"{number} of {suit}"
            
            Deck_dict[card] = n
            
        
    return 


def Deal():
    global Player_score 
    global Computer_score
    global Players_hand
    global Computers_hand
    """
    deals a card, removes from dict so it cant be redelt
    """
    for i in range(2):
        deal = random.choice(list(Deck_dict.keys()))
        #print(deal)
        Players_hand.append(deal)
        
        Player_score = Player_score + Deck_dict[deal]
        del Deck_dict[deal]
        
    for i in range(2):
        deal = random.choice(list(Deck_dict.keys()))
        #print(deal)
        Computers_hand.append(deal)
        
        Computer_score = Computer_score + Deck_dict[deal]
        del Deck_dict[deal]
        
    if Player_score > 11:
        Deck_dict['Ace of Hearts'] = 1
        Deck_dict['Ace of Diamonds'] = 1
        Deck_dict['Ace of Spades'] = 1
        Deck_dict['Ace of Clubs'] = 1
   
    
    return
            
            
            
            
    
        
    
    


#set up funds
def Funds():
    """
    player starts with 10 pounds 
    for every 2 pounds the player gets 3 back 
    
    """
    global Players_Pot
    while True:
        #print(f"You have ${Players_Pot} left")
        Bet = input("how much would you like to bet? $")
        try:
            Bet = float(Bet)
        except:
            print("invalid input")
            continue
        
        if Bet > Players_Pot:
            print("Not enough funds")
            continue
        
        else:
            break
        
            
    return Bet

def Display():
    
    """
    creates the users interface
    """
    if PLayers_turn is True:
        print(f" \n"
              f" \n"
              f" \n"
              f"              Players hand\n"
              f" \n"
              f"           score: {Player_score}\n"
              f" \n"
                f"{Players_hand}\n"
                f" \n"
                f"--------------------------------------------------------------\n"
                f" \n"
                f"             Computers hand"
                f" \n"
                f"           score: -\n"
                f" \n"
                f"{Computers_hand[0]}\n"
                f" \n"
                f" \n"
                f"--------------------------------------------------------------\n"
                f" \n"
                f" \n"
                f" \n")
        
    elif PLayers_turn is False:
        print(f" \n"
              f" \n"
              f" \n"
              f"              Players hand\n"
              f" \n"
              f"           score: {Player_score}\n"
              f" \n"
                f"{Players_hand}\n"
                f" \n"
                f"--------------------------------------------------------------\n"
                f" \n"
                f"             Computers hand"
                f" \n"
                f"           score: {Computer_score}\n"
                f" \n"
                f"{Computers_hand}\n"
                f" \n"
                f"--------------------------------------------------------------\n"
                f" \n"
                f" \n"
                f" \n")
        
def Check_score(Hand):
    global Player_status
    if Hand == 21:
        
        return "WIN"
    
    elif Hand > 21:
        Player_status = 21
        return False
    
    elif Hand < 21:
        
        return True
    
    
    
    
    
    
    
def Hit():
    global Player_score 
    global Computer_score
    global Players_hand
    global Computers_hand
    global PLayers_turn
    """
    adds another card to players hand
    """  
    if PLayers_turn is True:
        deal = random.choice(list(Deck_dict.keys()))
        #print(deal)
        Players_hand.append(deal)
        Player_score = Player_score + Deck_dict[deal]
        del Deck_dict[deal]
        if Player_score > 11:
            Deck_dict['Ace of Hearts'] = 1
            Deck_dict['Ace of Diamonds'] = 1
            Deck_dict['Ace of Spades'] = 1
            Deck_dict['Ace of Clubs'] = 1
        return
    elif PLayers_turn is False:
        deal = random.choice(list(Deck_dict.keys()))
        #print(deal)
        Computers_hand.append(deal)
        Computer_score = Computer_score + Deck_dict[deal]
        del Deck_dict[deal]
        if Player_score > 11:
            Deck_dict['Ace of Hearts'] = 1
            Deck_dict['Ace of Diamonds'] = 1
            Deck_dict['Ace of Spades'] = 1
            Deck_dict['Ace of Clubs'] = 1
        return
        
def Returns(bet, a): 
    global Players_Pot
    bet = float(bet)
    
    if a == 'win':
    
        Players_Pot = Players_Pot + (bet*2)
        
    elif a == 'lose':
        Players_Pot -= bet
 
    elif a == "draw":
        #Players_Pot += bet
        return
    
    elif a == 'blackjack':
        Players_Pot = Players_Pot + (bet*4)
    return 
    
def Computer_turn():
    global Player_score 
    global Computer_score
    global Players_hand
    global Computers_hand
    global PLayers_turn
    deal = random.choice(list(Deck_dict.keys()))
    #print(deal)
    Computers_hand.append(deal)
    Computer_score = Computer_score + Deck_dict[deal]
    del Deck_dict[deal]
    if Player_score > 11:
        Deck_dict['Ace of Hearts'] = 1
        Deck_dict['Ace of Diamonds'] = 1
        Deck_dict['Ace of Spades'] = 1
        Deck_dict['Ace of Clubs'] = 1
    return
    
    
    
def Clear():
    """
    clears everything to start a new game 
    
    """
    global Player_score 
    global Computer_score
    global Players_hand
    global Computers_hand
    global PLayers_turn
    
    Deck_dict.clear()
    Player_score = 0
    Players_hand = []
    Computer_score = 0
    Computers_hand = []
    PLayers_turn = True
    

def Play_game():
    global Bet
    global PLayers_turn
    while True:
        begin = input("welcome to blackjack. enter 'b' to begin: ")
        
        if begin == 'b':
            Display()
            if Player_score == 21:
                print("BLACKJACK")
                Returns(Bet, 'win')
                return
            break 
        else:
            continue
        
    while PLayers_turn is True:
        print("Pick your next move. 'h' to HIT.")
        print("                     's' to STAND")
        
        Next_move = input(": ")
        
        if Next_move == 'h':
            Hit()
            Display()
        
                
            score_check = Check_score(Player_score)
            if score_check is True:
                continue
            elif score_check is False:
                print("Bust!")
                print("YOU LOSE")
                Returns(Bet, 'lose')
                break
            
            elif score_check == "WIN":
                print("BLACKJACK!")
                Returns(Bet, "blackjack")
                break
            
            
        elif Next_move == 's':
            PLayers_turn = False
            break
            
        else:
            print("invalid input")
            continue

            
    while PLayers_turn is False:
        Display()
        
        if Computer_score == 21:
            print("YOU LOSE")
            Returns(Bet, 'lose')
            #Display()
            return
        elif Computer_score == Player_score:
            
            print("DRAW")
            Returns(Bet, "draw")
            break
        
        elif Computer_score < 21:
            if Computer_score < Player_score:
                Computer_turn()
                continue
            
            elif Computer_score > Player_score:
                print("YOU LOSE")
                Returns(Bet, 'lose')
                #Display()
                return
            
        elif Computer_score > 21:
            print("YOU WIN")
            Returns(Bet, "win")
            break
        
        
        
        return
    
            
        






    
def Start_game():
    while True:
        print(f"you have ${Players_Pot}")
        Deck()
        Deal()
        global Bet
        Bet = Funds()
        
        
       
            
        Play_game()
        
        Clear()
        if Players_Pot == 0:
            print("out of funds")
            break
        
    return
        
        
    
        
        
        
        
        
        
        
    

Start_game()