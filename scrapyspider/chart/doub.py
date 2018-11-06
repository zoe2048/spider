# -*- coding:utf-8 -*-
from pyecharts import Bar

'''
#例
bar = Bar('豆瓣TOP250电影','国家电影数')
bar.add('电影数量',
        ['中国','印度','日本','韩国','美国'],
        [16,4,33,9,146]
        )
bar.render('./m.html')
'''

# 可视化豆瓣电影top250 上映年份电影数分布
filenm = r'./doub_year.txt'
outfile = r'./doub_year.html'
L=[]
x=[]
y=[]
with open(filenm,encoding='utf-8-sig') as f:
    for line in f.readlines():
        L.append(line.strip())

for j in sorted(set(L)):
    count=0
    for i in sorted(L):
        if j==i:
            count+=1
    x.append(j)
    y.append(count)
    print('%s count:%s:' %(j,count))


bar = Bar('豆瓣TOP250电影','')
bar.add('电影年份',x,y)
bar.render(outfile)

