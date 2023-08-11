import random
Player_score = []
sum_of_player_score = sum(Player_score)
Computer_score = []
sum_of_computer_score = sum(Computer_score)
Players_Pot = 10
Deck_dict = {}
Deck_dict_Ace = {} 
Players_hand = []
Computers_hand = []
Player_status = True
Bet = 0
PLayers_turn =True
#----------------------------------------------------------------------------
def Start_game():
    while True:
        
        print(f"you have ${Players_Pot}")
        Deck()
        Deal(Deck_dict, Deck_dict_Ace, Players_hand, Player_score)
        Deal(Deck_dict, Deck_dict_Ace, Computers_hand, Computer_score)
        global Bet
        Bet = Funds()
 
        Play_game()
        
        Clear()
        if Players_Pot == 0:
            print("out of funds")
            break
    return
def Play_game():
    global Bet
    global PLayers_turn
    global sum_of_computer_score
    global sum_of_player_score
    while True:
        begin = input("welcome to blackjack. enter 'b' to begin: ")
        
        if begin == 'b':
            Display()
            if sum(Player_score) == 21:
                print("BLACKJACK")
                Returns(Bet, 'blackjack')
                return
            break 
        else:
            continue
        
    while PLayers_turn is True:
        sum_of_player_score = sum(Player_score)
        print("Pick your next move. 'h' to HIT.")
        print("                     's' to STAND")
        
        Next_move = input(": ")
        
        if Next_move == 'h':
            Hit(Deck_dict, Deck_dict_Ace, Player_score, PLayers_turn)
            
            sum_of_player_score = sum(Player_score)
            Display()   
            score_check = Check_score(Player_score, sum_of_player_score)
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
        sum_of_player_score = sum(Player_score)
        sum_of_computer_score = sum(Computer_score)
        Display()        
        if sum_of_computer_score == 21:
            print("YOU LOSE")
            Returns(Bet, 'lose')           
            return
        elif sum_of_computer_score == sum_of_player_score:
            
            print("DRAW")
            Returns(Bet, "draw")
            break
        
        elif sum_of_computer_score < 21:
            if sum_of_computer_score < sum_of_player_score:
                Hit(Deck_dict, Deck_dict_Ace, Computer_score , PLayers_turn)
                continue            
            elif sum_of_computer_score > sum_of_player_score:
                print("YOU LOSE")
                Returns(Bet, 'lose')
                #Display()
                return            
        elif sum_of_computer_score > 21:
            Ace_check(Computer_score, "c")
            sum_of_computer_score = sum(Computer_score)
            if sum_of_computer_score < 21:
                continue
            else:
                print("YOU WIN")
                Returns(Bet, "win")
                break
    return    
#initalize deck 
def Deck():                                 #creates the decks of cards
    """
    creates a dictionary of a deck of cards and their black jack value
    """      
    #global Deck_dict
    for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]: # s suits
        for number in range(13):                          # ace to king
            #card = f"{number} of {suit}"                 # key for dicts
            number +=1
            n = number
            #number = str(number)

            if number == 11:
                n = 10
                number = "Jack"
                Cards(number, suit, n)
            elif number == 12:
                n = 10
                number = "Queen"
                Cards(number, suit, n)
            elif number == 13:
                n = 10
                number = "King"
                Cards(number, suit, n)
            elif number == 1:
                number = "Ace"
                n = 11
                card = f"{number} of {suit}"
                Deck_dict[card] = n
                n = 1
                card = f"{number} of {suit}"
                Deck_dict_Ace[card] = n   
            else:
                card = f"{number} of {suit}"
                Deck_dict[card] = n
                Deck_dict_Ace[card] = n
    return
def Cards(number, suit, n):                 #creates the name for the cards
     card = f"{number} of {suit}"
     Deck_dict[card] = n
     Deck_dict_Ace[card] = n     
     return
def Deal(Deck_1, Deck_2, Hand, Score):      #creates the hands 
    """
    deals a card, removes from dict so it cant be redelt
    """    
    Deck = Deck_1
    for i in range(2):
        deal = random.choice(list(Deck.keys()))
        Hand.append(deal)
        Score.append(Deck[deal])
        del Deck_1[deal]
        del Deck_2[deal]
        if sum(Score) > 10:
            Deck = Deck_2
        else:
            continue
    return 
def Display():                              #creates the displays
    """
    creates the users interface
    
    """
    sum_of_player_score = sum(Player_score)
    sum_of_computer_score = sum(Computer_score)
    if PLayers_turn is True:
        print(f" \n"
              f" \n"
              f" \n"
              f"              Players hand\n"
              f" \n"
              f"           score: {sum_of_player_score}\n"
              f" \n"
                f"{Players_hand}\n"
                f" \n"
                f"--------------------------------------------------------------\n"
                f" \n"
                f"             Computers hand"
                f" \n"
                f"           score: ?\n"
                f" \n"
                f"{Computers_hand[0]}, ?\n"
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
              f"           score: {sum_of_player_score}\n"
              f" \n"
                f"{Players_hand}\n"
                f" \n"
                f"--------------------------------------------------------------\n"
                f" \n"
                f"             Computers hand"
                f" \n"
                f"           score: {sum_of_computer_score}\n"
                f" \n"
                f"{Computers_hand}\n"
                f" \n"
                f"--------------------------------------------------------------\n"
                f" \n"
                f" \n"
                f" \n")
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
def Hit(Deck_1, Deck_2, Score, Turn):
    """
    adds another card to players hand
    """ 
    # global Player_score 
    # global Computer_score
    global Players_hand
    global Computers_hand
    # global PLayers_turn
    if sum(Score) > 10:
        Deck = Deck_2
    else:
        Deck = Deck_1
        
    
    if PLayers_turn is True:
        deal = random.choice(list(Deck_dict.keys()))
        #print(deal)
        Players_hand.append(deal)
        Score.append(Deck[deal])
        del Deck_dict[deal]

        return
    elif PLayers_turn is False:
        deal = random.choice(list(Deck_dict.keys()))
        #print(deal)
        Computers_hand.append(deal)
        Score.append(Deck[deal])
        del Deck_dict[deal]
        return
def Check_score(Hand, Score):
    global Player_score
    global Computer_score
    global Player_status
    if Score == 21:        
        return "WIN"    
    elif Score > 21:
        Score = Ace_check(Hand, "p")       
        if Score > 21:
            Player_status = 21
            return False  
        else:
            return True
    elif Score < 21:        
        return True
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
def Clear():
    """
    clears everything to start a new game 
    """
    global Player_score 
    global Computer_score
    global Players_hand
    global Computers_hand
    global PLayers_turn
    global Deck_dict_Ace
    Deck_dict.clear()
    Deck_dict_Ace.clear()
    Player_score = []
    Players_hand = []
    Computer_score = []
    Computers_hand = []
    PLayers_turn = True
def Ace_check(Score, Player):
    """
    if scores are over 21, this func is called, it checks for aces in the score 
    if so it removes 10 points from score
    """
    print('doing ace check')
    global Player_score
    global Computer_score
    Sum = sum(Score) 
    
    if 11 in Score:
        if Player == 'p':
        
            Player_score.remove(11)
            Player_score.append(1)
            Sum = sum(Player_score)
            Display()
            return Sum
        elif Player == 'c':
            Computer_score.remove(11)
            Computer_score.append(1)
            Sum = sum(Computer_score)
            Display()            
            return Sum        
    else:
        return Sum
            
        
Start_game()
            
            
            
            
            
            
            