from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to a postgres database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db is an instance of our database
db = SQLAlchemy(app)

# create a class that map a table
class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    
    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'

# create tables from defined class models
db.create_all()

@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello ' + person.name


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=3000)