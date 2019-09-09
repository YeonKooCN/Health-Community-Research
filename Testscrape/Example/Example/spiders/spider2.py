import scrapy

from Example.items import ExampleItem


class spider2(scrapy.Spider):
    name = "spider2"
    start_urls = [
        'https://community.myfitnesspal.com/en/discussion/10759456/i-m-stumped-at-145lbs-please-help',
    ]

    def parse(self, response):
        item = ExampleItem()
        item['title'] = response.css('title::text').extract()
        item['thread_author'] = response.xpath(
            "//*[@class='Username']/text()").extract_first()
        item['thread_body'] = response.xpath(
            '//div[@class="Discussion"]//div[@class="Message"]/text()').extract()
        item['posting_time'] = response.xpath(
            '//span[@class="BodyDate DateCreated"]/a[@class="Permalink"]/text()').extract_first()

        return item
