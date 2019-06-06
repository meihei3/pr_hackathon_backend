from flask import Flask, jsonify
# from controllers.CommentsController import CommentController
from db import init_db


dummy_data = {
    "comments": [
        {
            "id": 0,
            "name": "sample_name_0",
            "text": "sample_comment_text_0",
            "posted_at": "YYYY-MM-DD hh:mm"
        },
        {
            "id": 1,
            "name": "sample_name_1",
            "text": "sample_comment_text_1",
            "posted_at": "YYYY-MM-DD hh:mm"
        }
    ]
}


# init flask app
def create_app():
    _app = Flask(__name__)
    _app.config.from_object('config.Config')

    init_db(_app)

    return _app


app = create_app()
# app.add_url_rule('/comments/<string:company_id>/<string:post_id>',
#                  view_func=CommentController.as_view('comment_controller'))


@app.route('/comments/<company_id>/<post_id>')
def index(company_id, post_id):
    print(company_id, post_id)
    return jsonify(dummy_data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=85, debug=True, threaded=True)
