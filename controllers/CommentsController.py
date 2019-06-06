from flask import request
# from models.commnets import Comments
from flask.json import jsonify
from flask.views import MethodView
# from db import db


class CommentController(MethodView):
    def get(self, company_id, post_id):
        """
        :return: json
        """
        return jsonify({"comments": []})

    def post(self, company_id, post_id):
        """
        :return: json
        """
        text = request.form[""]
        return jsonify({'response': 'ok'})
