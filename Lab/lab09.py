def open_file():
    while True:
        try:
            of=open(input('Enter a file name:'))
            break
        except:
            print('\nPlease enter a corret filename')
            continue
    return of
a_list=[]
a_file=open_file()
for i in a_file:
    i=i.strip()
    if i.isdigit():
        list_a=i.split()
        a_list.append(i)
number_list=[0,0,0,0,0,0,0,0,0,0]
total=0
for i in a_list:
    first_digit=i[0][0]
    number_list[int(first_digit)]+=1
    total+=1
print ('{:5s}'.format('\nDigit'),'{:>10s}'.format('Percent'),'{:>10s}'.format('Benford\n'),\
'{:>5s}'.format('1:'),'{:8.1f}{:1}'.format(number_list[1]/(total-number_list[0])*100,'%'),'{:>10s}'.format('(30.1%)\n'),\
'{:>5s}'.format('2:'),'{:8.1f}{:1}'.format(number_list[2]/(total-number_list[0])*100,'%'),'{:>10s}'.format('(17.6%)\n'),\
'{:>5s}'.format('3:'),'{:8.1f}{:1}'.format(number_list[3]/(total-number_list[0])*100,'%'),'{:>10s}'.format('(12.5%)\n'),\
'{:>5s}'.format('4:'),'{:8.1f}{:1}'.format(number_list[4]/(total-number_list[0])*100,'%'),'{:>10s}'.format('( 9.7%)\n'),\
'{:>5s}'.format('5:'),'{:8.1f}{:1}'.format(number_list[5]/(total-number_list[0])*100,'%'),'{:>10s}'.format('( 7.9%)\n'),\
'{:>5s}'.format('6:'),'{:8.1f}{:1}'.format(number_list[6]/(total-number_list[0])*100,'%'),'{:>10s}'.format('( 6.7%)\n'),\
'{:>5s}'.format('7:'),'{:8.1f}{:1}'.format(number_list[7]/(total-number_list[0])*100,'%'),'{:>10s}'.format('( 5.8%)\n'),\
'{:>5s}'.format('8:'),'{:8.1f}{:1}'.format(number_list[8]/(total-number_list[0])*100,'%'),'{:>10s}'.format('( 4.1%)\n'),\
'{:>5s}'.format('9:'),'{:8.1f}{:1}'.format(number_list[9]/(total-number_list[0])*100,'%'),'{:>10s}'.format('( 4.6%)\n'))
a_file.close()
