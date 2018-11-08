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

# 可视化IMDB电影top250 上映年份电影数分布
filenm = r'./imdb_year.txt'
outfile = r'./imdb_year.html'
L=[]
x=[]
y=[]
with open(filenm,encoding='utf-8-sig') as f:
    for line in f.readlines():
        L.append(line.strip())

for j in sorted(set(L)):
    count=0
    for i in sorted(L):
        if j == i:
            count += 1
    x.append(j)
    y.append(count)
    print('%s count:%s:' % (j, count))


'''
bar = Bar('IMDB TOP250电影','')
bar.add('电影年份',x,y)
bar.render(outfile)
'''

# 计算top250中所属年代的电影数
#取出年代
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


bar = Bar('IMDB TOP250电影所属年代数量分布','')
bar.add('年代', x_new_uniq, y_new)
bar.render(r'./imdb_ages.html')



