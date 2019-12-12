import json
import os

os.chdir('D:\Dropbox\CodingResources\webDevelopmentProjects\Python\PythonMegaCourse\interactiveEnglishDictionary')

data = json.load(open("data.json"))
print(data['rain'])

def 