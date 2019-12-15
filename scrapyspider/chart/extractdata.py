# -*- coding:utf-8 -*-

"""
爬虫爬取的数据，保存到csv文件中提取出制片国家/地区的数据
并保存到txt文件供制片国家/地区电影数分布数据可视化使用
"""

import csv
from assit import delfile
import setting


doub_path = setting.doub.get("doub_path")
doub_csv = setting.doub.get("doub_csv")
doub_country = setting.doub.get("cfilenm")
doub_year = setting.doub.get("yfilenm")

imdb_path = setting.imdb.get("imdb_path")
imdb_csv = setting.imdb.get("imdb_csv")
imdb_country = setting.imdb.get("cfilenm")
imdb_year = setting.imdb.get("yfilenm")


def extract_data(infile, datatype):
    """
    自动获取提取csv中某字段的index，读取数据，返回该数据的生成器
    :param infile: csv原始文件
    :param datatype: 从csv文件要读取的数据
    :return: 提取的数据
    """
    with open(infile, newline='', encoding='utf-8-sig') as f:
        row_first = next(f).strip()
        title = row_first.split(',')
        data_index = title.index(datatype)
        reader = csv.reader(f)
        for row in reader:
            data = row[data_index]
            yield data


def write_data_to_txt(infile, outfile, datatype='country'):
    """
    提取csv文件中某字段名称的数据，写入txt文件
    :param infile: csv原始文件
    :param outfile: 生成的txt文件
    :param datatype: 生成的txt文件中数据在csv的字段名称
    :return:
    """
    if 'doub' in infile:
        if datatype == 'country':
            outdata = extract_data(infile, datatype)
            delfile(doub_country)
        elif datatype == 'year':
            outdata = extract_data(infile, datatype)
            delfile(doub_year)
    elif 'imdb' in infile:
        if datatype == 'country':
            outdata = extract_data(infile, datatype)
            delfile(imdb_country)
        elif datatype == 'year':
            outdata = extract_data(infile, datatype)
            delfile(imdb_year)
    else:
        print('提取数据的源文件csv不存在或有问题')
    with open(outfile, 'a+', encoding='utf-8-sig') as f:
        for c in outdata:
            f.write(c + '\n')


if __name__ == '__main__':
    # 生成country.txt
    write_data_to_txt(doub_csv, doub_country)
    write_data_to_txt(imdb_csv, imdb_country)

    # 生成year.txt
    write_data_to_txt(doub_csv, doub_year, 'year')
    write_data_to_txt(imdb_csv, imdb_year, 'year')







