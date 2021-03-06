from App.database import db

class Stat(db.Model):
    stat_id = db.Column(db.Integer, primary_key=True) #primary key
    points_gained =  db.Column(db.Integer, nullable=False)
    correct_words = db.Column(db.Integer, nullable=False)
    incorrect_words = db.Column(db.Integer, nullable=False)
    timeStarted = db.Column(db.DateTime, nullable=False)
    id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # foreign key that links Stat to User Class
    user = db.relationship('User')

    def to_dict(self):
        return{
            'stat_id': self.stat_id,
            'points_gained': self.points_gained,
            'correct_words': self.correct_words,
            'incorrect_words': self.incorrect_words,
            'timeStarted':self.timeStarted,
            'user': self.user.toDict(),
        }
   
    
