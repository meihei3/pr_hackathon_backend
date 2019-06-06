from db import db


class NGs(db.Model):
    company_id = db.Column(db.String, unique=True)
    ng_words = db.Column(db.String)

    def to_dict(self):
        return {
            "company_id": self.company_id,
            "ng_words": self.ng_words
        }

    def __repr__(self):
        return '<NGs %r>' % self.company_id
