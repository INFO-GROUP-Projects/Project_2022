from App.database import db

class StatDetails(db.Model):
    stat_id = db.Column(db.Integer, db.ForeignKey('stat.stat_id'), primary_key=True) #primary key and foreign key that links
                                                                                     #StatDetails class to Stat class
    time_taken = db.Column(db.Integer, nullable=False)
    


    def toDict(self):
        return{
            'stat_id': self.stat_id,
            'time_taken': self.time_taken
        }
