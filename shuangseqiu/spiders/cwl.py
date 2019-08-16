# -*- coding: utf-8 -*-
import scrapy
import re
from ast import literal_eval
from shuangseqiu.items import ShuangseqiuItem
from shuangseqiu.pipelines import ShuangseqiuPipeline

class CwlSpider(scrapy.Spider):
    name = 'cwl'
    allowed_domains = ['www.cwl.gov.cn']
    start_urls = ['http://www.cwl.gov.cn/kjxx/ssq/kjgg/list.shtml']

    def parse(self, response):
        gglist = response.xpath('//*[@id="content"]/div[1]/ul/li')
        for gg in gglist:
            detailUrl = gg.xpath('./span[2]/a/@href').extract_first()
            if detailUrl:
                yield scrapy.Request("http://www.cwl.gov.cn" + detailUrl, callback=self.child_parse)

        next_url = response.xpath('//*[@id="content"]/div[1]/div[1]/ul/li[11]/a/@href').extract_first()
        if(next_url):
            yield scrapy.Request("http://www.cwl.gov.cn/kjxx/ssq/kjgg/" + next_url, callback=self.parse)
        pass

    def child_parse(self, response):
        item = ShuangseqiuItem()
        item['date'] = response.xpath('/html/body/div[3]/div/div/div[1]/table/tr[1]/td/text()').extract_first()
        result = response.xpath('/html/head/script[last()]/text()').extract_first()

        result =re.search('\\[(\S+)\\]',result).group()
        if not result:
            return
        result = literal_eval(result)
        item['qiuH1'],item['qiuH2'],item['qiuH3'],item['qiuH4'],item['qiuH5'],item['qiuH6']=result[:]
        item['qiuL'] = response.xpath('/html/body/div[3]/div/div/div[1]/div/div/span[@class="qiuL"]/text()').extract_first()
        pipline = ShuangseqiuPipeline()
        pipline.process_item(item,self)
        pass