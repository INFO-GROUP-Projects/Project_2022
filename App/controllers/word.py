#write code to intalize the words class and retrieve words and points 

import json
import random


from App.database import db
from App.models import (ThreeWords,FourWords)

def createWords(id, word,points,length):
    if length == 3:
        newWord = ThreeWords(id = id ,word = word, points = points)
    elif length == 4:
        newWord = FourWords(id = id , word = word, points = points)
    else:
        return "Error"
    db.session.add(newWord)
    db.session.commit()

def init_words():
    with open ("App/models/3-letter-words.json") as file:
        jsonData = json.load(file)
        for i in range(0,len(jsonData)):
            createWords(i+1, jsonData[i]["word"] ,len(jsonData[i]["word"]),  len(jsonData[i]["word"]))
            
    with open ("App/models/4-letter-words.json") as file:
        jsonData = json.load(file)
        for i in range(0,len(jsonData)):
            createWords(i+1, jsonData[i]["word"] ,len(jsonData[i]["word"]),  len(jsonData[i]["word"]))
    

def getWord(id,length):
    if length == 3:
        return ThreeWords.query.filterBy(id = id).first()
    elif length == 4:
        returnQuery =  FourWords.query.filter_by(id = id).first()
        return returnQuery.to_dict()
    else:
        return []

def getWordRand():
    random.seed()
    index = random.randrange(1,4176)
    return getWord(index,4)



