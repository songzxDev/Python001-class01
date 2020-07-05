# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pandas as pd
import pymysql
from sqlalchemy import create_engine


class MyscrapyPipeline:
    def process_item(self, item, spider):
        data = pd.DataFrame(item['result'])
        # 建立连接，username替换为用户名，passwd替换为密码，test替换为数据库名
        conn = create_engine('mysql+pymysql://root:123456@localhost:3306/test', encoding='utf-8')
        # 写入数据，table_name为表名，‘replace’表示如果同名表存在就替换掉
        data.to_sql("maoyan_movies", conn, if_exists='replace', index_label='id')
        return item
