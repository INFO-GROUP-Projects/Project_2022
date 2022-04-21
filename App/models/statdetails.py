from App.database import db

class StatDetails(db.Model):
    statDetailsId = db.Column(db.Integer, primary_key=True)
    stat_id = db.Column(db.Integer, db.ForeignKey('stat.stat_id'), nullable = False) #primary key and foreign key that links
    answer =  db.Column(db.String(4),nullable=False)
    user_response =  db.Column(db.String(4),nullable=False)                                                                                #StatDetails class to Stat class

    def to_dict(self):
        return{
            'stat_id': self.stat_id,
            'answer':self.answer,
            'answer':self.answer,
            'user_response':self.user_response,
        }
