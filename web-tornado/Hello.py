#!/usr/bin/env python
#coding:utf-8

import tornado.httpserver
#这个模块就是用来解决web服务器的http协议问题，它提供了不少属性方法，实现客户端和服务器端的互通。
# Tornado的非阻塞、单线程的特点在这个模块中体现。
import tornado.ioloop
#能够实现非阻塞socket循环，不能互通一次就结束呀。
import tornado.options
#这是命令行解析模块
import tornado.web
#它提供了一个简单的Web框架与异步功能，从而使其扩展到大量打开的连接，使其成为理想的长轮询。

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

#按照习惯，类的名字中的单词首字母都是大写的，并且如果这个类是请求处理程序类，那么就最好用Handler结尾
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', welcome you to read: www.itdiffer.com')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
