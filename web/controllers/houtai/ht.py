from flask import Blueprint,request,jsonify,g,redirect,json
from sqlalchemy import func

from common.libs.Helper import ops_render,getCurrentDate,iPagination,getDictFilterField,getFormatDate
from common.models.blog.Wenzhang import Wenzhang

from common.models.blog.Denglu import Denglu
import time
import datetime
import random



from application import  db

from sqlalchemy import extract,and_


blog_ht = Blueprint( 'ht_page',__name__ )

@blog_ht.route("/")
def index():
    resp_data = {}
    #获取当前日期
    date=time.strftime("%Y-%m-%d")
    cishu = 0
    denglu_info=db.session.query(func.sum(Denglu.cishu),func.date_format(Denglu.created_time, "%Y-%m-%d")).group_by(func.date_format(Denglu.created_time, "%Y-%m-%d"))
    for denglu in denglu_info:
        if date==denglu[1]:
            cishu = denglu[0]



    resp_data["cishu"]=cishu

    #获取当前yue
    year = datetime.date.today().year
    month = datetime.date.today().month

    denglu = db.session.query(and_(
    extract('year', Denglu.created_time) == year,
    extract('month', Denglu.created_time) == month
))

    yuecishu = 0
    yuecishu = denglu.count()
    resp_data["yuecishu"] = yuecishu
    #根据点击率顺序取出文章
    wenzhang_info = db.session.query(Wenzhang.articleid,Wenzhang.title,Wenzhang.hits).order_by(Wenzhang.hits.desc())

    wenzhang=[]
    wenzhangdetail={}
    count=0
    if wenzhang_info:
        count = int(wenzhang_info.count())

    i=0
    if count>0:
        for i in range (0,count-1):
            wenzhangdetail = {}
            wenzhangdetail["articleid"] = i+1
            wenzhangdetail["title"]=wenzhang_info[i][1]
            wenzhangdetail["hits"] = wenzhang_info[i][2]
            wenzhang.append(wenzhangdetail)
            i=i+1

    resp_data["wenzhanginfo"] = wenzhang













    return ops_render( "houtai/index.html",resp_data)


@blog_ht.route("/getdata",methods = [ 'GET','POST'])
def getdata():
    resp_data = {}

    denglu_info = Wenzhang.query.order_by( Wenzhang.hits.desc() ).all()


    xList = []
    yList = []
    yListinfo={}
    for denglu in denglu_info:
        xList.append(str(denglu.title))

        yList.append(int(denglu.hits))


    resp = {'xList': xList, 'yList': yList}
    resp_data['xList'] = xList
    resp_data['yList'] = yList
    return jsonify(resp_data)


@blog_ht.route("/getareadata",methods = [ 'GET','POST'])
def getareadata():
    resp_data = {}
    date = time.strftime("%Y-%m-%d")


    denglu_info = db.session.query(func.sum(Denglu.cishu),Denglu.country)\
        .group_by(Denglu.country).all()
    i=0
    xList = []
    yList = []

    cList = []
    for denglu in denglu_info:
        if denglu[1]:
            yListinfo = {}
            yListinfo["name"] = str(denglu[1])
            yListinfo["value"] = int(denglu[0])
            yList.append(yListinfo)
            xList.append(str(denglu[1]))
            cList.append(str(random_color()))


    resp_data['xList'] = xList
    resp_data['yList'] = yList
    resp_data['cList'] = cList
    print(resp_data)
    return jsonify(resp_data)

@blog_ht.route("/getssdjvdata",methods = [ 'GET','POST'])
def getssdjvdata():
    resp_data = {}
    date = time.strftime("%Y-%m-%d")

    denglu_info = db.session.query(func.sum(Denglu.cishu), Denglu.regionName).filter_by(country="中国")\
        .group_by(Denglu.regionName).all()
    i = 0
    xList = []
    yList = []

    cList = []
    for denglu in denglu_info:
        if denglu[1]:
            yListinfo = {}
            yListinfo["name"] = str(denglu[1])
            yListinfo["value"] = int(denglu[0])
            yList.append(yListinfo)
            xList.append(str(denglu[1]))


    resp_data['xList'] = xList
    resp_data['yList'] = yList

    print(resp_data)
    return jsonify(resp_data)


def random_color():
    color = ["#8d7fec", "#5085f2", "#e75fc3", "#f87be2", "#f2719a", "#fca4bb", "#f59a8f", "#fdb301", "#57e7ec", "#cf9ef1"]
    return random.choice(color)


