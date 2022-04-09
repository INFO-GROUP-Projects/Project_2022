#word model stores information about the model nothing else
class FiveWords(object):
        def __init__(self,id, word,points):
            self.id = id
            self.word = word
            self.points =points

        def to_dict(self):
            return {
                'id':self.id,
                'word':self.word
                'points':self.points
            }
#class currentGame(FlaskForm):
   # user_answer = StringField('Answer')
   # points = HiddenField('Stats')
    #submit = SubmitField('Enter', render_kw ={'onclick ="wordToSpeech()"'})
   # speakFaster = SubmitField('Speak Faster', render_kw ={'onclick ="wordToSpeech()"'})
    #speakSlower = SubmitField('SpeakSlower', render_kw ={'onclick ="wordToSpeech()"'})


