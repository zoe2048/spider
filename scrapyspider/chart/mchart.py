# -*- coding:utf-8 -*-
from pyecharts import Bar

# 获取TOP250中电影年份和对应的电影数
def movies_years(infile,L=None,x=None,y=None):
    '''
    :param infile：要读取数据用于图形化的文件,txt的文件
    :param x：X轴，infile处理后的top榜中按升序排列的电影年份
    :param y：Y轴，年份对应的电影数
    :return: （L,x,y) 所有电影年份、过滤重复年份后的电影年份、电影数
    '''
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
    return L,x,y

# 可视化TOP250中不同年代对应的电影数
def chart_years(infile,outfile,title):
    '''
    :param infile: 在movies_years()中要处理的电影数据原始文件
    :param outfile: 可视化柱形图后导出的文件，html格式
    :param title: 可视化的柱形图的图示标题
    '''
    bar = Bar(title,'')
    years = movies_years(infile)
    bar.add('电影年份',years[1],years[2])
    bar.render(outfile)

# 可视化TOP250中不同年代对应的电影数
def chart_ages(infile,outfile,title):
    '''
    :param infile: 在movies_years() 中要处理的电影数据原始文件
    :param outfile: 可视化柱形图后导出的文件，html格式
    :param title: 可视化柱形图的图示标题
    '''
    years= movies_years(infile)
    x_new = []
    y_new = []
    for a in [i[:3] for i in years[1]]:
        x_new.append(a + '0s')
    x_new_uniq = sorted(list(set(x_new)))
    for aa in [a[:3] for a in x_new_uniq]:
        ages_movies = 0
        for bb in [b[:3] for b in years[0]]:
            if aa == bb:
                ages_movies += 1
        y_new.append(ages_movies)
    bar = Bar(title,'')
    bar.add('年代',x_new_uniq,y_new)
    bar.render(outfile)

# test
chart_years(r'./imdb_year.txt',r'./imdb_years.html','IMDB TOP250中不同年份对应的电影数分布')
chart_ages(r'./imdb_year.txt',r'./imdb_ages.html','IMDB TOP250中不同年代对应的电影数分布')














