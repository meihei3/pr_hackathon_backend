# coding: utf-8
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# Model
class Model(db.Model):
    __tablename__ = 'models'
    comment_id = db.Column(db.Integer, primary_key=True)
    post_id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    text=db.Column(db.String(),unique=True)

    def get_comment(self):
        return dict(
            comment_id=self.comment_id ,post_id=self.post_id ,
             name=self.name ,text=self.text
        )

    def  post_comment(self,request):
        post=request.json['post_id']
        p=Model(post)
        db.session.add(d)
        db.session.commit()

        conpany=request.json['company_id']
        c=Model(company)
        db.session.add(c)
        db.session.commit()

        name=requests.jason['name']
        n=Model(name)
        db.session.add(n)
        db.session.commit()

        text=requests.jason['text']
        t=Model(text)
        db.session.add(t)
        db.session.commit()

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Model {}>'.format(self.name)


@app.route("/api/v1/model/<id>", methods=['DELETE'])
def api_v1_model_id(id):
    if request.method == 'DELETE':
        d = Model.query.get(id)
        db.session.delete(d)
        db.session.commit()
        return '', 204


@app.route("/api/v1/models", methods=['GET', 'POST'])
def api_v1_models():
    if request.method == 'POST':
        name = request.json['name']
        d = Model(name)
        db.session.add(d)
        db.session.commit()
        return jsonify(d.to_dict()), 201
    if request.method == 'GET':
        ls = Model.query.all()
        ls = [l.to_dict() for l in ls]
        return jsonify(ls), 200


if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    app.run(host='0.0.0.0', port=3001)
