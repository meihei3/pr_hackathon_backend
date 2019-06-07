from flask import Flask
from controllers.comment_controller import CommentController
from db import init_db
from flask_cors import CORS


# init flask app
def create_app():
    _app = Flask(__name__)
    _app.config.from_object('config.Config')

    init_db(_app)
    CORS(_app)

    return _app


app = create_app()
app.add_url_rule('/comments/<string:company_id>/<string:release_id>',
                 view_func=CommentController.as_view('comment_controller'))


@app.route('/')
def index():
    return "hello"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=777, debug=True, threaded=True)
