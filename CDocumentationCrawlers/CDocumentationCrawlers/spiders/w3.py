import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from CDocumentationCrawlers.items import Article



class W3Spider(CrawlSpider):
    name = 'w3'
    allowed_domains = ['w3schools.com']
    start_urls = ['https://w3schools.com/c/c_variables_format.php']

    rules = [
        Rule(LinkExtractor(allow=r'c/((?!tryc).)*$'), callback='parse', follow=True)
    ]

    def parse(self, response):
        article = Article() # make a new Article object
        article['title'] = response.xpath('//span[@class="color_h1"]/text()').get()
        article['url'] = response.url
        return article
