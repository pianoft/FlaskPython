#flask_blog/views.py
from flask import request ,redirect ,url_for,render_template,flash,session
from flask_blog import app
from functools import wraps
def login_required(view):
    @wraps(view)
    def inner(*args,**kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args,**kwargs)
    return inner

@app.route('/login',methods=['GET','POST'])
def login():
    error=None
    if request.method=='POST':
        if request.form['username']!=app.config['USERNAME']:
            flash("Wrong username")
        elif request.form['password']!=app.config['PASSWORD']:
            flash("Wrond password")
        else:
            session['logged_in']=True
            flash("Logged in")
            return redirect(url_for('show_entries'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    flash("Logged out")
    return redirect(url_for('show_entries'))