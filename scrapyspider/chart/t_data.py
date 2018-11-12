#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import csv
import re

# 根据爬虫爬取出的数据，再次处理，进一步提取出需要的数据
# 提取国家
filenm1 = './douban_etags.csv' #douban_movies_top250爬取的数据清除第一行字段名后的数据
filenm2 = './nations.csv'
filenm3 = './doub_nations.txt' #filenm2处理后保存的txt文件
filenm4 = './year.csv'

'''
# doub
with open(filenm1) as f1,open(filenm2,'w',newline='') as f2:
    mreader1 = csv.reader(f1)
    for row1 in mreader1:
        #print(row1)
        if len(row1):
            #print(row1)
            m_text = row1[-1].replace('?','')
            m_nations = m_text.split(',')[1].strip()
            #print(m_nations)
            m_nation = m_nations.split('/')[1]
            #print(m_nation)
            mwriter = csv.writer(f2,delimiter=' ')
            mwriter.writerow(m_nation,)

# 计算电影发行国家和对应的电影数（若同一电影有联合制片国家/地区的，只取第一个国家计算
d={}
with open(r'./doub_nations.txt',encoding='utf-8-sig') as f:
    for line in f.readlines():
        new_line=line.strip().split('  ') #提取国家列表
        if new_line[0] not in d:
            d[new_line[0]]=1
        else:
            d[new_line[0]]+=1
'''


'''
# 提取年份
with open(filenm1) as f1,open(filenm4,'w',newline='') as f4:
    mreader1 = csv.reader(f1)
    for row1 in mreader1:
        if len(row1):
            m_text = row1[-1].replace('?','').strip()
            m_text_s = m_text.strip(',')
            m_years = m_text_s.split(',')[1].strip()
            m_year = m_years.split('/')[0].strip()
            year= re.match('\d+',m_year).group()
            mwriter = csv.writer(f4)
            #mwriter = csv.writer(f4,delimiter=' ')
            mwriter.writerow((year,))
'''

L = []
with open(r'./year.txt', encoding='utf-8-sig') as f1:
    for line in f1.readlines():
        L.append(line.strip())
# print(L)


l = set(L)
x = []
y = []
for j in l:
    count = 0
    for i in L:
        if j == i:
            count += 1
    x.append(j)
    y.append(count)
    print('%s count:%s:' % (j, count))
print(x)
print(y)






