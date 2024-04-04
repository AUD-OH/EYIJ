from flask import Flask, redirect, render_template, url_for
from flask import request
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'ey_db.db')
db = SQLAlchemy(app)


class Eydb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(80), unique=True, nullable=False)
    upw = db.Column(db.String(100), unique=True, nullable=False)
    nn = db.Column(db.String(80), unique=True, nullable=False)
    uimg = db.Column(db.String(500), unique=True, nullable=False)
    mt = db.Column(db.String(4), unique=True, nullable=False)
    ut = db.Column(db.String(300), unique=True, nullable=False)


# 글쓰기 db


class Podb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pt = db.Column(db.String(20), unique=False, nullable=False)
    ct = db.Column(db.String(500), unique=False, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/join')
def ey_join():
    uid_recive = request.args.get("u_id")
    upw_recive = request.args.get("u_pw")
    nn_recive = request.args.get("nn")
    mt_recive = request.args.get("mt")
    ut_recive = request.args.get("ut")
    uimg_recive = "asdf"

    eydb = Eydb(uid=uid_recive, upw=upw_recive, nn=nn_recive,
                mt=mt_recive, ut=ut_recive, uimg=uimg_recive)
    db.session.add(eydb)
    db.session.commit()
    return render_template('ey_in.html')
# 글쓰기 db 저장


@app.route('/cr_post', methods=['POST'])
def cr_post():
    u_pt = request.form.get('title')
    u_ct = request.form.get('content')
    podb = Podb(pt=u_pt, ct=u_ct)
    db.session.add(podb)
    db.session.commit()
    return redirect(url_for('popular_posts'))


@app.route('/')
def home():
    # print(request.args.get("u_id"))
    # print(request.args.get("u_pw"))
    # print(request.args.get("nn"))
    # print(request.args.get("mt"))
    # print(request.args.get("ut"))
    return render_template('eyij.html')


@app.route('/ey_post')
def ey_post():
    return render_template('ey_post.html')


@app.route('/ey_team')
def ey_team():
    return render_template('ey_team.html')


@app.route('/ey_login')
def ey_login():
    print(request.args.get("title"))
    return render_template('ey_login.html')


@app.route('/ey_in')
def ey_in():
    return render_template('ey_in.html')


@app.route('/ey_post_con')
def ey_post_con():
    return render_template('ey_post_con.html')


@app.route('/write-post')
def submit_post():
    pt = request.form.get('title')
    ct = request.form.get('content')
    return render_template('write-post.html')


@app.route('/popular_post_user')
def popular_posts():
    post_list = Podb.query.all()
    return render_template('popular_post_user.html', data=post_list)


if __name__ == '__main__':
    app.run(debug=True)
