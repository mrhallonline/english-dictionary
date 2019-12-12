import json
import os

os.chdir('D:\Dropbox\CodingResources\webDevelopmentProjects\Python\PythonMegaCourse\interactiveEnglishDictionary')

with open('data.json') as di:
        corpus = json.load(di)


def lookup_word(word):
        return corpus[word]

user_word = input("Enter word to define: ")
if user_word in corpus:        
    print(lookup_word(user_word))
else:
    print("Doesn't match any words in dictionary. Check spelling")