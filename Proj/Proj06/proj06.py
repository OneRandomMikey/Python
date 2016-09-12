#Computer Project #06
#section 730
#June 27,2016
#The program should deal two cards to two players (one card to each player, then a second card to each
#player), and then five community cards which players share to make their hands. A poker hand is the
#best five cards from the community cards plus the player’s cards (i.e., best 5 out of 7 cards total). The
#goal of this assignment is to find the category of each player’s hand and determine the winner.
import cards
# function built a dictionary that the key is the rank and the value is the suit
def build_rank_D(H):
    D={}
    for i in H:
        key=i.rank()
        if key not in D:
            D[key]=[]
        if key in D:
            D[key].append(i)
    return D
#function bulit a dictionary that the key is the suit and the value is the rank
def build_suit_D(H):
    D={}
    for i in H:
        key=i.suit()
        if key not in D:
            D[key]=[]
        if key in D:
            D[key].append(i)
    return D
# function that test the possible for straight flush
def straight_flush(H):
    D={}
    D2={}
    for i in H:
        key=i.suit()
        if key not in D:
            D[key]=[]
            D2[key]=[]
        if key in D:
            D[key].append(i.rank())
            D2[key].append(i)
    for k,v in D2.items():
        if len(v)==5:
            win=v
        if len(v)==6:
            win=v
        if len(v)==7:
            win=v
    for k,v in D.items():
        if len(v)==5:
            if v[0]==v[1]-1 and v[1]==v[2]-1 and v[2]==v[3]-1 and v[3]==v[4]-1:
                return win
        if len(v)==6:
            if v[0]==v[1]-1 and v[1]==v[2]-1 and v[2]==v[3]-1 and v[3]==v[4]-1:
                return win[0:5]
            elif v[1]==v[2]-1 and v[2]==v[3]-1 and v[3]==v[4]-1 and v[4]==v[5]-1:
                return win[1:6]
        if len(v)==7:
            if v[0]==v[1]-1 and v[1]==v[2]-1 and v[2]==v[3]-1 and v[3]==v[4]-1:
                return win[0:5]
            elif v[1]==v[2]-1 and v[2]==v[3]-1 and v[3]==v[4]-1 and v[4]==v[5]-1:
                return win[1:6]
            elif v[2]==v[3]-1 and v[3]==v[4]-1 and v[4]==v[5]-1 and v[5]==v[6]-1:
                return win[2:7]
    return []
# function that test the possible for four of kind
def four(H):
    D=build_rank_D(H)

    for k,v in D.items():
        if len(v)==4:
            return v
    return []
# function that test the possible for full house
def full_house(H):
    D=build_rank_D(H)
    count=0
    count_pair_2=0
    count_pair_3=0
    for k,v in D.items():
        if len(v)==2 and count_pair_2==0:
            count+=1
            count_pair_2+=1
            pair_2=v
            continue
        if len(v)==3 and count_pair_3==0:
            count+=1
            count_pair_3+=1
            pair_3=v
            continue
        if len(v)==3 and count_pair_3==1:
            count+=1
            pair_2=v[0:2]
    if count==2:
        return (pair_3+pair_2)
    return []
# function that test the possible for flush
def flush(H):
    D=build_suit_D(H)
    for k,v in D.items():
        if len (v)==5:
            return v
    return []
# function that test the possible for straight
def straight(H):
    D=build_rank_D(H)
    a_list=[]
    card_list=[]
    for key in D:
        a_list.append(key)
    a_list.sort()
    for values in D.values():
        if len(D)==7:
            card_list+=values
        if len(D)==6:
            if len(values)==1:
                card_list+=values
            if len(values)==2:
                card_list.append(values[0])
        if len(D)==5:
            if len(values)==1:
                card_list+=values
            if len(values)==3:
                card_list.append(values[0])
    card_list.sort()
    if len(D)==7:
        if a_list[0]==a_list[1]-1 and a_list[1]==a_list[2]-1 and a_list[2]==a_list[3]-1 and a_list[3]==a_list[4]-1:
            return card_list[0:5]
        elif a_list[1]==a_list[2]-1 and a_list[2]==a_list[3]-1 and a_list[3]==a_list[4]-1 and a_list[4]==a_list[5]-1:
            return card_list[1:6]
        elif a_list[2]==a_list[3]-1 and a_list[3]==a_list[4]-1 and a_list[4]==a_list[5]-1 and a_list[5]==a_list[6]-1:
            return card_list[2:7]
    if len(D)==6:
        if a_list[0]==a_list[1]-1 and a_list[1]==a_list[2]-1 and a_list[2]==a_list[3]-1 and a_list[3]==a_list[4]-1:
            return card_list[0:5]
        if a_list[1]==a_list[2]-1 and a_list[2]==a_list[3]-1 and a_list[3]==a_list[4]-1 and a_list[4]==a_list[5]-1:
            return card_list[1:6]
    if len(D)==5:
        if a_list[0]==a_list[1]-1 and a_list[1]==a_list[2]-1 and a_list[2]==a_list[3]-1 and a_list[3]==a_list[4]-1:
            return card_list[0:5]
    return []
# function that test the possible for three of kind
def three_kind(H):
    D=build_rank_D(H)
    count=0
    count_pair_3=0
    for k,v in D.items():
        if len(v)==3:
            pair_3=v
            count_pair_3+=1
            continue
        if count==1:
            pair_1_b=v
            count+=1
        if count==0:
            pair_1_a=v
            count+=1
    if count==2 and count_pair_3==1:
        return (pair_3+pair_1_a+pair_1_b)
    return[]
# function that test the possible for two pairs
def two_pair(H):
    D=build_rank_D(H)
    count=0
    for k,v in D.items():
        if len(v)==2 and count==0:
            pair_2_a=v
            count+=1
            continue
        if len(v)==2 and count==1:
            pair_2_b=v
            count+=1
    if count==2:
        return (pair_2_a+pair_2_b)
    return []
# function that test the possible for one pair
def one_pair(H):
    D=build_rank_D(H)
    for k,v in D.items():
        if len(v)==2:
            return v
    return[]
#read the card
the_deck=cards.Deck()
#shuffle 52 cards
the_deck.shuffle()
#the loop that run in 52 cards
while True:
    player1_list=[]
    player2_list=[]
    #in a for loop, creat list of hand for both players
    for i in range (2):
        player1_list.append(the_deck.deal())
        player2_list.append(the_deck.deal())
    community_list=[]
    #in a for loop, creat a list of cards on deck
    for i in range (5):
        community_list.append(the_deck.deal())
    print ('------------------------------------',"\nLet's play poker!\n","\nCommunity cards:",community_list,'\nPlayer1:',player1_list,'\nPlayer2:',player2_list)
    H1=community_list+player1_list
    H2=community_list+player2_list
    rank_list1=['x','Hight card',one_pair(H1),two_pair(H1),three_kind(H1),straight(H1),flush(H1),full_house(H1),four(H1),straight_flush(H1)]
    rank_list2=['x','High card',one_pair(H2),two_pair(H2),three_kind(H2),straight(H2),flush(H2),full_house(H2),four(H2),straight_flush(H2)]
    rank_list=['x','High card','one pair','two pairs','three of a kind','straight','flush','full house','four of kind','straight flush']
    for i in range(8,0,-1):
        if rank_list1[i]!=[]:
            rank1=i
            break
    for i in range(8,0,-1):
        if rank_list2[i]!=[]:
            rank2=i
            break
    #check who has bigger hands
    if rank1>rank2:
        print('\nPlayer 1 wins with a',rank_list[rank1],':', rank_list1[rank1])
    if rank2>rank1:
        print('\nPlayer 2 wins with a',rank_list[rank2],':', rank_list2[rank2])
    if rank1==1 and rank2==1:
        D=build_rank_D(H1)
        height_list=[]
        for k,v in D.items():
            height_list.append((k,v))
        height_list.sort()
        print('\nTIE with High Card:',height_list[-1][-1])
    if rank1==rank2 and rank1!=1:
        print('\nTIE with a',rank_list[rank2],':',rank_list1[rank1])
    # check for how many cards on deck, if the cards are less than 9, quit the game
    if len(the_deck)<9:
        print('Deck has too few cards so game is done.')
        break
    # ask for players, do they want to play next hand
    ipt=input('\nDo you wish to play another hand?(Y or N)')
    if ipt.lower()=='y':
        continue
    else:
        print('The player quit the game.')
        break
