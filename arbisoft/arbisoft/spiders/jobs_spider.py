import scrapy

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    start_urls = [
        'https://news.ycombinator.com/jobs'
    ]

    def parse(self, response):
        # syntax : response.css("a.storylink::text")[i].extract().lower().split("hiring")[1] for job titles
        # syntax : response.css("span.sitestr::text").extract() for company site
        # syntax : response.css("").extract() for job site
