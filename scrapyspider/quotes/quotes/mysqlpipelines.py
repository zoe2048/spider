# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql.cursors


class QuotesPipeline(object):

    def process_item(self, item, spider):
        connect = pymysql.connect(host='', user='', password='', db='', port=3306)
        cursor = connect.cursor()
        insert_sql = """
        insert into quotes(content, author, tags) values(%s, %s, %s)
        """
        item['content'] = pymysql.escape_string(item['content'])
        item['author'] = pymysql.escape_string(item['author'])
        item['tags'] = pymysql.escape_string(item['tags'])
        cursor.execute(insert_sql, (item['content'], item['author'], item['tags']))
        connect.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()


class AuthorPipeline(object):

    def process_item(self, item, spider):
        connect = pymysql.connect(host='', user='', password='', db='', port=3306)
        cursor = connect.cursor()
        insert_sql = """
        insert into author(name, birth, country, bio) values(%s, %s, %s, %s)
        """
        item['name'] = pymysql.escape_string(item['name'])
        item['birth'] = pymysql.escape_string(item['birth'])
        item['country'] = pymysql.escape_string(item['country'])
        item['bio'] = pymysql.escape_string(item['bio'])
        cursor.execute(insert_sql, (item['name'], item['birth'], item['country'], item['bio']))
        connect.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()

