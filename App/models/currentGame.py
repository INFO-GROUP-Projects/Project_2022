from flask_wtf import FlaskForm
from wtforms import StringField,HiddenField,SubmitField
from wtforms.validators import InputRequired,Length

class currentGame(FlaskForm):
     userWord = StringField('passWord', validators=[ InputRequired(), Length(min =4, max = 4,message="Word must be 4 letters! ") ])
     spellingWord = HiddenField('Stats', id = 'spellingWord')
     points = HiddenField('Stats' , id='points',default= 0)
     submit = SubmitField('Enter')
     currentScore = HiddenField('cScore')
     correctWords = HiddenField('cWords')
     incorrectWords=HiddenField('iWords')
     index = HiddenField('cIndex')
     dateTime = HiddenField('cDate')
