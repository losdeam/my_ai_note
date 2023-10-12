from exts import db


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Inter)