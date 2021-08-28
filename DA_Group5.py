# T3
import requests
# T4
url = 'https://brickset.com/sets/year-2002'
# T5 i
r = requests.get(url)
print(r.text)
# T5 ii
print("Status code:")
print("\t *", r.status_code)
# T5 iii
h = requests.head(url)
print("Header:")
print("*********")
for x in h.headers:
    print("\t", x, ":", h.headers[x])
print("***********")
# T5 iv
headers = {
    'User-Agent':'Mobile'
}
url2 = 'http://httpbin.org/headers'
rh = requests.get(url2, headers=headers)
print(rh.text)
# Source reference from "Lab 10b - Spoofing header in HTTP Get request"
# ~Aniyutharan
# ----------------------------------------------------------------------------------------------------------------------
# T3
import scrapy
from scrapy.http.request import Request
# scrapy runspider DA_Group5.py
# T6 i
class BrickSetSpider(scrapy.Spider):
    name = "brick_spider"
    start_urls = ['https://brickset.com/sets/year-2002']
    def start_requests(self):
        headers = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9'}
        for url in self.start_urls:
            yield Request(url, headers=headers)
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
# T6 iii
# scrapy runspider DA_Group5.py -o resultes.json -t json
# T7
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
# Source reference from "Lab 10c - Using Scrapy webcrawler"
# ~Zi Xuan
# ----------------------------------------------------------------------------------------------------------------------
