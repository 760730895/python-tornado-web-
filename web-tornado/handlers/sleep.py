#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-12-25 下午7:10
# @Author  : hucl

import tornado.web
import tornado.gen
from handlers.base import BaseHandler

import time

# class SleepHandler(BaseHandler):
#     @tornado.web.asynchronous
#     def get(self):
#         tornado.ioloop.IOLoop.instance().add_timeout(time.time() + 17, callback=self.on_response)
#         # time.sleep(40)
#     def on_response(self):
#         self.render("sleep.html")
#         self.finish()
class SleepHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        # yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 17)
        yield tornado.gen.sleep(17)
        self.render("sleep.html")

class SeeHandler(BaseHandler):
    def get(self):
        self.render("see.html")