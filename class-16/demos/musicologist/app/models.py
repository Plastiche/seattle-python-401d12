from app import db


class Band(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    artists = db.relationship("Artist", backref="band", lazy=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name}


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    band_id = db.Column(db.Integer, db.ForeignKey("band.id"), nullable=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name}
