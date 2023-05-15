import scrapy


class QuotespiderSpider(scrapy.Spider):
    name = "quote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def start_requests(self):
        urls = [
            "http://quotes.toscrape.com/page/1",
            "http://quotes.toscrape.com/page/2"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.body.decode())
        self.log(f'Saved file {filename}')


