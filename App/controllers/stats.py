
from App.models.stat import Stat
from App.database import db

def create_stats(p_gain, c_words, i_words, u_id,time):
    newStat = Stat(points_gained = p_gain,correct_words = c_words,incorrect_words = i_words,id = u_id,timeStarted = time)
    db.session.add(newStat)
    db.session.commit()

def getStats_Id(u_id,time):
    returnStat = Stat.query.filter_by(id = u_id, timeStarted = time).first()
    return returnStat.to_dict()['stat_id']

def updateCorrectWords(stat_id,timeStarted, points):
    stat = Stat.query.filter_by(stat_id = stat_id,timeStarted =timeStarted).first()
    stat.points_gained = stat.points_gained + points
    stat.correct_words = stat.correct_words + 1
    db.session.add(stat)
    db.session.commit()
    
def updateIncorrectWords(stat_id,timeStarted):
    stat = Stat.query.filter_by(stat_id = stat_id,timeStarted =timeStarted).first()
    stat.incorrect_words = stat.incorrect_words + 1
    db.session.add(stat)
    db.session.commit()

def getAllStats():
    query = Stat.query.all()  
    if not query:
        return []
    returnStat = [q.to_dict() for q in query]
    return returnStat

def getTopTenStats():
    query = Stat.query.order_by("points_gained desc").limit(10)  
    if not query:
        return []
    returnStat = [q.to_dict() for q in query]
    return returnStat