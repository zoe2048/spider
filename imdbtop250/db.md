
1. 实现的主程序imdb_top250_movies.py  
2. 涉及到的数据库及表如下  

create database imdb_movies;  
#create database imdb_movies DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;  


存放电影的信息：  
（电影名长度可能会超过45，建议增加长度:实际中发现如The Lord of the Rings: The Fellowship of the Ring已超过45）
create table top_250_movies (  
id int(11) NOT NULL,  
name varchar(45) NOT NULL,  
year int(11) DEFAULT NULL,  
rate float NOT NULL,  
PRIMARY KEY (id)  
)  
;  


存放演员信息：  
create table actors (  
id int(11) NOT NULL,  
name varchar(45) DEFAULT NULL,  
PRIMARY KEY (id)  
)  
;  

存放导演信息：  
create table directors (  
id int(11) NOT NULL,  
name varchar(45) NOT NULL,  
PRIMARY KEY (id)  
)  
;  



存放演员出演电影的记录：  
（使用actor_id和movie_id为外键，与actors和top_250_movies表关联）：  
create table cast_in_movie (  
cast_id int(11) NOT NULL AUTO_INCREMENT,  
actor_id int(11) NOT NULL,  
movie_id int(11) NOT NULL,  
PRIMARY KEY (cast_id),  
KEY actor_id_idx (actor_id),  
KEY movie_id_idx (movie_id),  
CONSTRAINT actor_id FOREIGN KEY (actor_id) REFERENCES actors (id) ON DELETE NO ACTION ON UPDATE NO ACTION,  
CONSTRAINT movie_id FOREIGN KEY (movie_id) REFERENCES top_250_movies (id) ON DELETE NO ACTION ON UPDATE NO ACTION  
)  
;


存放导演导演的每一部电影的信息：  
（使用director_id与movie_id做为外键与directors和top_250_movies表关联）  
create table direct_movie (  
id int(11) NOT NULL AUTO_INCREMENT,  
director_id int(11) NOT NULL,  
movie_id int(11) NOT NULL,  
PRIMARY KEY (id),  
KEY director_id_idx (director_id),  
KEY movie_id_idx (movie_id),  
CONSTRAINT director_id FOREIGN KEY (director_id) REFERENCES directors (id) ON DELETE NO ACTION ON UPDATE NO ACTION  
)  
;  

TOP250导演次数
SELECT dm.director_id, d.name, count(dm.id) as direct_count  
FROM imdb_movies.direct_movie as dm  
JOIN imdb_movies.directors as d ON d.id = dm.director_id  
group by dm.director_id  
order by direct_count desc  


TOP250 演员次数  
SELECT cm.actor_id, a.name, count(cm.actor_id) as count_of_act  
FROM imdb_movies.cast_in_movie as cm  
JOIN imdb_movies.actors as a ON a.id = cm.actor_id  
group by cm.actor_id  
order by count_of_act desc  


3.实际遇到的情况：  
- 查看脚本执行完后top_250_movies表中，只有240条记录（实际应为250条记录）  
- 查看direct_movie表，只有249条记录（实际应为250条）  
- 通过查询语句，导演排名后数据，导演次数相加只有249（实际应为250）  
以上问题皆因电影名、导演名等含有单引号，未做转义，没有成功存入数据库；  
转义后，发现电影条数还是不足250条，发现是创建的保存电影信息的表的电影名字段长度不足，有电影名长度超过了设定的长度；  
