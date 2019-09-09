import scrapy


class spider3(scrapy.Spider):
    name = "spider3"
    start_urls = [
        'https://community.myfitnesspal.com/en/discussion/10759456/i-m-stumped-at-145lbs-please-help',
    ]

    def parse(self, response):
        # Extracting the content using css and xpath selectors
        author = response.css('.Username::text').extract()
#        title = response.css('title::text').extract()
#        thread_author = response.xpath("//*[@class='Username']/text()").extract_first()
#        thread_body = response.xpath('//div[@class="Discussion"]//div[@class="Message"]/text()').extract()
        time = response.xpath(
            '//span[@class="BodyDate DateCreated"]/a[@class="Permalink"]/text()').extract()
        post_body = response.xpath('//div[@class="Message"]').extract()

        # Give the extracted content row wise
        for item in zip(author, time, post_body):
            # Create a dictionary to store the scraped into
            scraped_info = {
                'author': item[0],
                'time': item[1],
                'post_body': item[2],
            }

            # Yield output
            yield scraped_info

        # Follow pagination link
        next_page_url = response.css(
            'a.Next.Pager-nav::attr(href)').extract_first()
        yield scrapy.Request(url=next_page_url, callback=self.parse)
