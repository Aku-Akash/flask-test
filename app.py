import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Test

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/add")
def add_test():
    id = request.args.get('id')
    name=request.args.get('name')
    score=request.args.get('score')
    try:
        test=Test(
            id = id,
            name=name,
            score=score,
        )
        db.session.add(test)
        db.session.commit()
        return "score added. score id={}".format(test.id)
    except Exception as e:
	    return(str(e))

@app.route("/getall")
def get_all():
    try:
        tests=Test.query.all()
        return  jsonify([e.serialize() for e in tests])
    except Exception as e:
	    return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        test=Test.query.filter_by(id=id_).first()
        return jsonify(test.serialize())
    except Exception as e:
	    return(str(e))

if __name__ == '__main__':
    app.run()