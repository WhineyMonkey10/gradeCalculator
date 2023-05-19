from flask import Flask, render_template, request, redirect, url_for, flash, session
import dotenv
import os
from src.auth.accounts import Authentication

app = Flask(__name__)
dotenv.load_dotenv()

app.secret_key = os.getenv('SECRETKEY')

Authentication = Authentication()

@app.route("/")
def index():
    if 'loggedin' in session:
        return redirect(url_for("dashboard"))
    else:
        return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    if 'loggedin' in session:
        return redirect(url_for("dashboard"))
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        loginResult = Authentication.login(email, password)
        if loginResult:
            session['loggedin'] = True
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials", "error")
            return redirect(url_for("index"))
        
@app.route("/logout")
def logout():
    if 'loggedin' not in session:
        return redirect(url_for("dashboard"))
    else:
        session.pop('loggedin', None)
        return redirect(url_for("index"))

@app.route("/dashboard")
def dashboard():
    if 'loggedin' in session:
        return render_template("dashboard.html")
    else:
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)


#ä Todo:

# Fix the dashboard page, css (obviously) and add the profile dropdown and make the toggle theme button work