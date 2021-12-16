# -*- coding:utf-8 -*-

"""
提取csv列数据，统计列中元素出现的次数并可视化为图表
"""

from pyecharts import Pie, Bar
from transdata import *


def extract_data_list(field, infile):
    """
    从csv文件中提取某列数据
    :param field: 列名
    :param infile: csv源文件
    :return: {列元素: 出现次数}
    """
    field_data = {}
    with open(infile, encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        headers = next(reader)
        field_id = headers.index(field)
        for line in reader:
            k = line[field_id]
            if k not in field_data:
                field_data[k] = 1
            else:
                field_data[k] += 1
        return field_data


def get_chart_data(field, infile, istrans='no', *, transfile=None):
    """
    处理（排序、语言翻译）提取出的列数据
    :param field: 列名
    :param infile: csv文件
    :param istrans: 数据是否需要翻译
    :param transfile: 翻译所需的文件
    :return: 图表所需的横坐标数据和对应的纵坐标数据
    """
    if field == 'ages':
        field_data = extract_data_list('year', infile)
        data = {}
        for year in field_data:
            ages = year[:3] + '0s'
            if ages not in data:
                data[ages] = field_data[year]
            else:
                data[ages] += field_data[year]
        sortdata = sorted(data.items(), key=lambda x: x[0])
    elif field == 'country1':
        field_data = extract_data_list(field, infile)
        if istrans == 'yes':
            data_transed = translate_data(field_data, transfile)
            data = union_data(data_transed)
        elif istrans == 'no':
            data = union_data(field_data)
        sortdata = sorted(data.items(), key=lambda x: x[1], reverse=True)
    elif field == 'year':
        data = extract_data_list(field, infile)
        sortdata = sorted(data.items(), key=lambda x: x[0])
    else:
        data = extract_data_list(field, infile)
        sortdata = sorted(data.items(), key=lambda x: x[1], reverse=True)
    attr = [x[0] for x in sortdata]
    v1 = [x[1] for x in sortdata]
    return attr, v1


def chart_data(field, infile, outfile, title, charttype='bar'):
    """
    数据可视化为图表
    :param field: 可视化的字段
    :param infile: 传入的csv源文件
    :param outfile: 可视化的图表文件
    :param title: 图表title
    :param charttype: 图表类型
    """
    if 'country' in field and 'imdb' in infile:
        istrans, transfile = 'yes', 'countrytrans.txt'
        chardata = get_chart_data(field, infile, istrans=istrans, transfile=transfile)
    else:
        chardata = get_chart_data(field, infile)
    attr = chardata[0]
    v1 = chardata[1]
    if charttype == 'bar':
        char = Bar(title, '')
        char.add(field, attr, v1)
    elif charttype == 'pie':
        char = Pie(title, title_pos='center')
        char.add(field, attr, v1, legend_orient='vertical', legend_pos='left', is_label_show=True, label_pos='inner', label_formatter='{c}')
    else:
        raise TypeError('缺少图表类型')
    char.render(outfile)
