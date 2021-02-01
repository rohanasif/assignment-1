import scrapy

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    start_urls = [
        'https://news.ycombinator.com/jobs'
    ]

    def parse(self, response):
        # job_titles = response.css(".storylink::text")[i].extract().lower().split("hiring")[1] # for job titles
        # company_links = response.css(".sitestr::text").extract() # for company site (ycombinator links missing)
        # job_links = response.css(".storylink ::attr(href)").extract() # for job sites (ycombinator jobs have id)
        date_posted = response.css(".age a::text").extract()  # for date posted, datetime.datetime.now()-datetime.timedelta(days_ago))
        yield {"date_posted" : date_posted}d