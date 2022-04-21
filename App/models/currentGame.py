from flask_wtf import FlaskForm
from wtforms import StringField,HiddenField,SubmitField

class currentGame(FlaskForm):
     userWord = StringField('passWord')
     spellingWord = HiddenField('Stats', id = 'spellingWord')
     points = HiddenField('Stats' , id='points',default= 0)
     submit = SubmitField('Enter')
     currentScore = HiddenField('cScore')
     correctWords = HiddenField('cWords')
     incorrectWords=HiddenField('iWords')
     index = HiddenField('cIndex')
     dateTime = HiddenField('cDate')
