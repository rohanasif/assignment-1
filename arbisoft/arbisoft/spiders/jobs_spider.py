import scrapy
import datetime
from ..items import JobItem
import re


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    start_urls = [
        'https://news.ycombinator.com/jobs'
    ]

    def parse(self, response):

        times = response.css("span.age")
        jobitems = response.css("tr.athing")
        items = zip(times, jobitems)
        ycombinatorlink = 'https://news.ycombinator.com/'
        for time, jobitem in items:
            job = JobItem()
            job_title = jobitem.css("a.storylink::text").get()
            company_url = jobitem.css("span.sitebit.comhead a span.sitestr::text").get()
            job_url = jobitem.css("a.storylink ::attr(href)").get()
            job_posting_date = time.css("a::text").get()
            if job_posting_date:
                if 'days' in job_posting_date and int(job_posting_date[:2]) > 5:
                    break
            if job_posting_date:
                if 'day' in job_posting_date:
                    job['job_posting_date'] = str(datetime.date.today() -
                                                 datetime.timedelta(days=int(job_posting_date[:2])))
                elif 'hour' in job_posting_date:
                    full_date = datetime.datetime.now() - datetime.timedelta(hours=int(job_posting_date[:2]))
                    simple_date = full_date.date()
                    job['job_posting_date'] = str(simple_date)

            if job_title:
                pattern = re.compile(r'(?<=[hH]iring ).*')
                matches = pattern.finditer(job_title)
                for match in matches:
                    job['job_title'] = match[0]

                job['company_url'] = company_url or ''

            if job_url:
                if 'http' not in job_url:
                    job_url = ycombinatorlink + job_url
                job['job_url'] = job_url
            yield job
        next_page = response.css("a.morelink::attr(href)").get()
        if next_page and job_posting_date:
            if 'days' in job_posting_date and int(job_posting_date[:2]) > 5:
                yield response.follow(next_page, callback=self.parse)
