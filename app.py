from flask import Flask, render_template, request, session, redirect, url_for
import os   
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY','1234')
UTILISATEUR = { 'username': 'etudiant', 'password': 'edit2026'}

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('login'))
    return redirect(url_for('home'))

@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        if request.form['username'] == UTILISATEUR['username'] and request.form['password'] == UTILISATEUR['password']:
            session['username'] = request.form['username']
            return redirect(url_for('home',username=session['username']))
        else:
            message = 'Identifiant incorrect'
    return render_template('index.html', message=message)

@app.route('/logout')
def logout():
    session.pop('username', None)  
    return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True,host='0.0.0.0',port=5000)
