# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db




class Denglu(db.Model):
    __tablename__ = 'denglu'

    denglulogid = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(255))
    mokuai = db.Column(db.String(50))
    adress = db.Column(db.String(255))
    cishu = db.Column(db.Integer)
    created_time = db.Column(db.DateTime)
    country = db.Column(db.String(50))
    regionName = db.Column(db.String(50))
    city = db.Column(db.String(50))
