
import string

def build_word_set( input_file ):

    word_set = set()

    for line in input_file:

        # rid of white space
        word_lst = line.strip().split()

        # create a list that is lower case and strip any punctuation
        word_lst = [w.lower().strip(string.punctuation) for w in word_lst]

        for word in word_lst:

            if word != "":

                # add word into set
                word_set.add( word )

    return word_set


def compare_files( file1, file2 ):
    count=0
    # Build two sets:
    #   all of the unique words in file1
    #   all of the unique words in file2
    file1_set=build_word_set(file1)
    file2_set=build_word_set(file2)
    print (len(file1_set))
    # Display the total number of unique words between the
    # two files.  If a word appears in both files, it should
    # only be counted once.
    print('Total number of unique words between the two files:',len(file1_set | file2_set))
    # Display the number of unique words which appear in both
    # files.  A word should only be counted if it is present in
    # both files.
    print ('The number of unique words which appear in both files:',len(file1_set&file2_set))

######################################################################

f1 = open("document1.txt")
f2 = open( "document2.txt" )

compare_files( f1, f2 )

f1.close()
f2.close()
