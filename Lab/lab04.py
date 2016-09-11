VOWELS='aeiou'
while True:
    ipt=input('Please enter a word you want to convert to Pig Latin form:')
    if ipt.lower()=='quit':
        break
    elif ipt[0] in VOWELS:
        vword=ipt+'way'
        print ('Pig Latin form:',vword)
    else:
        while True:
            if ipt[0] in VOWELS:
                break
            else:
                first_char=ipt[0]
                rest_char=ipt[1:]
                ipt=rest_char+first_char
        ipt=ipt+'ay'
        print ('Pig Latin form:',ipt)
print ('Thank you for using')
