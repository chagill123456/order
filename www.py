#!/usr/bin/env/python
# -*- coding:utf-8 -*-
# Author:lj
from application import app






from web.controllers.static import route_static

from web.controllers.upload.Upload import route_upload


from web.controllers.blog.blog import blog_bp
from web.controllers.houtai.ht import blog_ht

from web.controllers.SignIn.SignIn import route_SignIn


app.register_blueprint(route_SignIn,url_prefix="/")

app.register_blueprint(route_static,url_prefix="/static")


app.register_blueprint(route_upload,url_prefix = "/upload" )
app.register_blueprint(blog_ht,url_prefix = "/ht" )
app.register_blueprint(blog_bp,url_prefix = "/blog" )

