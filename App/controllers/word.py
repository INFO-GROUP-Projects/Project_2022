#write code to intalize the words class and retrieve words and points 

import random
from flask import jsonify
from flask_wtf import FlaskForm
from wtforms import StringField,HiddenField,SubmitField

from App.database import db
from App.models import threeLetterWords,fourLetterWords,fiveLetterWords

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



