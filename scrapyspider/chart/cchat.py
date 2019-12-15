# -*- coding: utf-8 -*-

# 可视化豆瓣和IMDb Top250电影榜单制片国家/地区电影数分布
# country.txt数据来源于extractdata.py生成的txt文件

from pyecharts import Pie
import setting
from assit import delfile

doub_country = setting.doub.get("cfilenm")
doub_chtml = setting.doub.get("chtml")

imdb_country = setting.imdb.get("cfilenm")
imdb_chtml = setting.imdb.get("chtml")


def movies_country(infile, d=None):
    """
    获取制片国家/地区和对应的电影数量
    :param infile: country.txt
    :param d: list
    :return:  {电影制片国家：电影数}
    """
    if d is None:
        d = {}
    with open(infile, encoding='utf-8-sig') as f:
        for line in f.readlines():
            if 'doub' in infile:
                new_line = line.strip().split(' ')
            elif 'imdb' in infile:
                new_line = line.strip().split(',')
            else:
                print('制片国家/地区文件内数据问题')
            # 有联合制片国家/地区的，只取第一个国家/地区
            country = new_line[0].strip()
            if country not in d:
                d[country] = 1
            else:
                d[country] += 1
    return d


def creat_country_transtab(infile):
    """
    生成国家名称英文-中文映射、国家代码-中文映射
    :param infile: 国家英文名称、国家代码、中文名称文件 countrytrans.txt
    :return:
    """
    d1 = {}
    d2 = {}
    d3 = {'UK': '英国', 'West Germany': '西德', 'South Korea': '韩国', 'Soviet Union': '苏联'}
    with open(infile, encoding='utf-8-sig') as f:
        for line in f.readlines():
            new_line = line.strip().split(',')
            country1 = new_line[0].strip()
            country2 = new_line[1].strip()
            if country1 not in d1:
                d1[country1] = new_line[2]
            if country2 not in d2:
                d2[country2] = new_line[2]
    return d1, d2, d3


# 将imdb国家名称中英文转换
def translate_country(intab, outtab1, outtab2, outtab3):
    """
    将国家英文名转为中文
    :param intab: {英文名制片国家: 电影数}
    :param outtab1: {国家英文名: 中文名}
    :param outtab2: {国家编码: 中文名}
    :param outtab3: intab中国家在outtab1和outtab2中没有对应映射的国家
    :return:
    """
    newintab = {}
    for en in intab:
        if en in outtab1:
            cn = outtab1[en]
            newintab[cn] = intab[en]
        elif en in outtab2:
            cn = outtab2[en]
            newintab[cn] = intab[en]
        elif en in outtab3:
            cn = outtab3[en]
            newintab[cn] = intab[en]
        else:
            print('中英文对照国家没有对应数据：%s' % en)
    return newintab


def get_chart_data(infile):
    """
    生成制片国家/地区:电影数分布饼状图所需的属性/值
    :param infile: country.txt
    :return:
    """
    cn = []
    num = 0
    newdata = []
    if 'doub' in infile:
        data = movies_country(infile)
    if 'imdb' in infile:
        # 先将英文名国家转为中文
        intab = movies_country(infile)
        transtab = creat_country_transtab('countrytrans.txt')
        data = translate_country(intab, transtab[0], transtab[1], transtab[2])
    for item in data.items():
        if item[0] in '中国大陆中国香港中国澳门中国台湾香港台湾澳门':
            cn.append(item)
            num += item[1]
            print('%s 制片国家/地区中国详情：%s' % (infile, cn))
        else:
            newdata.append(item)
    if len(cn) > 0:
        newdata.append(('中国', num))
    newdata = sorted(newdata, key=lambda x: x[1], reverse=True)
    attr = [i[0] for i in newdata]
    v = [i[1] for i in newdata]
    return attr, v


def chart_country(infile, outfile, title):
    """
    可视化制片国家/地区电影数分布
    :param infile: country.txt
    :param outfile: 可视化后的国家/地区:电影数分布的饼状图，html文件
    :param title: 饼状图标题
    """
    data = get_chart_data(infile)
    attr = data[0]
    v = data[1]
    pie = Pie(title, title_pos='center')
    pie.add('制片国家/地区', attr, v, legend_orient='vertical', legend_pos='left', is_label_show=True, label_pos='inner', label_formatter='{c}')
    pie.render(outfile)


# test
if __name__ == '__main__':
    delfile(doub_chtml)
    delfile(imdb_chtml)
    chart_country(doub_country, doub_chtml, '豆瓣Top250电影制片国家/地区分布')
    chart_country(imdb_country, imdb_chtml, 'IMDb Top250电影制片国家/地区分布')

