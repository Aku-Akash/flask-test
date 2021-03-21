from app import db

class Test(db.Model):
    __tablename__ = 'tests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    score = db.Column(db.Integer)

    def __init__(self,id ,name, score):
        self.id = id
        self.name = name
        self.score = score

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'score': self.score,
        }