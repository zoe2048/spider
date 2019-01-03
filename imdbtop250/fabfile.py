# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 本地使用，适用于python2环境下

import os,re


from datetime import datetime


# 导入fabric api
from fabric.api import *


# 服务器登录用户名及服务器地址
# env.user='root'
# env.hosts=['ip']
env.user=''
env.hosts=['']


# 服务器mysql用户名和口令
db_user=''
db_password=''


_TMP_FILE='tmp'

_REMOTE_TMP_DIR = '/home/ubuntu/%s' % _TMP_FILE



def deploy():
    put('./imdb_top250_movies.py','/home/ubuntu/tmp/.')





