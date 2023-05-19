# This code is for registering and logging in users

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import hashlib
import os
import dotenv

dotenv.load_dotenv()

certname = os.environ.get("AUTHENTICATIONKEYNAME")

cred = credentials.Certificate(f"src/auth/key/{certname}.json")
firebase_admin.initialize_app(cred)



class Authentication:
    def __init__(self):
        self.db = firebase_admin.firestore.client()
        
    
    
    def register(email, password, name):
        try:
            if self.db.collection("users").where("email", "==", email).get():
                return False
            else:
                password = hashlib.sha256(password.encode()).hexdigest()
                self.db.collection("users").add({
                    "email": email,
                    "name": name,
                    "password": password
                })
                return True
        except Exception as e:
            return False
    
    def login(self, email, password):
        try:
            if self.db.collection("users").where("email", "==", email).get():
                password = hashlib.sha256(password.encode()).hexdigest()
                if self.db.collection("users").where("password", "==", password).get():
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            return False
        
    def deleteUser(self, email):
        try:
            if self.db.collection("users").where("email", "==", email).get():
                self.db.collection("users").where("email", "==", email).delete()
                return True
            else:
                return False
        except Exception as e:
            return False