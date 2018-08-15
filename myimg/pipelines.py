# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import json
from urllib.request import urlretrieve
class MyimgPipeline(object):
    def __init__(self):
        self.file = open('img.json', 'wb')

    def process_item(self, item, spider):
        # content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # self.file.write(content.encode('utf-8'))
        absoluteSrc = "http://www.xiaohuar.com" + item['src']  # 拼接实际路径，因为.extract()会返回一个list，但是我们是依次取得div，所以是取第0个
        file_name = "%s_%s.jpg" % (item['school'], item['name'])  # 拼接文件名，学校_姓名
        file_path = os.path.join("D:/DjangoProject/myimg/image/", file_name)  # 拼接这个图片的路径
        if os.path.exists(file_name):
            pass
        else:
            urlretrieve(absoluteSrc, file_path)  # 接收文件路径和需要保存的路径，会自动去文件路径下载并保存到我们指定的本地路径
        return item

    def close_spider(self, spider):
        self.file.close()