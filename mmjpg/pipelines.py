# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import os
import scrapy
# from .settings import IMAGES_STORE as imgs_store
from scrapy.pipelines.images import ImagesPipeline

class MmjpgPipeline(ImagesPipeline):   # 因为下图像，所以可以继承 ImagesPipeline
    def get_media_requests(self, item, info):
        url = item['url'] 
        yield scrapy.Request(url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        os.rename(image_paths[0], 'full/'+item['title']+'.jpg')
