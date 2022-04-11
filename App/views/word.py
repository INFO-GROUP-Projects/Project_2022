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
def init_wordPage():
  userStats = currentGame()
  currentScore = 0
  correctWords = 0
  incorrectWords = 0 
  currentIndex = 1
  return render_template('wordPageBegin.html',currentIndex =currentIndex ,incorrectWords = incorrectWords,
  correctWords = correctWords, currentScore = currentScore,  userStats = userStats )

@word_views.route('/WordPage/<id>', methods={'POST'})
def returnWordPage(id): 
  data = request.form
  
  currentScore = data['currentScore']
  correctWords =  data['correctWords']
  incorrectWords =  data['incorrectWords']
  currentIndex =  data['index']

  print('Hello')

  if id > currentIndex:
    return "Error"
  
  cGame = currentGame()
  
  returnVar = getWordRand()
  spellWord = returnVar["word"]
  uPoints = returnVar["points"]
  
  return render_template('wordPage.html',cGame = cGame , spellWord = spellWord,uPoints =uPoints,
  currentIndex =currentIndex ,incorrectWords = incorrectWords,correctWords = correctWords, 
  currentScore = currentScore)  

@word_views.route('/api/getWord/', methods = {'GET'})
def getWordsId():
    return getWordRand()

@word_views.route('/api/validate/', methods = {'POST'})
def validate_word():
    data = request.form
    currentScore = data['currentScore']
    correctWords =  data['correctWords']
    incorrectWords =  data['incorrectWords']
    currentIndex =  data['index']
    points_gained = data['points']
    cGame = currentGame()

    if  data['spellingWord'] == data['userWord'] :
      flash('Correct')
      currentScore = currentScore + points
      correct_words = correct_words + 1
    else:
      flash('Incorrect')
    currentIndex =  currentIndex + 1
    return redirect('/WordPage/')