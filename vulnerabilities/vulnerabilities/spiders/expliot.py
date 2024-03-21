import scrapy


class ExpliotSpider(scrapy.Spider):
    name = "expliot"
    allowed_domains = ["cve.mitre.org"]
    start_urls = ["https://cve.mitre.org"]

    def parse(self, response):
        pass
