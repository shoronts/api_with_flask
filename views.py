from flask import request, jsonify
from flask_restful import Resource, marshal_with
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from werkzeug.security import check_password_hash, generate_password_hash

from config import db
from models import UsersImpInfo, UsersInfo, FloorInfo, NftInfo, LoanInfo
from serializers import FloorGetFields, NftGetFields, LoanGetFields

from datetime import datetime


def is_user(username):
    user = UsersInfo.query.filter_by(username=username).first()
    loged_user = UsersImpInfo.query.filter_by(username=username).first()
    context = {
        'user': user,
        'loged_user': loged_user
    }
    return context


class Register(Resource):
    def post(self):
        name = request.json.get("name", None)
        email = request.json.get("email", None)
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        hashPassword = generate_password_hash(password, method='sha256')
        if UsersInfo.query.filter_by(username=username).first():
            return jsonify(message='Username exists.')
        elif UsersInfo.query.filter_by(email=email).first():
            return jsonify(message='Email exists.')
        else:
            NewRegister = UsersInfo(
                name=name,
                username=username,
                password=hashPassword,
                email=email
            )
            db.session.add(NewRegister)
            db.session.commit()
            return jsonify(message='You are successfully registered.')


class Login(Resource):
    def post(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        user = is_user(username)
        if user['loged_user']:
            return jsonify(access_token=user['loged_user'].token)
        elif user['user'] and not user['loged_user']:
            if check_password_hash(user['user'].password, password):
                access_token = create_access_token(identity=username)
                loged_in_user = UsersImpInfo(
                    username=username,
                    is_logedin=True,
                    token=access_token
                )
                db.session.add(loged_in_user)
                db.session.commit()
                return jsonify(access_token=access_token)
            else:
                return jsonify(message="Wrong Password")
        else:
            return jsonify(message="Wrong Username")


class Logout(Resource):

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = is_user(current_user)
        if user['user']:
            db.session.delete(UsersImpInfo.query.get_or_404(user['loged_user'].id))
            db.session.commit()
            return jsonify(message="Successfully Logout")
        else:
            return jsonify(message="No user found")


class Floor(Resource):

    @jwt_required()
    @marshal_with(FloorGetFields)
    def get(self):
        current_user = get_jwt_identity()
        user = is_user(current_user)
        if user['loged_user']:
            data = FloorInfo.query.all()
            return data

    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        user = is_user(current_user)
        if user['loged_user']:
            name = request.json.get("name", None)
            price = request.json.get("price", None)
            new_floor = FloorInfo(
                name=name,
                time=datetime.now(),
                price=price
            )
            db.session.add(new_floor)
            db.session.commit()
            return jsonify(message=f"Floor saved")


class Nft(Resource):

    @jwt_required()
    @marshal_with(NftGetFields)
    def get(self):
        current_user = get_jwt_identity()
        user = is_user(current_user)
        if user['loged_user']:
            data = NftInfo.query.all()
            return data

    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        user = is_user(current_user)
        if user['loged_user']:
            name = request.json.get("name", None)
            price = request.json.get("price", None)
            new_nft = NftInfo(
                name=name,
                time=datetime.now(),
                price=price
            )
            db.session.add(new_nft)
            db.session.commit()
            return jsonify(message=f"NFT saved")


class Loan(Resource):
    
    @jwt_required()
    @marshal_with(LoanGetFields)
    def get(self):
        current_user = get_jwt_identity()
        user = is_user(current_user)
        if user['loged_user']:
            data = LoanInfo.query.all()
            return data

    @jwt_required()
    def post(self):
        current_user = get_jwt_identity()
        user = is_user(current_user)
        if user['loged_user']:
            name = request.json.get("name", None)
            price = request.json.get("price", None)
            new_nft = LoanInfo(
                name=name,
                time=datetime.now(),
                price=price
            )
            db.session.add(new_nft)
            db.session.commit()
            return jsonify(message=f"Loan saved")
