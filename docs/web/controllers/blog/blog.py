# -*- coding: utf-8 -*-
from flask import Blueprint,request,jsonify,g,redirect
from common.libs.Helper import ops_render,getCurrentDate,iPagination,getDictFilterField,getFormatDate
from common.models.blog.Wenzhang import Wenzhang
from common.models.blog.Biaoqian import Biaoqian
from common.models.blog.Heji import Heji
from common.models.blog.Log import Log
from common.models.blog.Pinglun import Pinglun


from application import  db

from application import app


from common.models.User import ( User )
from common.libs.user.UserService import ( UserService )





blog_bp = Blueprint( 'blog_page',__name__ )

@blog_bp.route("/")
def index():
    resp_data = {}
    req = request.values
    ip = request.remote_addr
    print(request.remote_addr)
    page = int(req['p']) if ('p' in req and req['p']) else 1
    offset = (page - 1) * 20

    query = Wenzhang.query
    list = query.order_by( Wenzhang.articleid.desc() ).offset( offset ).limit(20).all()
    query = Biaoqian.query
    biaoqianlist=query.order_by( Biaoqian.biaoqianID.desc() )
    query = Heji.query
    hejilist = query.order_by(Heji.hejiID.desc())

    #按热度顺序推最高的五个
    tuijianlist=Wenzhang.query.order_by( Wenzhang.hits.desc() ).limit(5).all()
    resp_data['page'] = page
    resp_data['list'] = list
    resp_data['hejilist'] = hejilist
    resp_data['biaoqianlist'] = biaoqianlist
    resp_data['tuijianlist'] = tuijianlist
    resp_data['current'] = 'index'

    # 修改浏览数
    blog_log_info = Log.query.first()
    if blog_log_info:
        model_log_info = blog_log_info
        model_log_info.ip = ip
        model_log_info.updated_time=getFormatDate()
        model_log_info.hits = int(blog_log_info.hits) + 1

    else:
        model_log_info=Log()
        model_log_info.hits = 1
        model_log_info.ip = ip
        model_log_info.updated_time = getFormatDate()
    resp_data['model_log_info'] = model_log_info
    db.session.add(model_log_info)
    db.session.commit()

    g.current_user=check_login()

    return ops_render("blog/index.html", resp_data)

@blog_bp.route( "/details")
def detail():
    resp_data = {}
    req = request.values


    id = int(req.get('id', 0))

    info = Wenzhang.query.filter_by(articleid=id).first()
    pinglun = Pinglun.query.filter_by(articleid=id).order_by(Pinglun.pinglunid.desc()).all()





    result = info.quanwen.split('\n')
    resp_data['info'] = info
    resp_data['pinglun'] = pinglun
    resp_data['result'] = result
    resp_data['current'] = 'index'

    if info.blnIsNeedPw == 1:
        return ops_render("blog/decrypt.html", resp_data)


    # 修改浏览数
    blog_detail_info = Wenzhang.query.filter_by(articleid=id).first()
    if blog_detail_info:
        model_detail_cat = blog_detail_info

    model_detail_cat.hits = int(blog_detail_info.hits) if (blog_detail_info.hits is not None) else 0
    model_detail_cat.hits=model_detail_cat.hits+1




    db.session.add(model_detail_cat)
    db.session.commit()


    return ops_render("blog/blog.html", resp_data)


@blog_bp.route( "/classify")
def classify():
    resp_data = {}

    query = Heji.query
    hejilist = query.order_by(Heji.hejiID.desc())
    shuliang=hejilist.count()

    query = Biaoqian.query
    biaoqianlist = query.order_by(Biaoqian.biaoqianID.desc())

    resp_data['hejilist'] = hejilist
    resp_data['shuliang'] = shuliang
    resp_data['biaoqianlist'] = biaoqianlist
    resp_data['current'] = 'index'
    return ops_render("blog/classify.html",resp_data)

@blog_bp.route( "/info")
def info():
    resp_data = {}

    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    offset = (page - 1) * 20
    id = int(req.get('id', 0))

    list = Wenzhang.query.filter_by(hejiID=id).order_by(Wenzhang.articleid.desc()).offset(offset).limit(20).all()
    # 按热度顺序推最高的五个
    tuijianlist = Wenzhang.query.order_by(Wenzhang.redu.desc()).limit(5).all()
    resp_data['page'] = page
    resp_data['list'] = list
    resp_data['tuijianlist'] = tuijianlist
    resp_data['current'] = 'index'
    return ops_render("blog/info.html", resp_data)

@blog_bp.route( "/biaoqian")
def biaoqian():
    resp_data = {}

    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    offset = (page - 1) * 20
    bq = str(req.get('bq', ''))

    list = Wenzhang.query.filter_by(biaoqian=bq).order_by(Wenzhang.articleid.desc()).offset(offset).limit(20).all()
    # 按热度顺序推最高的五个
    tuijianlist = Wenzhang.query.order_by(Wenzhang.hits.desc()).limit(5).all()
    resp_data['page'] = page
    resp_data['list'] = list
    resp_data['tuijianlist'] = tuijianlist
    resp_data['current'] = 'index'

    g.current_user = check_login()
    return ops_render("blog/info.html", resp_data)





@blog_bp.route( "/search",methods = [ 'GET','POST'] )
def search():
    if request.method == "GET":
        resp_data = {}
        req = request.values
        print(req)

        title = str(req['search']) if ('search' in req and req['search']) else 'dao'
        print(title)


        list = Wenzhang.query.filter(Wenzhang.title.ilike("%{0}%".format(title))).order_by(
            Wenzhang.articleid.desc()).limit(20).all()
        # 按热度顺序推最高的五个
        tuijianlist = Wenzhang.query.order_by(Wenzhang.hits.desc()).limit(5).all()
        resp_data['page'] = 1
        resp_data['list'] = list
        resp_data['tuijianlist'] = tuijianlist
        resp_data['current'] = 'index'
        return ops_render("blog/info.html", resp_data)

    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    title = str(req['search']) if ('search' in req and req['search']) else ''
    if title=='':
        resp['code'] = '-1'
        return jsonify(resp)

    return jsonify(resp)

@blog_bp.route( "/pinglunset",methods = [ 'GET','POST'] )
def pinglunset():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values
    articleid = int(req['articleid']) if 'articleid' in req and req['articleid'] else 0
    name = req['name'] if 'name' in req else ''
    pinglun = req['pinglun'] if 'pinglun' in req else ''

    model_pinglun = Pinglun()

    model_pinglun.articleid = articleid
    model_pinglun.name = name
    model_pinglun.pinglun = pinglun
    model_pinglun.data = getCurrentDate()

    db.session.add(model_pinglun)
    ret = db.session.commit()

    return jsonify(resp)


@blog_bp.route( "/verify" )
def verify():
    resp_data = {}
    req = request.values

    print(req)
    id = int(req.get('id', 0))

    info = Wenzhang.query.filter_by(articleid=id).first()
    pinglun = Pinglun.query.filter_by(articleid=id).order_by(Pinglun.pinglunid.desc()).all()

    result = info.quanwen.split('\n')
    resp_data['info'] = info
    resp_data['pinglun'] = pinglun
    resp_data['result'] = result
    resp_data['current'] = 'index'


    # 修改浏览数
    blog_detail_info = Wenzhang.query.filter_by(articleid=id).first()
    if blog_detail_info:
        model_detail_cat = blog_detail_info
    model_detail_cat.hits = int(blog_detail_info.hits) if (blog_detail_info.hits is not None) else 0
    model_detail_cat.hits = model_detail_cat.hits + 1
    db.session.add(model_detail_cat)
    db.session.commit()

    return ops_render("blog/blog.html", resp_data)

@blog_bp.route( "/test",methods = [ 'GET','POST'] )
def test():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}


    return jsonify( resp )

@blog_bp.route( "/postblog" )
def postblog():
    resp_data = {}
    req = request.values
    print(req)
    id = int(req.get('id', 0))

    info = Wenzhang.query.filter_by(articleid=id).first()


    query = Biaoqian.query
    biaoqianlist = query.order_by(Biaoqian.biaoqianID.desc())
    query = Heji.query
    hejilist = query.order_by(Heji.hejiID.desc())

    resp_data['info'] = info
    resp_data['hejilist'] = hejilist
    resp_data['biaoqianlist'] = biaoqianlist

    resp_data['current'] = 'index'
    return ops_render("blog/postblog.html", resp_data)

@blog_bp.route( "/postdetail",methods = [ 'GET','POST'] )
def postdetail():
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    info=check_login()
    req = request.values
    hejiid = int(req['heji_id']) if 'heji_id' in req and req['heji_id'] else 0
    name = req['name'] if 'name' in req else ''
    articleid = int(req['articleid']) if 'articleid' in req and req['articleid'] else 0
    biaoqian_id = int(req['biaoqian_id']) if 'biaoqian_id' in req and req['biaoqian_id'] else 0
    summary = req['summary'] if 'summary' in req else ''
    jianjie = req['jianjie'] if 'jianjie' in req else ''
    heji = req['heji'] if 'heji' in req else ''
    psw = req['psw'] if 'psw' in req else ''
    biaoqian=""
    blnIsNeedPw=0
    type="同人"
    print(req)
    if hejiid>0:
        hejilist =  Heji.query.filter_by(hejiID=hejiid).first()
        if hejilist:
            heji = hejilist.heji
            print(hejilist.heji)


        print(hejilist)
    if biaoqian_id > 0:
        biaoqianlist = Biaoqian.query.filter_by(biaoqianID=biaoqian_id).first()
        if biaoqianlist:
            biaoqian = biaoqianlist.biaoqian
        print(biaoqianlist)
    if psw:
        blnIsNeedPw=1


    wenzhang_info=Wenzhang.query.filter_by(articleid=articleid).first()
    if wenzhang_info:
        model_wenzhang_info=wenzhang_info
    else:
        model_wenzhang_info = Wenzhang();
    model_wenzhang_info.title=name
    model_wenzhang_info.hejiID=hejiid
    model_wenzhang_info.quanwen=summary
    model_wenzhang_info.biaoqian=biaoqian
    model_wenzhang_info.heji=heji
    model_wenzhang_info.name=info.nickname
    model_wenzhang_info.type="同人"
    model_wenzhang_info.blnIsNeedPw=blnIsNeedPw
    model_wenzhang_info.psw=psw
    model_wenzhang_info.headportraitadress = info.headportraitadress
    model_wenzhang_info.jianji=jianjie
    model_wenzhang_info.data=getFormatDate()


    db.session.add(model_wenzhang_info)
    db.session.commit()

    return jsonify( resp )


@blog_bp.route( "/author",methods = [ 'GET','POST'])
def author():
    if request.method == "GET":
        resp_data = {}

        req = request.values
        page = int(req['p']) if ('p' in req and req['p']) else 1
        offset = (page - 1) * 20
        author = str(req.get('author', ''))

        list = Wenzhang.query.filter_by(name=author).order_by(Wenzhang.articleid.desc()).offset(offset).limit(20).all()
        # 按热度顺序推最高的五个
        tuijianlist = Wenzhang.query.order_by(Wenzhang.hits.desc()).limit(10).all()
        resp_data['page'] = page
        resp_data['list'] = list
        resp_data['tuijianlist'] = tuijianlist
        resp_data['current'] = 'index'

        g.current_user = check_login()
        return ops_render("blog/info.html", resp_data)
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    return jsonify(resp)

@blog_bp.route( "/personalinformation",methods = [ 'GET','POST'])
def personalinformation():
    if request.method == "GET":
        resp_data = {}

        req = request.values


        info = check_login()
        g.current_user = info
        resp_data['info'] = info
        return ops_render("blog/personalinfo.html", resp_data)
    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    return jsonify(resp)







'''
判断用户是否已经登录
'''
def check_login():
    cookies = request.cookies
    auth_cookie = cookies[app.config['AUTH_COOKIE_NAME']] if app.config['AUTH_COOKIE_NAME'] in cookies else None


    if '/api' in request.path:
        app.logger.info(request.path)
        auth_cookie = request.headers.get("Authorization")
        app.logger.info( request.headers.get("Authorization") )

    if auth_cookie is None:
        return False

    auth_info = auth_cookie.split("#")
    if len(auth_info) != 2:
        return False

    try:
        user_info = User.query.filter_by(uid=auth_info[1]).first()
    except Exception:
        return False

    if user_info is None:
        return False

    if auth_info[0] != UserService.geneAuthCode( user_info ):
        return False

    if user_info.status != 1:
        return False

    return user_info