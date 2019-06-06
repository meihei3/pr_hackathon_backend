from flask import Flask
from controllers.CommentsController import CommentController
# import models as db


# init flask app
def create_app():
    _app = Flask(__name__)
    _app.config.from_object('config.Config')

    # Todo: db
    # db.init_db(_app)

    return _app


app = create_app()
app.add_url_rule('/comments/<string:company_id>/<string:post_id>',
                 view_func=CommentController.as_view('comment_controller'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=777, debug=True, threaded=True)
