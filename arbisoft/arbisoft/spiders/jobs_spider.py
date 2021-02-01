import scrapy

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    start_urls = [
        'https://news.ycombinator.com/jobs'
    ]

    def parse(self, response):
        # syntax : response.css(".storylink::text")[i].extract().lower().split("hiring")[1] for job titles
        # syntax : response.css(".sitestr::text").extract() for company site
        # syntax : response.css(".title a::attr(href)").extract() even indices for job sites
        # syntax : response.css(".age a::text").extract() for time posted