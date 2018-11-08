# -*- coding:utf-8 -*-
from pyecharts import Bar

#柱形图/条形图

def f(infile,outfile,title,L=None,x=None,y=None):
    # @infile : 要读取数据用于图形化的文件,暂处理txt的文件
    # @outfile：数据可视化的文件，html格式
    if L is None:
        L = []
    if x is None:
        x = []
    if y is None:
        y = []
    with open(infile,encoding='utf-8-sig') as f:
        for line in f.readlines():
            L.append(line.strip())
        for j in sorted(set(L)):    # set过滤列表L中重复数据后按升序重新排序
            count = 0
            for i in sorted(L):
                if i==j:
                    count +=1
            x.append(j)
            y.append(count)
    bar = Bar(title, '')
    bar.add('电影年份', x, y)
    bar.render(outfile)

f(r'./imdb_year.txt',r'./imdb_year.html','IMDB TOP250上榜的电影数所在年份分布')
f(r'./doub_year.txt',r'./doub_year.html','豆瓣电影TOP250上榜电影数所在年份分布')














