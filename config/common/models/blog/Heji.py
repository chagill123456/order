from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db




class Heji(db.Model):
    __tablename__ = 'heji'

    hejiID = db.Column(db.Integer, primary_key=True)
    heji = db.Column(db.String(255))
    name = db.Column(db.String(255))
    data = db.Column(db.String(255))

