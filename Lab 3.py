# substringResal(sentence, word)
#
# sentence: "Hello and welcome to the lab"
# word: "lab"
#
# output: "Hello and welcome to the bal"

# Challenge: empty inputs, non existence words, '
# Challenge 2: Multiple
# -------------------------------------
# The idea is to locate the position of the word, reverse the word,
# then adding the sentence before and after the "word" in "sentence"
# As known as slicing
def asking_for_sentence(): # Directly taking inputs from user.
    s = input("What's your sentence? ")
    if s == "":
        return asking_for_sentence()
    else:
        return s
def asking_for_word(): # Directly taking inputs from user.
    x = input("Reverse word? ")
    return x
def empty_string_check(string): #check for empty string
    count = 0
    for i in string:
        if i == " ":
            count += 1
    if count == len(string):
        return True # True if whole string is empty
    else:
        return False
def substringResal():
    sentence = asking_for_sentence() #Directly take input from user, from other function
    word = asking_for_word()
    while word not in sentence: # In case user input not valid
        if not empty_string_check(word): # Check if there's empty string, if not, re ask for input
            print('Word not in sentence. Try again? ')
            word = asking_for_word() # Re ask for word
        else:
            print(sentence) # If empty string, no matter how many empty string, print the result
            exit(0)
    index_position = sentence.index(word)  # Look for the position of the "word" we're looking for
    inverted_word = ""
    leng_word = len(word) # Find the length of the word to invert it
    leng_sentence = len(sentence) # Find the length of the sentence
    beginning_sentence = sentence[0:index_position] #Before the word
    end_sentence = sentence[index_position+leng_word:leng_sentence] # After the word
    index_word = sentence[index_position:index_position+leng_word] # Looking for the word
    inverted_word = index_word[::-1] # The reverse the word
    print(beginning_sentence + inverted_word + end_sentence) # Return result
    return exit(0) # Not sure about this, Harley told us to use so I put it in to end the thing. Is this necessary ?

substringResal()