import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import os

this_folder = os.path.dirname(os.path.abspath(__file__))
myfile = os.path.join(this_folder,'AuthDB.json')


cred = credentials.Certificate(myfile)
firebase_admin.initialize_app(cred)

wordDB = firestore.client()

class Words(object):
        def __init__(self, word,id):
            self.id = id
            self.word = word

        def to_dict(self):
            return {
                'id':self.id,
                'word':self.word
            }

ref = wordDB.collections(u'ThreeLetterWords')
def initThreeLetterWords():
    with open("3-letter-words.json", "r") as File: 
        jsonData = json.load(File)

        for x in range(len(jsonData)):
            three = Words (jsonData[x]["word"],x)
            s = "%s" %three.id
            wordDB.collection(u'ThreeLetterWords').document(s).set(three.to_dict())

ref = wordDB.collections(u'FourLetterWords')
def initFourLetterWords():
    with open("4-letter-words.json", "r") as File: 
        jsonData = json.load(File)

        for x in range(len(jsonData)):
            three = Words (jsonData[x]["word"],x)
            s = "%s" %three.id
            wordDB.collection(u'FourLetterWords').document(s).set(three.to_dict())

ref = wordDB.collections(u'FiveLetterWords')
def initFiveLetterWords():
    with open("5-letter-words.json", "r") as File: 
        jsonData = json.load(File)

        for x in range(len(jsonData)):
            three = Words (jsonData[x]["word"],x)
            s = "%s" %three.id
            wordDB.collection(u'FiveLetterWords').document(s).set(three.to_dict())


#initThreeLetterWords()
#initFourLetterWords()
# #initFiveLetterWords()
