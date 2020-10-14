# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db




class Log(db.Model):
    __tablename__ = 'log'

    logid = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(50))

    updated_time = db.Column(db.DateTime)
    hits = db.Column(db.Integer)
