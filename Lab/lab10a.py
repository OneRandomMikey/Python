
import string
from operator import itemgetter
def add_word( word_map, word ):
    """
    count how many times does each word appear in the file
    """
# check if the word is in the dict or not, if it is not the value for the key word will be 0
    if word:
        if word in word_map:
            word_map[word]+=1
        else:
            word_map[word]=1
# if the word is in the word_map, the value of word will increase by 1
    #word_map[ word ] += 1
def build_map( in_file, word_map ):
    """
    read the file.
    creat a list.
    rid of all the punctuation
    run the add_word function.
    get the each word and how many times does each word appear in the fiel
    """
    for line in in_file:
# turn the file to a list
        word_list = line.split()
        for word in word_list:
# rid of all the punctuation
            word = word.lower().strip().strip(string.punctuation)
            add_word( word_map, word )
def display_map( word_map ):
    """
    creat a list that contain the each key and the value of each key.
    sort a list sort a list alphabetically by name but does not change the origonal list
    print all the word and the frequence
    """
    word_list = list()
# read the items in the word_map and word is the key in dict and count is the value in dict
    for word, count in word_map.items():
        word_list.append( (word, count) )
    word_list.sort()
# sort a list alphabetically by name but does not change the origonal list
    freq_list = sorted(word_list,key=itemgetter(1),reverse=True)
    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )
def open_file():
    """
    open the file.
    error checking.
    return the open file
    """
    try:
        in_file = open(input('Please enter a file name:'))
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None
    return in_file
word_map = dict()
in_file = open_file()
if in_file != None:
    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()







def build_word_index( input_file ):

    word_map = {}
    line_no = 0
    #word_list=[]
    for line in input_file:
        word_lst=line.strip().split()
        word_lst = [w.lower().strip(string.punctuation) for w in word_lst]
        line_no+=1
        for word in word_lst:
            if word not in word_map:
                if word !='':
                    word_map[word]=set()

            if word!='':
                word_map[word].add(line_no)

            #if word not in word_list:
                #if word!='':
                #    word_map[word].add(line_no)
                    #word_list.append(word)
            #if word in word_list:
                #word_map[word].add(line_no)

    return word_map
