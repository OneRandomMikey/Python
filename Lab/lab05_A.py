

vowels='aeiou'
op_file=open("dictionary.txt",'r')
for line in op_file:
    word=''
    count=0
    for x in line:
        if x in vowels:
            word+=x
            count+=1
    if count==5 and word=='aeiou':

        print (line)
op_file.close()
