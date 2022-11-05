from flask_restful import fields


FloorGetFields = {
    'id': fields.Integer,
    'name': fields.String,
    'slug': fields.String,
    'time': fields.DateTime,
    'price': fields.Float
}

NftGetFields = {
    'id': fields.Integer,
    'name': fields.String,
    'slug': fields.String,
    'time': fields.DateTime,
    'price': fields.Float
}

LoanGetFields = {
    'id': fields.Integer,
    'name': fields.String,
    'slug': fields.String,
    'time': fields.DateTime,
    'price': fields.Float
}
