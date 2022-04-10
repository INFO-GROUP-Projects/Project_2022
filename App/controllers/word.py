#write code to intalize the words class and retrieve words and points 

import json
import random
from flask import jsonify
from flask_wtf import FlaskForm
from wtforms import StringField,HiddenField,SubmitField

from App.database import db
from App.models import threeLetterWords,fourLetterWords,fiveLetterWords

def init_words():
    with open ("/models/3-letter-words.json") as file:
        jsonData = json.load(file)
        for i in jsonData:
            createWords(jsonData[i].word , jsonData[i].word.length, jsonData[i].word.length)
            
    with open ("/models/4-letter-words.json") as file:
        jsonData = json.load(file)
        for i in jsonData:
            createWords(jsonData[i].word , jsonData[i].word.length, jsonData[i].word.length)

    with open ("/models/5-letter-words.json") as file:
        jsonData = json.load(file)
        for i in jsonData:
            createWords(jsonData[i].word , jsonData[i].word.length, jsonData[i].word.length)
    

def createWords(word,points,length):
    if length == 3:
        newWord = ThreeWord(word = word, points = points)
    elif length == 4:
        newWord = FourWord(word = word, points = points)
    elif length == 5:
        newWord = FiveWord(word = word, points = points)
    else:
        return "Error"
    db.session.add(newWord)
    db.commit()

def getWord(id,length):
    if length == 3:
        return ThreeWord.query.filterBy(id = id).first()
    elif length == 4:
        return FourWord.query.filterBy(id = id).first()
    elif length == 5:
        return FiveWord.query.filterBy(id = id).first()
    else:
        return []



