from flask import Flask, render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
#basedir -> db 파일 기본 경로 import os 씀
basedir = os.path.abspath(os.path.dirname(__file__))
# db 경로
app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'ey_db.db')
db = SQLAlchemy(app)

# 댓글 db 테이블
class com_t(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    u_coment = db.Column(db.String(200), unique=True, nullable=False)

with app.app_context():
     db.create_all()
@app.route('/')
def home():
    print(request.args.get("comment"))
    return render_template('eyij.html')


@app.route('/ey_post')
def ey_post():
    return render_template('ey_post.html')


@app.route('/ey_team')
def ey_team():
    return render_template('ey_team.html')


@app.route('/ey_post_con')
def ey_post_con():
    return render_template('ey_post_con.html')


if __name__ == '__main__':
    app.run(debug=True)

