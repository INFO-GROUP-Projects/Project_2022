#write code to create and actually manipulate word page here
from flask import Blueprint, redirect, render_template, jsonify, request, send_from_directory,flash, url_for
from flask_jwt import jwt_required
import random

from App.controllers import (
    createWords, 
    getWord,
    getWordRand,
)
from App.models.currentGame import currentGame

word_views = Blueprint('word_views', __name__, template_folder='../templates')

@word_views.route('/WordPage')
def returnWordPage(): 
  cGame = currentGame()
  spellWord = getWordRand()["word"]
  uPoints = 0
  return render_template('wordPage.html',cGame = cGame , spellWord = spellWord,uPoints =uPoints)  

@word_views.route('/api/getWord/', methods = {'GET'})
def getWordsId():
    return getWordRand()

@word_views.route('/api/validate/', methods = {'POST'})
def validate_word():
    data = request.form
    cGame = currentGame()
    if  data['spellingWord'] == data['userWord'] :
      flash('Correct')
      uPoints = int(data['points']) + 1
    else:
      flash('Incorrect')
    return redirect('http://127.0.0.1:8080/WordPage')