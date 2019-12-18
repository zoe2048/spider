# -*- coding:utf-8 -*-

import os


def delfile(filenm):
    if os.path.exists(filenm):
        os.remove(filenm)


def creat_filepaths(base, name, *filenms):
    basedir = os.path.join(base, name)
    nms = []
    if 'data' in base:
        suffix = '.txt'
        csvnm = name + '.csv'
        nms.append(csvnm)
    elif 'html' in base:
        suffix = '.html'
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    if len(filenms) >= 1:
        for filenm in filenms:
            filenm = filenm + suffix
            nms.append(filenm)
    filepaths = [os.path.join(basedir, nm) for nm in nms]
    return filepaths


