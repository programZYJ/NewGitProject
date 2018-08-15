# -*- coding: utf-8 -*-
import scrapy
import os
from scrapy.selector import Selector
import re
import urllib.request
from myimg.items import MyimgItem
class ImgSpider(scrapy.Spider):
    name = 'img'
    allowed_domains = ['http://www.xiaohuar.com']
    # start_urls = ['http://www.xiaohuar.com/list-1-0.html']
    start_urls = []
    url1 = 'http://www.xiaohuar.com/list-1-'
    for i in range(20):
        url = url1 + str(i) + '.html'
        start_urls.append(url)
    print("aaaaaaaaaaaaaaaaaa",start_urls)
    def parse(self, response):
        current_url = response.url  # 爬取请求时的url
        body = response.body  # 返回的html
        # open('hhh.html',"wb").write(body)
        if re.match('http://www.xiaohuar.com/list-1-\d+.html', response.url):
            for each in response.xpath('//div[@class="item masonry_brick"]//div[@class="item_t"]//div[@class="img"]'):
                item = MyimgItem()
                src = each.xpath('a/img/@src').extract()  # 查询所有img标签的src属性，即获取校花图片地址
                name = each.xpath('span/text()').extract()  # 获取span的文本内容，即校花姓名
                school = each.xpath('div[@class="btns"]/a/text()').extract()  # 校花学校
                item['src'] = src[0]
                item['name'] = name[0]
                item['school'] = school[0]
                yield item
        all_urls = response.xpath('//a/@href').extract()  # 提取界面所有的url
        for url in all_urls:  # 遍历获得的url，如果满足条件，继续爬取
            if url.startswith('http://www.xiaohuar.com/list-1-'):
                urls = url
                open('hhh.html', "wb").write(response.body)
                yield scrapy.Request(url, callback=self.parse)
