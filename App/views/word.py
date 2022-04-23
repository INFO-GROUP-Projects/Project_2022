
from cmath import log
from datetime import datetime
from math import ceil
from time import strptime
from flask import Blueprint, redirect, render_template, jsonify, request, send_from_directory,flash, url_for
from flask_login import login_required,current_user

from App.controllers import (
    getWordRand
)
from App.controllers.stats import countUserStats, create_stats, getAllStats, getAllUserStat, getPostion, getStats_Id, getTopTenStats, updateCorrectWords,updateIncorrectWords
from App.controllers.statsDetails import create_statsDetails, getAllUserStatsDetails
from App.models.currentGame import currentGame

word_views = Blueprint('word_views', __name__, template_folder='../templates')

@word_views.route('/WordPage')
@login_required
def init_wordPage():
  userStats = currentGame()
  toStringDate = str(datetime.now())
  gameStr = 'gamemaster.PNG'
  userData = {
    "currentScore": 0,
    "correctWords": 0,
    "incorrectWords":0,
    "currentIndex": 3,
    "startTime": toStringDate
    "filename": gameStr
  }

  uStat = create_stats(userData['currentScore'],userData['correctWords'],userData['incorrectWords'],current_user.id ,userData['startTime'])
  return render_template('wordPageBegin.html',  userStats = userStats, userData = userData )

@word_views.route('/WordPage', methods={'POST'})
@login_required
def returnWordPage(): 
  data = request.form
  userData = {}
  userData['currentScore'] =  data['currentScore']
  userData['correctWords'] = data['correctWords'] 
  userData['incorrectWords'] = data['incorrectWords']
  userData ['currentIndex'] = data['index']
  userData["startTime"] = data['dateTime']
  returnVar = getWordRand()
  userData["word"] = returnVar["word"]
  userData["points"] = returnVar["points"]
  userData['gamemaster'] = 'gamemaster.PNG'
  
  cGame = currentGame()
  
  return render_template('wordPage.html',cGame = cGame , userData = userData)  

@word_views.route('/api/getWord/', methods = {'GET'})
@login_required
def getWordsId():
    return getWordRand()

@word_views.route('/api/validate/', methods = {'POST'})
@login_required
def validate_word():
    form = currentGame()
    if form.validate_on_submit: 
      data = request.form
      userData = {}
      userData['currentScore'] = int(data['currentScore'])
      userData['correctWords'] =  int(data['correctWords'])
      userData['incorrectWords'] =  int(data['incorrectWords'])
      userData['currentIndex'] =  int(data['index'])
      userData['points_gained'] = int(data['points'])
      userData["startTime"] = data['dateTime']
      userData['gamemaster'] = 'gamemaster.PNG'
      cGame = currentGame()
      s_id = getStats_Id(current_user.id,userData["startTime"])
      if  data['spellingWord'] == data['userWord'] :
        flash('Correct')
        userData['currentScore']= userData['currentScore'] + userData['points_gained']
        userData['correctWords'] = userData['correctWords'] + 1
        stat = updateCorrectWords(s_id,userData["startTime"],userData['points_gained'] )
        userData['gamemaster'] = 'correct.PNG'
      else:
        flash('Incorrect')
        userData['incorrectWords'] = userData['incorrectWords'] + 1
        userData['currentIndex'] = userData['currentIndex'] - 1 
        stat = updateIncorrectWords(s_id,userData["startTime"])
        userData['gamemaster'] = 'gamemaster.PNG'

      create_statsDetails(s_id,data['spellingWord'],data['userWord'])

      if userData['currentIndex'] == 0:
        leaderboard = getTopTenStats()
        position = getPostion(userData['currentScore'])
        return render_template('endPage.html', userData = userData, leaderboard = leaderboard, position = position)

      returnVar = getWordRand()
      userData["word"] = returnVar["word"]
      userData["points"] = returnVar["points"]
      history = getAllUserStatsDetails(s_id)

      return render_template('wordPage.html',cGame = cGame , userData = userData,history = history) 

@word_views.route('/history/<page>/')
@login_required
def returnHistoryPage(page):
  query = getAllUserStat(current_user.id,page)
  count = countUserStats(current_user.id)
  if(int(page) == 1):
    prev = 1
  else:
    prev = int(page) - 1
  if(int(page) >= ceil(count/10)):
    next = int(page) 
    flash("No more records")
  else:
    next = int(page) + 1
   
  return render_template('history.html', history = query, next = next, prev = prev)

@word_views.route('/history/<page>/<id>')
@login_required
def returnHistoryDetails(id):
  query = getAllUserStatsDetails(id)
  return render_template('historydetails.html', history = query)
