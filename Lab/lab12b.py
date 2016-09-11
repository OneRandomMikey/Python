
import cards

the_deck = cards.Deck()
the_deck.shuffle()


player1_list=[]
player2_list=[]

for i in range( 26 ):
    player1_list.append( the_deck.deal())
    player2_list.append( the_deck.deal())
print ('Stack of cards of player # 1: ', player1_list)
print('Stack of cards of player # 2: ',player2_list,'\n')

count=0
while True:
    count+=1
    print('Round ',count)
    player1_card=player1_list.pop(0)
    player2_card=player2_list.pop(0)
    print('Card played by player # 1: ',player1_card)
    print('Card played by player # 2: ',player2_card)

    if player1_card.rank()==player2_card.rank():
        player1_list.append(player1_card)
        player2_list.append(player2_card)
        print ('\n',player1_card,' and ',player2_card," have same value.\nReturn both cards to plyear's hand" )
        
    elif 1==player1_card.rank():
        player1_list.append(player1_card)
        player1_list.append(player2_card)
      
        print('\n',player1_card,' has higher rank than ',player2_card,'\nplayer # 1 won this battle')
        
    elif 1==player2_card.rank():
        player2_list.append(player2_card)
        player2_list.append(player1_card)
       
        print('\n',player2_card,' has higher rank than ',player1_card,'\nplayer # 2 won this battle')
    elif player1_card.rank()>player2_card.rank():
        player1_list.append(player1_card)
        player1_list.append(player2_card)
        
        print('\n',player1_card,' has higher rank than ',player2_card,'\nplayer # 1 won this battle')
    elif player2_card.rank()>player1_card.rank():
        player2_list.append(player2_card)
        player2_list.append(player1_card)
        
        print('\n',player2_card,' has higher rank than ',player1_card,'\nplayer # 2 won this battle')
    if len(player1_list)==0:
        print('\nPlayer # 2 won the war')
        break
    if len(player2_list)==0:
        print('\nPlayer # 1 won the war')
        break
    print('\nStack of cards of player # 1: ',player1_list)
    print('Stack of cards of player # 2: ',player2_list,'\n')
    ipt=input("Do you want to continue? \nIf you want to quit the game,please enter 'quit'.\nIf you want to continue,press Enter key.\n")
    if ipt.lower()=='quit':
        if len(player1_list)>len(player2_list):
            print ('\nWinner is player # 1')
        if len(player2_list)>len(player1_list):
            print ('\nWinner is player # 2')
        if len(player1_list)==len(player2_list):
            print('\nNo winner, two players have same amount of cards')
        break
    