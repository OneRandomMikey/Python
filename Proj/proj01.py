#Computer Project #01
#section 730.
#May 22,2016
    #input a int
    #ten's digit is as large as ones digit and hundreds's digit.
    #find different between tens and ones then between tens and hundreds.
    #print the result.

#user input
num_int=int(input('Please enter a 3-digit number.''\nThe tens digit should ba at least as large as the ones and hundreds digits''\n'))
hud_ten=num_int%100//10-num_int//100    #find difference between tens digit and hundreds digit
ten_one=num_int%100//10-num_int%10      #find difference between tens digit and ones digit
#print the result
print ('\nI am a 3-digit number.','\nMy tens digit is ',ten_one,' more than my ones digit.''\nMy hundreds digit is ',hud_ten,' less than my tens digit.\n''\nWhat number am I?')
