# This code is for users to add grades to their account

import firebase_admin
from firebase_admin import credentials
import os
import dotenv

dotenv.load_dotenv()

certname = os.environ.get("AUTHENTICATIONKEYNAME")

cred = credentials.Certificate(f"src/auth/key/{certname}.json")
firebase_admin.initialize_app(cred)

class Grades:
    def __init__(self) -> None:
        self.db = firebase_admin.firestore.client()
        
    def addGrade(self, email, grade, class_name):
        try:
            grade = int(grade)
            if grade < 0 or grade > 100:
                return False
            self.db.collection("grades").add({
                "email": email,
                "grade": grade,
                "class": class_name
            })
            return True
        except Exception as e:
            return False
        
    def getGrades(self, email):
        try:
            grades = self.db.collection("grades").where("email", "==", email).get()
            return grades
        except Exception as e:
            return False
        
    def deleteGrade(self, email, gradeID):
        try:
            if self.db.collection("grades").document(gradeID).where("email", "==", email).get():
                self.db.collection("grades").document(gradeID).delete()
                return True
            else:
                return False
        except Exception as e:
            return False
        
    def deleteAllGrades(self, email):
        try:
            if self.db.collection("grades").where("email", "==", email).get():
                self.db.collection("grades").where("email", "==", email).delete()
                return True
            else:
                return False
        except Exception as e:
            return False
        
    def getUserClasses(self, email):
        try:
            classes = self.db.collection("grades").where("email", "==", email).get()
            return classes.distinct("class")
        except Exception as e:
            return False
        