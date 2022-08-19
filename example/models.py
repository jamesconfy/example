from sqlalchemy import Column, String, Integer
from example import db
from marshmallow import Schema, fields

class Users(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)

class UserSchema(Schema):
    id = fields.Integer(data_key="id")
    name = fields.Str(data_key="Name")