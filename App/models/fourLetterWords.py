#word model stores information about the model nothing else
from App.database import db
class FourWords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word =  db.Column(db.String(4), nullable=False)
    points = db.Column(db.Integer, nullable=False)

    def __init__(self,id, word,points):
            self.id = id
            self.word = word
            self.points =points

    def to_dict(self):
            return {
                'id':self.id,
                'word':self.word,
                'points':self.points
            }


