# -*- coding:utf-8 -*-


from extractdata import *
import setting
from os.path import join


if __name__ == '__main__':
    n = int(input('''输入运行类型:
    1 生成图表\n
    2 debug\n'''))
    if n == 1:
        title = '{}TOP250不同{}电影数分布'
        for name in ['豆瓣', 'IMDb']:
            nm = setting.files[name]
            infile, outdir = nm['csv'], nm['dir']
            chart_data('year', infile, join(outdir, 'year.html'), title.format(name, '年份'))
            chart_data('ages', infile, join(outdir, 'ages.html'), title.format(name, '年代'))
            chart_data('country1', infile, join(outdir, 'country1.html'), title.format(name, '国家/地区'), 'pie')
    elif n == 2:
        data = extract_data_list('director_cn1', setting.files['豆瓣']['csv'])
        result = [x for x in data.items() if x[1] > 2]
        for r in sorted(result, key=lambda x: x[1]):
            print(r)
        data2 = extract_data_list('director_en1', setting.files['豆瓣']['csv'])
        result2 = [y for y in data2.items() if y[1] > 2]
        for r2 in sorted(result2, key=lambda x: x[1]):
            print(r2)
