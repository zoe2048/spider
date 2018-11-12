# -*- coding:utf-8 -*-
from pyecharts import Bar
import csv
import os

'''
#可视化柱形图示例
bar = Bar('豆瓣TOP250电影','国家电影数')
bar.add('电影数量',
        ['中国','印度','日本','韩国','美国'],
        [16,4,33,9,146]
        )
bar.render('./m.html')
'''


'''
imdb.csv：爬取的原始数据
imdb_etags.csv: 爬取的原始数据删除字段名后的数据
'''
# 由 spiders 爬虫获取的imdb.csv数据处理
#imdb_etags.csv：手动删除imdb.csv中第一行后的文件
pwd = os.getcwd()
data_dir = r'data\imdb'
data_dir_path = os.path.join(pwd,data_dir)
data_filenm = 'imdb_etags.csv'

# ===============提取发行国家数据，可视化为柱形图==================
'''
imdb_nations.csv：从imdb_etags.csv中提取的只有国家的数据
imdb_nations.txt：手动存储imdb_nations.csv为txt文件,后面想办法自动处理
imdb_nn.txt': 清理ok的数据
'''
nation_filenm = 'imdb_nations.csv'
filenm1 = os.path.join(data_dir_path,data_filenm)
filenm2 = os.path.join(data_dir_path,nation_filenm)
with open(filenm1) as f1, open(filenm2, 'w', newline='') as f2:
    mreader1 = csv.reader(f1)
    for row1 in mreader1:
        m_nation = row1[1]  
        mwriter = csv.writer(f2, delimiter=' ')
        mwriter.writerow(m_nation, )

nation_filenm_txt = 'imdb_nations.txt'
data_filenm_txt = 'imdb_nn.txt'
filenm3 = os.path.join(data_dir_path,nation_filenm_txt)
filenm4 = os.path.join(data_dir_path,data_filenm_txt)
with open(filenm3,encoding='utf-8-sig') as f3,open(filenm4, 'w', encoding='utf-8-sig') as f4:
    for line in f3.readlines():
        l= line.strip().replace('" "', '')
        f4.write(l + '\n')

out_filenm = 'imdb_nations.html'
outfile = os.path.join(data_dir_path,out_filenm)
d={}
#发行国家对应的电影数
with open(filenm4,encoding='utf-8-sig') as f:
    for line in f.readlines():
        new_line=line.strip().split(',')
        #print(new_line)
        nation=new_line[0].strip()
        if nation not in d: #若有合作制片的电影，只取第一个国家
            d[nation]=1
        else:
            d[nation]+=1
d_x = list(d.keys())
d_y = list(d.values())
#可视化
bar = Bar('IMDB TOP250制片国家/地区电影数量分布', '')
bar.add('制片国家/地区', d_x, d_y)
bar.render(outfile)
# ===============提取发行国家数据，可视化发行国家发行电影数分布柱形图==================


#================提取上映年份数据，可视化不同年份上映电影数分布==============================
# 可视化IMDB电影top250 上映年份电影数分布
#imdb_year.txt：已经清理好的数据
year_filenm_txt = 'imdb_year.txt'
year_out_filenm = 'imdb_year.html'
filenm_year = os.path.join(data_dir_path,year_filenm_txt)
outfile = os.path.join(data_dir_path,year_out_filenm)
L=[]  
x=[]
y=[]
#年份对应的电影数
with open(filenm_year,encoding='utf-8-sig') as f:
    for line in f.readlines():
        L.append(line.strip())
for j in sorted(set(L)):
    count=0
    for i in sorted(L):
        if j == i:
            count += 1
    x.append(j)
    y.append(count)
    #print('%s count:%s:' % (j, count))
#可视化
bar = Bar('IMDB TOP250电影','')
bar.add('电影年份',x,y)
bar.render(outfile)
#================提取上映年份数据，可视化不同年份上映电影数分布==============================



#================提取不同年代上映的电影数据，可视化不同年代电影数分布==============================
#取出年代
ages_out_filenm = 'imdb_ages.html'
outfile = os.path.join(data_dir_path,ages_out_filenm)
x_new = []
for a in [i[:3] for i in x]:
    x_new.append(a+'0s')
x_new_uniq=sorted(list(set(x_new)))
#计算年代对应的电影数
y_new = []
for aa in [a[:3] for a in x_new_uniq]:  # 取年代的前三位：如1930s -> 193
    ages_movies = 0
    for bb in [xx[:3] for xx in L]:  #  所有电影的年份中取年份的前三位：如1932 -> 193
        if aa == bb:
            ages_movies += 1
    y_new.append(ages_movies)
#可视化
bar = Bar('IMDB TOP250电影所属年代数量分布','')
bar.add('年代', x_new_uniq, y_new)
bar.render(outfile)
#================提取不同年代上映的电影数据，可视化不同年代电影数分布==============================






