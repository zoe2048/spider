# -*- coding:utf-8 -*-

"""
支持将xx.csv文件中的某列写入到txt文件
"""

import csv
from assit import delfile, creat_filepaths
import setting


class CsvProcess(object):
    def __init__(self, infile, outfile, filed):
        self.infile = infile
        self.outfile = outfile
        self.filed = filed

    def extract_data(self):
        with open(self.infile, newline='', encoding='utf-8-sig') as f:
            row_first = next(f).strip()
            title = row_first.split(',')
            filed_index = title.index(self.filed)
            reader = csv.reader(f)
            for row in reader:
                data = row[filed_index]
                yield data

    def write_data_to_text(self):
        outdata = self.extract_data()
        delfile(self.outfile)
        with open(self.outfile, 'a+', encoding='utf-8-sig') as f:
            for c in outdata:
                f.write(c + '\n')


if __name__ == '__main__':
    base = setting.basepath
    names = setting.names
    for name in names:
        fields = names.get(name)
        paths = creat_filepaths(base, name, *fields)
        if len(paths) == 1:
            csvpath = paths[0]
            print('如果要提取数据，缺少要从csv提取的列名称，请在setting中配置')
        elif len(paths) > 1:
            csvpath, *txtpaths = paths[0], paths[1:]
            filenm_field = sorted(zip(*txtpaths, fields))
            for element in filenm_field:
                cp = CsvProcess(csvpath, element[0], element[1])
                cp.write_data_to_text()






