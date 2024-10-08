import scrapy


class IetfSpider(scrapy.Spider):
    name = "ietf"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["https://www.pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
        author = response.xpath('//span[@class="author-name"]/text()').get()
        title = response.xpath('//span[@class="title"]/text()').get()
        date = response.xpath('//meta[@name="DC.Date.Issued"]/@content').get()
        return {
            "title": title,
            "author": author,
            "date": date
        }