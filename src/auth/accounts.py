# This code is for registering and logging in users

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("src/auth/key/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

class Authentication:
    def __init__(self, app):
        self.app = app
        self.db = firebase_admin.firestore.client()
    
    def register(self, email, password):
        
    
    def login(self, email, password):
        pass