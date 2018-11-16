# -*- coding:utf-8 -*-

from pyecharts import Bar


def movies_years(infile, year=None, x=None, y=None):
    """
    获取TOP250中电影年份和对应的电影数
    :param infile: txt格式，Top250榜单年份数据
    :param year: 年份列表
    :param x: Top250榜单中出现的不重复的年份列表
    :param y: x列表中对应的年份出现的次数列表
    :return: (l,x,y）
    """
    if year is None:
        year = []
    if x is None:
        x = []
    if y is None:
        y = []
    with open(infile, encoding='utf-8-sig') as f:
        for line in f.readlines():
            year.append(line.strip())
        for j in sorted(set(year)):
            count = 0
            for i in sorted(year):
                if i == j:
                    count += 1
            x.append(j)
            y.append(count)
    return year, x, y


def chart_years(infile, outfile, title):
    """
    可视化TOP250中不同年份对应的电影数
    :param infile: txt格式，movies_years()要处理的电影年份的原始数据
    :param outfile: html格式，可视化的柱形图文件
    :param title: 柱形图图表标题
    """
    bar = Bar(title, '')
    years = movies_years(infile)
    bar.add('电影年份', years[1], years[2])
    bar.render(outfile)


def movies_ages(infile):
    """
    获取Top250榜单年代和电影数
    :param infile: txt格式，Top250榜单的电影年份数据
    :return: x_ages: 电影年代列表，y_new: 年代对应的电影数量列表
    """
    years = movies_years(infile)
    x_new = []
    y_new = []
    for a in [i[:3] for i in years[1]]:
        x_new.append(a + '0s')
    x_ages = sorted(list(set(x_new)))
    for aa in [a[:3] for a in x_ages]:
        ages_movies = 0
        for bb in [b[:3] for b in years[0]]:
            if aa == bb:
                ages_movies += 1
        y_new.append(ages_movies)
    return x_ages, y_new


def chart_ages(i_infile, d_infile, outfile, title):
    """
    可视化Top250榜单不同年代对应的电影数
    :param i_infile: txt格式，IMDb Top250榜单电影年份数据
    :param d_infile: txt格式，豆瓣榜单Top250电影年份数据
    :param outfile: html格式，导出的可视化柱形图的文件
    :param title: 柱形图的标题
    """
    i = movies_ages(i_infile)
    d = movies_ages(d_infile)
    attr = i[0]
    d[1].insert(0, 0)
    v1 = i[1]
    v2 = d[1]
    bar = Bar(title)
    bar.add('IMDb', attr, v1, is_stack=True)
    bar.add('Douban', attr, v2, is_stack=True)
    bar.render(outfile)


# test
if __name__ == '__main__':
    chart_ages(r'./data/imdb/year.txt', r'./data/doub/year.txt', r'./html/movies_ages.html', 'Top250榜单不同年代电影数分布')
    chart_years(r'./data/imdb/year.txt', r'./html/imdb_year.html', 'IMDb Top250不同年份电影数分布')
    chart_years(r'./data/doub/year.txt', r'./html/doub_year.html', '豆瓣 Top250不同年份电影数分布')


















