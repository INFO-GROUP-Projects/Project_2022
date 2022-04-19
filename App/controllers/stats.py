
from App.models import Stats
from App.database import db

def create_stats(p_gain, c_words, i_words, u_id,time):
    newStat = Stats(points_gained = p_gain,correct_words = c_words,incorrect_words = i_words,id = u_id,timeStarted = time)
    db.session.add(newStat)
    db.session.commit()

def getStats_Id(u_id,time):
    returnStat = Stats.query.filter_by(id = u_id, timeStated = time).first()
    return returnStat.to_dict()

def getAllStats():
    query = Stats.query.all()  
    if not query:
        return []
    returnStat = [q.to_dict() for q in query]
    return returnStat

def getTopTenStats():
    query = Stats.query.order_by("points_gained desc").limit(10)  
    if not query:
        return []
    returnStat = [q.to_dict() for q in query]
    return returnStat