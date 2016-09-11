color='RYBGWO'
history=''
key=input('Input the secret key (RYBGWO):')
print('\nMastermind: your challenge is to guess the secret key.\nThere are six colors with no repeats: RYBGWO.')
guess=input('\nInput your guess (RYBGWO):').upper()
total_guess=0
while guess!='':


    correct=0
    count=0
    half_correct=0
    if not(len(guess)==4 and guess.isalpha() and guess[0] in color and guess[1] in color and guess[2] in color and guess[3] in color):
        guess=input('\nBad guess so inpt another guess (RYBGWO):').upper()
        continue
    for i in color:
        count= guess.count(i)
        if count >1:
            break
    if count>1:
        guess=input('\nBad guess so inpt another guess (RYBGWO):').upper()
        continue

    total_guess+=1
    if guess==key.upper():
        if total_guess==1:
            print('You won','\nIt took',total_guess,'guess')
            break
        else:
            print('You won','\nIt took',total_guess,'guesses')
            break





    for a,ch in enumerate(guess):

        if ch==key[a].upper():
            correct+=1
    print ('Correct color and position count:',correct)

    for i in key.upper():
        if i in guess:
            half_correct+=1

    print('Correct color, but wrong position count:',half_correct-correct)


    history+='\n'+guess
    print ('History:',history)


    print('Guesses(out of 8):',total_guess)
    if total_guess==8:
        print('\nYou lose: too many guesses.','\nThe key is',key.upper())
        break
    guess=input('\nInput your guess (RYBGWO):').upper()












    color='RYBGWO'
    history=''
    key=input('Input the secret key (RYBGWO):')
    print('Mastermind: your challenge is to guess the secret key.\nThere are six colors with no repeats: RYBGWO')
    guess=input('Input your guess (RYBGWO):').upper()
    total_guess=0
    while guess!='':
        correct=0
        count=0
        half_correct=0
        if not(len(guess)==4 and guess.isalpha() and guess[0] in color and guess[1] in color and guess[2] in color and guess[3] in color):
            guess=input('Bad guess so inpt another guess (RYBGWO):').upper()
            continue
        for i in color:
            count= guess.count(i)
            if count >1:
                break
        if count>1:
            guess=input('Bad guess so inpt another guess (RYBGWO):').upper()
            continue

        for a,ch in enumerate(guess):

            if ch==key[a].upper():
                correct+=1
        print ('Correct color and position count:',correct)

        for i in key.upper():
            if i in guess:
                half_correct+=1

        print('Correct color, but wrong position count:',half_correct-correct)


        history+='\n'+guess
        print ('History:',history)
        guess=input('Guess:').upper()
        total_guess+=1
        print('Guesses(out of 8):',total_guess)
        if guess==key.upper():
            print('You won','\nIt took',total_guess,'guesses')
            break
        if total_guess==8:
            print('You lose: too many guesses.','\nThe key is',key.upper)
