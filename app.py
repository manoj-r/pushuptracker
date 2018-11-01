import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "pushUpDatabase.db"))
print(database_file)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Pushups(db.Model):
    count = db.Column(db.Integer, unique=False)
    date = db.Column(db.DATETIME, primary_key=True)

    def __repr__(self):
        return "<Count: {}>".format(self.count)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.form:
        pushUps = Pushups(count = request.form.get("count"), date=datetime.utcnow())
        db.session.add(pushUps)
        db.session.commit()
    pushs = Pushups.query.all()
    return render_template('home.html', pushUps=pushs)

if __name__ == '__main__':
    app.run()
