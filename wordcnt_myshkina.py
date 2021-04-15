def word_count():
   
    #creates a list (array) of lines of the text
    with open('alice.txt') as file_object:
     Working
        lines = file_object.readlines()  #creates a list (array) of lines of the text

    #initialize a new empty string
    new_string = ''
    for line in lines:
        new_string += line.rstrip() 
        #removes the whitespace at the end of every line and adds that line to the string

    return new_string.count(" ") #counts the number of spaces in the string
    #the number of spaces is approximately the same as the number of words

        lines = file_object.readlines()  
    
    #initializing a new empty string
    new_string = '' 
    
    #removes the whitespace at the end of every line 
    #and adds that line to the string
    for line in lines:
        new_string += line.rstrip() 
       
    #counts the number of spaces in the string the number of spaces is
    # approximately the same as the number of words
    return new_string.count(" ") 
        main

print("The file alice.txt has about", word_count(), "words.")

#           CODE REVIEW
#  overall I think this code is very succinct and well executed.
#  I don't think there is much for me to improve on, maybe just
#  cleaning up the comments.
