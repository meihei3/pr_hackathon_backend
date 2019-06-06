from flask import Flask
from controllers.CommentsController import CommentController
from db import init_db


# init flask app
def create_app():
    _app = Flask(__name__)
    _app.config.from_object('config.Config')

    init_db(_app)

    return _app


app = create_app()
app.add_url_rule('/comments/<string:company_id>/<string:post_id>',
                 view_func=CommentController.as_view('comment_controller'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=777, debug=True, threaded=True)
