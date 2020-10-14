# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db




class Pinglun(db.Model):
    __tablename__ = 'pinglun'

    pinglunid = db.Column(db.Integer, primary_key=True)
    pinglun = db.Column(db.String(255))
    name = db.Column(db.String(255))
    data = db.Column(db.String(255))
    articleid = db.Column(db.Integer)
