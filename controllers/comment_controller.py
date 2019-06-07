from flask import request
from models.comments import Comments
from flask.json import jsonify
from flask.views import MethodView
from db import db
from datetime import datetime
import pytz


class CommentController(MethodView):

    def get(self, company_id, release_id):
        comments = db.session.query(Comments).filter_by(release_id=release_id).filter_by(company_id=company_id)
        comments = [Comments.to_dict(c) for c in comments]
        return jsonify({"comments": comments})

    def post(self, company_id, release_id):
        """
        :return: json
        """
        text = request.form["text"]
        name = request.form["name"]
        dt = datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y-%m-%d %H:%M')
        c = Comments(company_id=company_id, release_id=release_id, name=name, text=text, posted_at=dt)
        db.session.add(c)
        db.session.commit()
        return jsonify({'response': 'ok'})
