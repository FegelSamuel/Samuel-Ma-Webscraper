import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Article_Scraper.items import Article


class WikipediaSpider(CrawlSpider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Kevin_Bacon']

    rules = [
        Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse', follow=True)
        # If you're wondering about the ReGeX, it means allow anything past wiki/ but without any ?, !, or :
        # Anything = *
    ]



    def parse(self, response):
        article = Article()



        article['title'] = response.xpath('//span[@class="mw-page-title-main"]/text()').get() or response.xpath('//h1/i/text()')
        article['url'] = response.url
        article['last_updated'] = response.xpath('//li[@id="footer-info-lastmod"]/text()').get()

        return article
        