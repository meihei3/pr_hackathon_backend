# coding: utf-8
from db import db


# Model
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.String())
    post_id = db.Column(db.String())
    name = db.Column(db.String(80))
    text = db.Column(db.String())
    posted_at = db.Column(db.String())

    def to_dict(self):
        return dict(
            company_id=self.company_id,
            post_id=self.post_id,
            name=self.name,
            text=self.text,
            poted_at=self.posted_at,
        )

    def __init__(self, company_id, post_id, name, text, posted_at):
        self.company_id = company_id
        self.post_id = post_id
        self.name = name
        self.text = text
        self.posted_at = posted_at

    def __repr__(self):
        return '<Model {}>'.format(self.name)
