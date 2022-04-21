from App.models import StatDetails
from App.database import db

def create_statsDetails(stat_id, answer, user_response):
    newStatDetails = StatDetails(stat_id = stat_id,answer = answer,user_response = user_response)
    db.session.add(newStatDetails)
    db.session.commit()


def getAllUserStatsDetails(stat_id):
    query = StatDetails.query.filter_by(stat_id = stat_id)  
    if not query:
        return []
    returnStat = [q.to_dict() for q in query]
    return returnStat