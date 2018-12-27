#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-12-25 下午6:00
# @Author  : hucl

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")