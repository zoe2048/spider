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
    if istrans == 'no':
        if field == 'year':
            data = extract_data_list(field, infile)
            sortdata = sorted(data.items(), key=lambda x: x[0])
        elif field == 'ages':
            ages_data = {}
            data = extract_data_list('year', infile)
            for year in data:
                ages = year[:3] + '0s'
                if ages not in ages_data:
                    ages_data[ages] = data[year]
                else:
                    ages_data[ages] += data[year]
            sortdata = sorted(ages_data.items(), key=lambda x: x[0])
        elif field == 'country1':
            data = extract_data_list(field, infile)
            newdata = union_data(data)
            sortdata = sorted(newdata.items(), key=lambda x: x[1], reverse=True)
        else:
            data = extract_data_list(field, infile)
            sortdata = sorted(data.items(), key=lambda x: x[1], reverse=True)
        attr = [x[0] for x in sortdata]
        v1 = [x[1] for x in sortdata]
        return attr, v1
    elif istrans == 'yes':
        if field == 'country1':
            data = extract_data_list(field, infile)
            data_transed = translate_data(data, transfile)
            newdata = union_data(data_transed)
            sortdata = sorted(newdata.items(), key=lambda x: x[1], reverse=True)
            attr = [x[0] for x in sortdata]
            v1 = [x[1] for x in sortdata]
            return attr, v1
    else:
        raise TypeError('是否需要将数据翻译，istrans只能传入yes或no')


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
