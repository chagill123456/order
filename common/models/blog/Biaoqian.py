# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db




class Biaoqian(db.Model):
    __tablename__ = 'biaoqian'

    biaoqianID = db.Column(db.Integer, primary_key=True)
    biaoqian = db.Column(db.String(255))
