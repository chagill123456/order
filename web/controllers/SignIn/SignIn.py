# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, make_response, g, redirect
from common.libs.Helper import ops_render,getCurrentDate,iPagination,getDictFilterField
from common.models.User import (User)
from common.libs.user.UserService import (UserService)

from common.libs.UrlManager import (UrlManager)
from application import app, db
import json

route_SignIn = Blueprint( 'index_page',__name__ )

@route_SignIn.route("/")
def index():
    return ops_render( "SignIn/index.html" )

@route_SignIn.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        g.current_user = check_login()
        if g.current_user:
            return redirect(UrlManager.buildUrl("/blog"))
        return ops_render("SignIn/index.html")

    resp = {'code': 200, 'msg': '登录成功~~', 'data': {}}
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名~~"
        return jsonify(resp)

    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的邮箱密码~~"
        return jsonify(resp)

    user_info = User.query.filter_by(login_name=login_name).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名~~"
        return jsonify(resp)



    if user_info.login_pwd != UserService.genePwd( login_pwd,user_info.login_salt ):
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名和密码-2~~"
        return jsonify(resp)

    g.current_user=user_info
    response = make_response(json.dumps({'code': 200, 'msg': '登录成功~~'}))
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
        UserService.geneAuthCode(user_info), user_info.uid), 60 * 60 * 24 * 120)  # 保存120天
    return response

@route_SignIn.route("/register",methods = [ 'GET','POST'])
def register():
    if request.method == "GET":
        return ops_render("SignIn/register.html")

    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    req = request.values

    username = req['username'] if 'username' in req else ''
    nickname = req['nickname'] if 'nickname' in req else ''
    password = req['password'] if 'password' in req else ''
    email = req['email'] if 'email' in req else ''
    
    User_info = User.query.filter_by(login_name=username).first()
    if User_info:
        resp['code'] = -1
        resp['msg'] = "已有此账号！"
        return jsonify(resp)

    salt= UserService.geneSalt()
    print(salt)
    password= UserService.genePwd(password,salt)


    model_User_info = User()
    model_User_info.created_time = getCurrentDate()
    model_User_info.login_name = username
    model_User_info.nickname = nickname
    model_User_info.login_salt = salt
    model_User_info.login_pwd = password
    model_User_info.email=email
    model_User_info.updated_time = getCurrentDate()
    db.session.add(model_User_info)
    db.session.commit()
    return jsonify(resp)


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




