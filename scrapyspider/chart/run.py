# -*- coding:utf-8 -*-


from extractdata import *
import setting
import os


if __name__ == '__main__':
    n = int(input('''输入运行类型:
    1 生成图表\n
    2 debug\n'''))
    if n == 1:
        for s in ['豆瓣', 'IMDb']:
            nm = setting.files[s]
            infile, outfile = nm['csv'], nm['dir']
            chart_data('year', infile, os.path.join(outfile, 'year.html'), '{}TOP250不同年份电影数分布'.format(s))
            chart_data('ages', infile, os.path.join(outfile, 'ages.html'), '{}TOP250不同年代电影数分布'.format(s))
            if s == '豆瓣':
                chart_data('country1', infile, os.path.join(outfile, 'country1.html'), '{}TOP250不同国家/地区电影数分布'.format(s),
                           'pie')
            else:
                chart_data_transed('country1', infile, os.path.join(outfile, 'country1.html'),
                                   '{}TOP250不同国家/地区电影数分布'.format(s), 'pie')
    elif n == 2:
        data = extract_data_list('director_cn1', setting.files['豆瓣']['csv'])
        result = [x for x in data.items() if x[1] > 2]
        for r in sorted(result, key=lambda x: x[1]):
            print(r)
        data2 = extract_data_list('director_en1', setting.files['豆瓣']['csv'])
        result2 = [y for y in data2.items() if y[1] > 2]
        for r2 in sorted(result2, key=lambda x: x[1]):
            print(r2)


