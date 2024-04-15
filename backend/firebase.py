
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore


class FirebaseHandler:
    def __init__(self, serviceAccount):
        self.cred = credentials.Certificate(serviceAccount)
        self.app = firebase_admin.initialize_app(self.cred)

        self.db = firestore.client()
    
    
    def makeNewCollection(self, collectionName):
        if collectionName in self.db.collections():
            return False
        
        self.db.collection(collectionName)
        return True
    
    def addDocument(self, collectionName, documentName, data):
        doc_ref = self.db.collection(collectionName).document(documentName)

        doc_ref.set(data)
    def editDocument(self, collectionName, documentName, data):
        #check if the document exists
        if not self.db.collection(collectionName).document(documentName).get().exists:
            return False
        doc_ref = self.db.collection(collectionName).document(documentName)
        doc_ref.update(data)
        return True
    def getDoc(self, collectionName, documentName):
        if not self.db.collection(collectionName).document(documentName).get().exists:
            return {}
        else: return self.db.collection(collectionName).document(documentName).get()
    