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



        items = response.css("tr.athing td.title, td.subtext")

        ycombinatorlink = 'https://news.ycombinator.com/'
        for item in items:
            job = JobItem()
            job_title = item.css("a.storylink::text").get()
            company_url = item.css("span.sitebit.comhead a span.sitestr::text").get()
            job_url = item.css("a.storylink ::attr(href)").get()
            job_posting_date = item.css("span.age a::text").get()
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
        # print(next_page)
        if next_page and job_posting_date:
            if 'days' in job_posting_date and int(job_posting_date[:2]) > 5:
                yield response.follow(next_page, callback=self.parse)
