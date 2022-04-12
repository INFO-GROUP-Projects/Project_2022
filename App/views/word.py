#write code to create and actually manipulate word page here
from flask import Blueprint, redirect, render_template, jsonify, request, send_from_directory,flash, url_for
from flask_jwt import jwt_required
import random

from App.controllers import (
    createWords, 
    getWord,
    getWordRand,
    user,
)
from App.models.currentGame import currentGame

word_views = Blueprint('word_views', __name__, template_folder='../templates')

@word_views.route('/WordPage')
def init_wordPage():
  userStats = currentGame()
  userData = {
    "currentScore": 0,
    "correctWords": 0,
    "incorrectWords":0,
    "currentIndex": 3
  }
  return render_template('wordPageBegin.html',  userStats = userStats, userData = userData )

@word_views.route('/WordPage', methods={'POST'})
def returnWordPage(): 
  data = request.form
  userData = {}
  userData['currentScore'] =  data['currentScore']
  userData['correctWords'] = data['correctWords'] 
  userData['incorrectWords'] = data['incorrectWords']
  userData ['currentIndex'] = data['index']
  returnVar = getWordRand()
  userData["word"] = returnVar["word"]
  userData["points"] = returnVar["points"]
  cGame = currentGame()
  
  return render_template('wordPage.html',cGame = cGame , userData = userData)  

@word_views.route('/api/getWord/', methods = {'GET'})
def getWordsId():
    return getWordRand()

@word_views.route('/api/validate/', methods = {'POST'})
def validate_word():
    data = request.form
    userData = {}
    userData['currentScore'] = int(data['currentScore'])
    userData['correctWords'] =  int(data['correctWords'])
    userData['incorrectWords'] =  int(data['incorrectWords'])
    userData['currentIndex'] =  int(data['index'])
    userData['points_gained'] = int(data['points'])
    cGame = currentGame()

    if  data['spellingWord'] == data['userWord'] :
      flash('Correct')
      userData['currentScore']= userData['currentScore'] + userData['points_gained']
      userData['correctWords'] = userData['correctWords'] + 1
    else:
      flash('Incorrect')
      userData['incorrectWords'] = userData['incorrectWords'] + 1
      userData['currentIndex'] = userData['currentIndex'] - 1 

    if userData['currentIndex'] == 0:
      render_template('endGame.html', userData = userData)

    returnVar = getWordRand()
    userData["word"] = returnVar["word"]
    userData["points"] = returnVar["points"]

    return render_template('wordPage.html',cGame = cGame , userData = userData) 