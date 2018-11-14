# -*- coding:utf-8 -*-

from pyecharts import Bar
from pyecharts import Pie


d1 = {'美 国': 122, '中 国 大 陆': 11, '法 国': 11, '意 大 利': 8, '日 本': 31, '印 度': 4, '香 港': 19, '韩 国': 8, '德 国': 4, '英 国': 15, '新 西 兰': 1, '台 湾': 5, '伊 朗': 2, '西 班 牙': 1, '澳 大 利 亚': 1, '丹 麦': 1, '巴 西': 1, '阿 根 廷': 1, '爱 尔 兰': 1, '瑞 典': 1, '泰 国': 1, '博 茨 瓦 纳': 1}
d2 = {'U S A': 152, 'N e w  Z e a l a n d': 3, 'I t a l y': 7, 'J a p a n': 15, 'B r a z i l': 1, 'F r a n c e': 9, 'U K': 22, 'G e r m a n y': 6, 'S o u t h  K o r e a': 3, 'W e s t  G e r m a n y': 2, 'I n d i a': 7, 'D e n m a r k': 1, 'I r a n': 2, 'C a n a d a': 1, 'T u r k e y': 2, 'S p a i n': 1, 'A r g e n t i n a': 2, 'S w e d e n': 3, 'I r e l a n d': 2, 'S o v i e t  U n i o n': 3, 'A u s t r a l i a': 3, 'M e x i c o': 1, 'H o n g  K o n g': 1, 'E s t o n i a': 1}

bar = Bar('豆瓣TOP250制片国家/地区电影数量分布','')
bar.add('制片国家/地区',list(d1.keys()),list(d1.values()))
bar.render(r'./data/doub/doub_nations.html')


attr1 = list(d1.keys())
v1 = list(d1.values())
pie = Pie("豆瓣TOP250电影发行国家/地区分布",title_pos='center')
pie.add("发行国家/地区", attr1, v1,  legend_orient="vertical",legend_pos="left")
pie.render('./test_nations.html')

attr2 = list(d2.keys())
v2 = list(d2.values())
pie = Pie("IMDB TOP250电影发行国家/地区分布",title_pos='center')
pie.add("发行国家/地区", attr2, v2,  legend_orient="vertical",legend_pos="left")
pie.render('./test_nationsi.html')