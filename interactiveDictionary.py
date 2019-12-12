import json
import os

os.chdir('D:\Dropbox\CodingResources\webDevelopmentProjects\Python\PythonMegaCourse\interactiveEnglishDictionary')

def lookup_word(word):
    with open('data.json') as di:
        corpus = json.load(di)
        print( corpus[word])

user_word = input("Enter word to define: ")        
lookup_word(user_word)