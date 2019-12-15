# -*- coding:utf-8 -*-

import os


def delfile(filenm):
    if os.path.exists(filenm):
        os.remove(filenm)
