#word model stores information about the model nothing else
class Words(object):
        def __init__(self,id, word,points,length):
            self.id = id
            self.word = word
            self.points =points
            self.length = length

        def to_dict(self):
            return {
                'id':self.id,
                'word':self.word
                'points':self.points
                'word length':self.word_length
            }
#class currentGame(FlaskForm):
   # user_answer = StringField('Answer')
   # points = HiddenField('Stats')
    #submit = SubmitField('Enter', render_kw ={'onclick ="wordToSpeech()"'})
   # speakFaster = SubmitField('Speak Faster', render_kw ={'onclick ="wordToSpeech()"'})
    #speakSlower = SubmitField('SpeakSlower', render_kw ={'onclick ="wordToSpeech()"'})


