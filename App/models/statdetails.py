from multiprocessing.connection import answer_challenge
from App.database import db

class StatDetails(db.Model):
    stat_id = db.Column(db.Integer, db.ForeignKey('stat.stat_id'), primary_key=True) #primary key and foreign key that links
    answer =  db.Column(db.String(4),nullable=False)
    user_response =  db.Column(db.String(4),nullable=False)                                                                                #StatDetails class to Stat class
    time_taken = db.Column(db.Integer, nullable=False)

    def toDict(self):
        return{
            'stat_id': self.stat_id,
            'answer':self.answer,
            'user_response':self.user_response,
            'time_taken': self.time_taken
        }
