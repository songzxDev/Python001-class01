# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pandas as pd


class MyscrapyPipeline:
    def process_item(self, item, spider):
        data = pd.DataFrame(item['result'])
        data.to_csv('./maoyan2.csv', index=False, header=False, encoding="utf_8_sig")
        return item
