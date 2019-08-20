import scrapy


class MFPSpider(scrapy.Spider):
    name = "mfp_spider"
    start_urls = [
        'https://community.myfitnesspal.com/en/discussion/comment/44055688#Comment_44055688',
    ]

    def parse(self, response):
        content = response.xpath("//*[@class='Message']").extract()
        yield{
            "Content": content
        }
