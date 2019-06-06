# coding: utf-8
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# Model
class Comment(db.Model):
    __tablename__ = 'comments'
    id=db.Column(db.Integer,primary_key=True)
    company_id = db.Column(db.Integer)
    post_id= db.Column(db.Integer)
    name = db.Column(db.String(80))
    text=db.Column(db.String())
    posted_at=db.Column(db.Datetime, default=datetime.datetime.now(pytz.timezone('Asia/Tokyo')))

    def to_dict(self):
        return dict(
            company_id=self.company_id ,
            post_id=self.post_id ,
            name=self.name ,
            text=self.text
        )

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<Model {}>'.format(self.name)
