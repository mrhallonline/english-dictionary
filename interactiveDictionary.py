import json
import os
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

os.chdir('D:\Dropbox\CodingResources\webDevelopmentProjects\Python\PythonMegaCourse\interactiveEnglishDictionary')

#open and read from json database
with open('data.json') as di:
        corpus = json.load(di)


#convert list to string and newlines
def list_to_string(old_list):
    new_string = old_list
    return new_string

#function to look up user inputted word
#check if word is valid to avoid traceback error before reading from database
def lookup_word(word):
    if user_word in corpus: 
        definition = corpus[word]
        return list_to_string(definition)
         
    elif len(get_close_matches(user_word, corpus, n=3, cutoff=0.8)) > 0:
        close_word = get_close_matches(user_word, corpus, n=3, cutoff=0.8)[0]
        user_answer = (input("Did you mean to type %s? Enter Y for yes, or N for no: "%close_word)).lower()
        if user_answer == 'y':
            return corpus[close_word]
        elif user_answer == 'n':
            return "Sorry %s doesn't match any other words in the dictionary. Check spelling and try again" %word
        else:
            return "Sorry that wasn't one of the options."
    else:
        return "Doesn't match any words in dictionary. Check spelling"
    
    
#ask for user input and makes all lowercase
user_word = (input("Enter word to define: ")).lower()


prelist = (lookup_word(user_word))
if type(prelist) == list:
    for item in prelist:
        print(item)
else:
    print(prelist)
