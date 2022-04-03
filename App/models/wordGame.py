import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import random
from flask import jsonify

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
def getWordsSingular(id):
    jsonList = {}
    if int(id) < 3 or int(id) > 5:
        return "Invalid"
    
    word_length = 0
    if int(id) == 3:
        collectionName = 'ThreeLetterWords'
        word_length = 1065
    elif int(id) == 4:
        collectionName = 'FourLetterWords'
        word_length = 4176
    elif int(id) == 5:
        collectionName = 'FiveLetterWords'
        word_length = 9330
    for x in range(0,10):
        index = random.randrange(0, word_length)
        doc_ref = wordDB.collection(collectionName).document(str(index))
        doc = doc_ref.get()
        if doc.exists:
            jsonList[x] = doc.to_dict()["word"]
        else:
            print(u'No such document!')
    return jsonify(jsonList)

def getWordsMultiple():
    jsonList = {}
    collectionName1 = 'ThreeLetterWords'
    word_length1 = 1065

    collectionName2 = 'FourLetterWords'
    word_length2 = 4176

    collectionName3 = 'FiveLetterWords'
    word_length3 = 9330

    for x in range(0,3):
        index = random.randrange(0, word_length1)
        doc_ref = wordDB.collection(collectionName1).document(str(index))
        doc = doc_ref.get()
        if doc.exists:
            jsonList[x] = doc.to_dict()["word"]
        else:
            print(u'No such document!')
    for x in range(3,6):
        index = random.randrange(0, word_length2)
        doc_ref = wordDB.collection(collectionName2).document(str(index))
        doc = doc_ref.get()
        if doc.exists:
            jsonList[x] = doc.to_dict()["word"]
        else:
            print(u'No such document!')
    for x in range(6,10):
        index = random.randrange(0, word_length3)
        doc_ref = wordDB.collection(collectionName3).document(str(index))
        doc = doc_ref.get()
        if doc.exists:
            jsonList[x] = doc.to_dict()["word"]
        else:
            print(u'No such document!')
    return jsonify(jsonList)
