from flask import Flask, jsonify
# import models as db


# init flask app
def create_app():
    _app = Flask(__name__)
    _app.config.from_object('config.Config')

    # Todo: db
    # db.init_db(_app)

    return _app


app = create_app()


if __name__ == '__main__':
    app.run()
