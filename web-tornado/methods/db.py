#!/usr/bin/env python
# coding=utf-8

import pymysql

conn = pymysql.connect(host="localhost", user="admin", passwd="admin", db="qiwsirtest", port=3306, charset="utf8")
#连接对象
cur = conn.cursor()    #游标对象
#cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
#cur.execute("select * from users")
#print(cur.fetchone())
#print(cur.fetchone())

#cur.execute("insert into users (username,password,email) values (%s,%s,%s)",("python","123456","python@gmail.com"))
# cur.executemany("insert into users (username,password,email) values (%s,%s,%s)",
#                 (
#                     ("google","111222","g@gmail.com"),
#                     ("facebook","222333","f@face.book"),
#                     ("github","333444","git@hub.com"),
#                     ("docker","444555","doc@ker.com")
#                 )
#                 )
# conn.commit()
#cur.execute("select * from users")
#lines = cur.fetchall()
#for line in lines:
#    print(line)