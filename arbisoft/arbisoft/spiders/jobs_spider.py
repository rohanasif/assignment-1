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

        def generate_posting_dates(job_posting_date):
            if job_posting_date:
                if 'day' in job_posting_date:
                    job['job_posting_date'] = str(datetime.date.today() -
                                                  datetime.timedelta(days=int(job_posting_date[:2])))
                elif 'hour' in job_posting_date:
                    full_date = datetime.datetime.now() - datetime.timedelta(hours=int(job_posting_date[:2]))
                    simple_date = full_date.date()
                    job['job_posting_date'] = str(simple_date)
                elif 'minute' in job_posting_date:
                    full_date = datetime.datetime.now() - datetime.timedelta(minutes=int(job_posting_date[:2]))
                    simple_date = full_date.date()
                    job['job_posting_date'] = str(simple_date)
                elif 'second' in job_posting_date:
                    full_date = datetime.datetime.now() - datetime.timedelta(seconds=int(job_posting_date[:2]))
                    simple_date = full_date.date()
                    job['job_posting_date'] = str(simple_date)
            return job['job_posting_date']

        def generate_job_titles(job_title):
            if job_title:
                if 'hiring' in job_title or 'Hiring' in job_title:
                    if job_title.endswith('hiring') or job_title.endswith('Hiring'):
                        job['job_title'] = job_title
                    else:
                        pattern = re.compile(r'(?<=[hH]iring ).*')
                        matches = pattern.finditer(job_title)
                        for match in matches:
                            job['job_title'] = match[0]
                else:
                    job['job_title'] = job_title
            return job['job_title']

        def generate_company_urls(company_url):
            job['company_url'] = company_url or ''
            return job['company_url']

        def generate_job_urls(job_url):
            if job_url:
                if 'http' not in job_url:
                    job_url = ycombinatorlink + job_url
                job['job_url'] = job_url
            return job['job_url']

        for time, jobitem in items:
            job = JobItem()
            job_title = jobitem.css("a.storylink::text").get()
            company_url = jobitem.css("span.sitebit.comhead a span.sitestr::text").get()
            job_url = jobitem.css("a.storylink ::attr(href)").get()
            job_posting_date = time.css("a::text").get()
            if job_posting_date:
                if 'days' in job_posting_date and int(job_posting_date[:2]) > 5:
                    break
            generate_posting_dates(job_posting_date)
            generate_job_titles(job_title)
            generate_company_urls(company_url)
            generate_job_urls(job_url)
            yield job

        next_page = response.css("a.morelink::attr(href)").get()
        if next_page and job_posting_date:
            if 'days' in job_posting_date and int(job_posting_date[:2]) < 5:
                yield response.follow(next_page, callback=self.parse)
