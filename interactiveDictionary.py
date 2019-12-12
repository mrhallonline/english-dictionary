import json
import os
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

os.chdir('D:\Dropbox\CodingResources\webDevelopmentProjects\Python\PythonMegaCourse\interactiveEnglishDictionary')

#open and read from json database
with open('data.json') as di:
        corpus = json.load(di)



#function to look up user inputted word
#check if word is valid to avoid traceback error before reading from database
def lookup_word(word):
    if user_word in corpus: 
        return corpus[word]
    elif len(get_close_matches(user_word, corpus, n=3, cutoff=0.8)) > 0:
        close_word = get_close_matches(user_word, corpus, n=3, cutoff=0.8)[0]
        return "Did you mean to type " + close_word + '?'
    else:
        return "Doesn't match any words in dictionary. Check spelling"
    
    
#ask for user input and makes all lowercase
user_word = (input("Enter word to define: ")).lower()

#difflib sequence SequenceMatcher
# SequenceMatcher(None, "rainn", "rain").ratio()





print(lookup_word(user_word))
