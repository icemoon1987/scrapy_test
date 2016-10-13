# -*- coding: utf-8 -*-
import scrapy
import json


class BaiduPicSpider(scrapy.Spider):
    name = "baidu_pic"
    allowed_domains = ["image.baidu.com"]
    word=""
    start_urls = (
        'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=ppt&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%s&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=0&rn=10&gsm=5a&1476340126801=' % ( self.word ),
    )

    multi_map = {
            "_z2C$q" : ":",
            "_z&e3B" : ".",
            "AzdH3F" : "/"
            }

    single_map = {
            "w": "a",
            "k": "b",
            "v": "c",
            "1": "d",
            "j": "e",
            "u": "f",
            "2": "g",
            "i": "h",
            "t": "i",
            "3": "j",
            "h": "k",
            "s": "l",
            "4": "m",
            "g": "n",
            "5": "o",
            "r": "p",
            "q": "q",
            "6": "r",
            "f": "s",
            "p": "t",
            "7": "u",
            "e": "v",
            "o": "w",
            "8": "1",
            "d": "2",
            "n": "3",
            "9": "4",
            "c": "5",
            "m": "6",
            "0": "7",
            "b": "8",
            "l": "9",
            "a": "0"
            }

    def url_decode(self, strin):

        tmp = strin
        result = ""

        for item in self.multi_map:
            tmp = tmp.replace(item, self.multi_map[item])

        for c in tmp:
            if c in self.single_map:
                result += self.single_map[c]
            else:
                result += c
            
        return result


    def parse(self, response):
        result = json.loads(response.body)

        for item in result["data"]:
            if item != {}:
                thumb_img = item.get("thumbURL")
                obj_url = item.get("objURL")
                source_url = item.get("fromURLHost")
                width = item.get("width")
                height = item.get("height")

                param = self.url_decode(obj_url)

                print param

