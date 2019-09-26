# -*- coding: utf-8 -*-

# 可视化豆瓣和IMDb Top250电影榜单制片国家电影数分布
# country.txt数据来源于extractdata.py从爬取的数据中提取的国家/地区

from pyecharts import Pie


def movies_country(infile, d=None):
    """
    获取制片国家和电影数量
    :param infile: txt格式，Top250榜单电影制片国家数量，如infile = ./data/doub/country.txt
    :param d: 字典，{电影制片国家: 电影数量}
    :return: d {电影制片国家：电影数}
    """
    if d is None:
        d = {}
    with open(infile, encoding='utf-8-sig') as f:
        for line in f.readlines():
            if 'doub' in infile:
                new_line = line.strip().split(' ')
            else:
                new_line = line.strip().split(',')
            # 有联合制片国家的，只取联合制片的第一个国家
            country = new_line[0].strip()
            if country not in d:
                d[country] = 1
            else:
                d[country] += 1
    return d


def chart_country(infile, outfile, title):
    """
    可视化制片国家电影数分布
    :param infile: txt格式，Top250电影制片国家数据，豆瓣文件名包含doub
    :param outfile: html格式，可视化为饼状图的文件
    :param title: 饼状图标题
    """
    c = movies_country(infile)
    attr = list(c.keys())
    v = list(c.values())
    pie = Pie(title, title_pos='center')
    pie.add('制片国家/地区', attr, v, legend_orient='vertical', legend_pos='left', is_label_show=True, label_pos='inner', label_formatter='{c}')
    pie.render(outfile)


# test
if __name__ == '__main__':
    chart_country(r'./data/doub/country.txt', r'./html/doub_country.html', '豆瓣Top250制片国家电影数分布')
    chart_country(r'./data/imdb/country.txt', r'./html/imdb_country.html', 'IMDb Top250制片国家电影数分布')

