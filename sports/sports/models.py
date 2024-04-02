from sports import db

class player(db.Model):
    name = db.Column(db.String(200), primary_key=True)
    kind = db.Column(db.String(200), nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime(), nullable=False)
    
class plan(db.Model):
    id = db.Column(db.Integer,primary_key=True, autoincrement=True )
    date2 = db.Column(db.DateTime())
    time = db.Column(db.String(200))
    kind = db.Column(db.String(200))
    name = db.Column(db.String(200))
    player = db.Column(db.String(200))
    
class Cheer(db.Model):
    cheer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime(), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    