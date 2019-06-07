from db import db


class NGs(db.Model):
    __tablename__ = 'ng_words'
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.String, unique=True, nullable=False)
    ng_words = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            "company_id": self.company_id,
            "ng_words": self.ng_words
        }

    def __repr__(self):
        return '<NGs %r>' % self.company_id
