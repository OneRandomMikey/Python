
#Computer Project #03
#section 730
#June 6, 2016
#input a Key that is 4 char
#have 8 chance to guess what is the key
color='RYBGWO'
history=''
#input a key
key=input('Input the secret key (RYBGWO):')
#describetion of the game
print('\nMastermind: your challenge is to guess the secret key.\nThere are six colors with no repeats: RYBGWO.')
#start to input your guess
guess=input('\nInput your guess (RYBGWO):').upper()
total_guess=0
while guess!='':
    correct=0
    count=0
    half_correct=0
    #check the guess is 4 char, the guess is alpha and the letter of the guess is in the range of color
    if not(len(guess)==4 and guess.isalpha() and guess[0] in color and guess[1] in color and guess[2] in color and guess[3] in color):
        guess=input('\nBad guess so inpt another guess (RYBGWO):').upper()
        #return to the top of the loop
        continue
    #check there is no repeat letter in the guess
    for i in color:
        count= guess.count(i)
        if count >1:
            # if there are repeat letters, get out of the for loop
            break
    # go back to the top of the loop if there are repeat letters
    if count>1:
        guess=input('\nBad guess so inpt another guess (RYBGWO):').upper()
        continue

    total_guess+=1
    #check the guess and key match
    if guess==key.upper():
        if total_guess==1:
            print('You won','\nIt took',total_guess,'guess')
            break
        else:
            print('You won','\nIt took',total_guess,'guesses')
            break
    #check how many letter that is the same and at the same position
    for a,ch in enumerate(guess):
        if ch==key[a].upper():
            correct+=1
    print ('Correct color and position count:',correct)
    #check for the same letter but different position
    for i in key.upper():
        if i in guess:
            half_correct+=1
    print('Correct color, but wrong position count:',half_correct-correct)
    history+='\n'+guess
    print ('History:',history)
    print('Guesses(out of 8):',total_guess)
    # check if player do not get right answer in 8 chances, the player lose the game
    if total_guess==8:
        print('\nYou lose: too many guesses.','\nThe key is',key.upper())
        break
    guess=input('\nInput your guess (RYBGWO):').upper() 
