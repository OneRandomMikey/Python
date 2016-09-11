def squares(n,p):
    sum_1=0
    for x in range(p):
        sum_1+=n**2
        n+=1
    return sum_1
def cubes(n,p):
    sum_1=0
    for x in range(p):
        sum_1+=n**3
        n+=1
    return sum_1
while True:
    command=input('Pleaes enter a command:')
    if command =='squares':
        n=int(input('Please enter the first number:'))
        p=int(input('Please enter the second number'))
        print (squares(n,p))
    elif command=='cubes':
        n=int(input('Please enter the first number:'))
        p=int(input('Please enter the second number:'))
        print (cubes(n,p))
    elif command == 'exit':
        print('Program halted normally')
        break
    else:
        print('***Invalid Choice ***')
