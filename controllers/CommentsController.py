from flask import request
from models.commnets import Comments
from flask.json import jsonify
from flask.views import MethodView
from db import db
import datetime
import pytz



class CommentController(MethodView):
    def get(self, company_id, post_id):
        comments=Comment.query.all().filter(post_id=post_id,company_id=company_id)
        comments=[c.to_dict() for c in comments]
        return jsonify({"comments": comments})

    def post(self, company_id, post_id):
        """
        :return: json
        """
        text = request.form["text"]
        name=request.form["name"]
        datetime=datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        c=Comment(company_id,post_id,name,text,datetime)
        db.session.add(c)
        db.session.commit()
        return jsonify({'response': 'ok'})
