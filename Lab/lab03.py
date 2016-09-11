odds_sum=0
evens_sum=0
odds_count=0
evens_count=0
total_int_count=0
while True:
    inp=int(input('Input a integer(0 terminaes):'))
    if inp==0:
        break
    elif inp<0:
        print ('Error,please enter a positive number')
        continue
    elif inp%2==0:
        evens_count+=1
        evens_sum+=inp
    else:
        odds_count+=1
        odds_sum+=inp
    total_int_count+=1


print('\nsum of odds:',odds_sum,'\nsum of evens:',evens_sum,'\nodd count:',odds_count,'\neven count:',evens_count,'\ntotal positive int count:',total_int_count)
