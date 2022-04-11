#write code to intalize the words class and retrieve words and points 

import json
import random
from flask import jsonify
from flask_wtf import FlaskForm
from wtforms import StringField,HiddenField,SubmitField

from App.database import db
from App.models import (ThreeWords,FourWords,FiveWords)

def init_words():
    with open ("App/models/3-letter-words.json") as file:
        jsonData = json.load(file)
        for i in range(0,len(jsonData)):
             dictToSingle = (jsonData[i])
             createWords(i+ 1, dictToSingle["word"] , len(dictToSingle["word"]),len(dictToSingle["word"]))
            
    with open ("App/models/4-letter-words.json") as file:
        jsonData = json.load(file)
        for i in range(0,len(jsonData)):
            createWords(i+1, jsonData[i]["word"] , len(jsonData[i]["word"]),  len(jsonData[i]["word"]))

    with open ("/models/5-letter-words.json") as file:
        jsonData = json.load(file)
        for i in range(0,len(jsonData)):
            createWords(i + 1,jsonData[i]["word"] , len(jsonData[i]["word"]),  len(jsonData[i]["word"]))
    

def createWords(id, word,points,length):
    if length == 3:
        newWord = ThreeWords(id = id ,word = word, points = points)
    elif length == 4:
        newWord = FourWords(id = id , word = word, points = points)
    elif length == 5:
        newWord = FiveWords(id = id, word = word, points = points)
    else:
        return "Error"
    db.session.add(newWord)
    db.commit()

def getWord(id,length):
    if length == 3:
        return ThreeWords.query.filterBy(id = id).first()
    elif length == 4:
        return FourWords.query.filterBy(id = id).first()
    elif length == 5:
        return FiveWords.query.filterBy(id = id).first()
    else:
        return []

