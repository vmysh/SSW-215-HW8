def word_count():

    with open('alice.txt') as file_object:
        lines = file_object.readlines()  #creates a list (array) of lines of the text

    new_string = '' #initializing a new empty string
    for line in lines:
        new_string += line.rstrip() 
        #removes the whitespace at the end of every line 
        #and adds that line to the string

    return new_string.count(" ") #counts the number of spaces in the string
    #the number of spaces is approximately the same as the number of words

print("The file alice.txt has about", word_count(), "words.")