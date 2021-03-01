from flask import render_template
from app import app


@app.route("/index")
@app.route("/")
def index():
    return render_template('base.html')

"""
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
    else:
        print(form.errors)
    return render_template('login.html', form=form)


@app.route("/test", defaults={'info': None})
@app.route("/test/<info>")
def teste(info):
    i = User("anaa", "1234", "Ana", "laala@gmail.com")
    db.session.add(i)
    db.session.commit()
    return "olá Teste!!"
"""

"""
#@app.route("/test", defaults={'name': None})
@app.route("/test/<int:id>")
def teste(id):
    if id:
        return "olá Teste!! %s" % id
    else:
        return "olá Teste!!"
"""
