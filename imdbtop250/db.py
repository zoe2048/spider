# -*- coding:utf-8 -*-
#连接数据库

import pymysql
import mysql.connector

# 使用pymysql
db = pymysql.connect()
cursor = db.cursor("192.168.99.100", "root", "admin", "imdb_movie")
db.close()


# 使用mysql.connector
conn = mysql.connector.connect(host='', port='', user='', password='', database='', charset='')
cursor = conn.cursor()
cursor.close()
conn.close()



