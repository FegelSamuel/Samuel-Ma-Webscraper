import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from CDocumentationCrawlers.items import Article

class RefSpider(CrawlSpider):
    name = 'ref'
    allowed_domains = ['en.cppreference.com']
    start_urls = ['https://en.cppreference.com/w/c/language/basic_concepts']

    rules = [
        Rule(LinkExtractor(allow=r'w/c/language/(.)*$'), callback='parse', follow=True)
        # If you're wondering about the ReGeX, it means allow anything past wiki/ but without any ?, !, or :
        # Anything = .
    ]

    def parse(self, response):
        article = Article() # make a new Article object
        article['title'] = response.xpath('//span[@class="color_h1"]/text()').get()
        article['url'] = response.url
        return article