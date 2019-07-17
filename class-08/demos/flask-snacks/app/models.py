from app import db
class Snack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    rank = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id' : self.id,
            'name' : self.name
        }
