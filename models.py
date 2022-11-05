from config import db
from sqlalchemy import event
from slugify import slugify


class UsersInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return self.name


class UsersImpInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    is_logedin = db.Column(db.Boolean, unique=False, default=False)
    token = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return self.username


class FloorInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255))
    time = db.Column(db.DateTime)
    price = db.Column(db.Float)

    def __repr__(self):
        return self.name

    @staticmethod
    def generate_slug(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)

db.event.listen(FloorInfo.name, 'set', FloorInfo.generate_slug, retval=False)


class NftInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255))
    time = db.Column(db.DateTime)
    price = db.Column(db.Float)

    def __repr__(self):
        return self.name

    @staticmethod
    def generate_slug(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)

db.event.listen(NftInfo.name, 'set', NftInfo.generate_slug, retval=False)


class LoanInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255))
    time = db.Column(db.DateTime)
    price = db.Column(db.Float)

    def __repr__(self):
        return self.name

    @staticmethod
    def generate_slug(target, value, oldvalue, initiator):
        if value and (not target.slug or value != oldvalue):
            target.slug = slugify(value)

db.event.listen(LoanInfo.name, 'set', LoanInfo.generate_slug, retval=False)
