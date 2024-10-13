import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from CDocumentationCrawlers.items import Article


class G4gSpider(CrawlSpider):
    name = 'g4g'
    allowed_domains = ['geeksforgeeks.org']
    start_urls = ['https://www.geeksforgeeks.org/c-file-io/']

    rules = [
        Rule(LinkExtractor(allow=r'cpp.*'), callback='parse', follow=True) # LOOK HERE
    ]

    def parse(self, response):
        article = Article() # make a new Article object
        article['title'] = response.xpath('//div[@class="article-title"]/h1/text()').get()
        article['url'] = response.url
        yield article