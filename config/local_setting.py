#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:lj

SERVER_PORT=8999
SQLALCHEMY_DATABASE_URI ='mysql://root:123456!a@127.0.0.1/article'
SQLALCHEMY_TRACK_MODIFICATIONS =False


APP = {
    'domain': 'http://127.0.0.1:8999'
}
#有可能你使用浏览器看到的一串字符串不是那么容易看懂的，这是因为python底层使用unicode编码。
#通过设置下面的参数可以解决这个问题。
JSON_AS_ASCII = False

AUTH_COOKIE_NAME = "aritice_wenrene"

SEO_TITLE = "Python Flask构建微信小程序订餐系统"
##过滤url
IGNORE_URLS = [
    "^/SignIn"
    "^/api"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

MINA_APP={
    "appid":'wxb3e553d0126cad5c',
    "appkey":'0449b80b47b939ebb39a3b08eb338a90'
}

PAGE_SIZE = 50
PAGE_DISPLAY = 10

STATUS_MAPPING = {
    "1":"正常",
    "0":"已删除"
}

UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'/web/static/upload/',
    'prefix_url':'/static/upload/'
}

