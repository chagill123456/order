# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from application import db




class Wenzhang(db.Model):
    __tablename__ = 'wenzhang'

    articleid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    type = db.Column(db.String(255))
    jianji = db.Column(db.String(255), nullable=False)
    quanwen = db.Column(db.Text)
    redu = db.Column(db.Text)
    name = db.Column(db.String(255))
    biaoqian = db.Column(db.String(255))
    data = db.Column(db.String(255))
    heji = db.Column(db.String(255))
    hejiID = db.Column(db.Integer)
    hits = db.Column(db.String(255))
    blnIsNeedPw = db.Column(db.Integer)
    psw = db.Column(db.String(255))
    headportraitadress = db.Column(db.String(255))
