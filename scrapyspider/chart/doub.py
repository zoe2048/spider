# -*- coding:utf-8 -*-
from pyecharts import Bar
import csv
'''
#示例
bar = Bar('豆瓣TOP250电影','国家电影数')
bar.add('电影数量',
        ['中国','印度','日本','韩国','美国'],
        [16,4,33,9,146]
        )
bar.render('./m.html')
'''

# 由spiders爬虫获取的imdb.csv数据处理
filenm1 = r'./imdb_etags.csv'  #imdb_etags.csv：手动删除imdb.csv中第一行后的文件
filenm2 = r'./imdb_nations.csv'
# imdb
with open(filenm1) as f1, open(filenm2, 'w', newline='') as f2:
    mreader1 = csv.reader(f1)
    for row1 in mreader1:
        # print(row1)
        m_nation = row1[1]
        # print(m_nation)
        mwriter = csv.writer(f2, delimiter=' ')
        mwriter.writerow(m_nation, )



'''
# 可视化豆瓣电影top250 上映年份对应电影数分布
filenm = r'./doub_year.txt'
outfile = r'./doub_year.html'
L=[]  #top250所有电影年份列表
x=[]  #电影年份升序列表
y=[]  #电影年份x对应的电影数列表

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
'''


'''
# 可视化top250中所属年代对应的电影数
#取出年代
x_new = []
for a in [i[:3] for i in x]:
    x_new.append(a+'0s')
x_new_uniq = sorted(list(set(x_new)))

#计算年代对应的电影数
y_new = []
for aa in [a[:3] for a in x_new_uniq]:  # 取年代的前三位：如1930s -> 193
    ages_movies = 0
    for bb in [xx[:3] for xx in L]:  #  所有电影的年份中取年份的前三位：如1932 -> 193
        if aa == bb:
            ages_movies += 1
    y_new.append(ages_movies)

bar = Bar('豆瓣TOP250电影所属年代数量分布','')
bar.add('年代', x_new_uniq, y_new)
bar.render('./doub_ages.html')
'''


#可视化制片国家/地区对应的电影数
d={}
with open(r'./doub_nations.txt',encoding='utf-8-sig') as f:
    for line in f.readlines():
        new_line=line.strip().split('  ') #提取国家列表
        #print(new_line)
        if new_line[0] not in d: #若有合作制片的电影，只取第一个国家
            d[new_line[0]]=1
        else:
            d[new_line[0]]+=1

d_x = list(d.keys())
d_y = list(d.values())
bar = Bar('豆瓣TOP250制片国家/地区电影数量分布','')
bar.add('制片国家/地区',d_x,d_y)
bar.render(r'./doub_nations.html')





