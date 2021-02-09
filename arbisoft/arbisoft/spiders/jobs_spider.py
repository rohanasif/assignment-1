import scrapy
import datetime
from ..items import JobItem

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    start_urls = [
        'https://news.ycombinator.com/jobs'
    ]

    def parse(self, response):

        items = response.css("tr.athing, td.subtext")
        job_titles = []
        company_urls = []
        job_urls = []
        job_posting_dates = []
        for item in items:

            job_title = item.css("td.title a.storylink::text").get()
            company_url = item.css("td.title span.sitebit.comhead a span.sitestr::text").get()
            job_url = item.css("td.title a.storylink ::attr(href)").get()
            job_posting_date = item.css("span.age a::text").get()

            if job_title:
                if 'hiring ' in job_title:
                    job_title = job_title.split("hiring ")[1]
                    if job_title.startswith('– '):
                        job_title = job_title.replace('– ', '')
                elif 'Hiring ' in job_title:
                    job_title = job_title.split("Hiring ")[1]
                    if job_title.startswith('– '):
                        job_title = job_title.replace('– ', '')
                job_titles.append(job_title)
                company_urls.append(company_url or '')

            if job_url:
                ycombinatorlink = 'https://news.ycombinator.com/'
                if 'http' not in job_url:
                    job_url = ycombinatorlink + job_url
                job_urls.append(job_url)

            if job_posting_date:
                if 'days' in job_posting_date or 'day' in job_posting_date:
                    job_posting_dates.append(str(datetime.date.today() -
                                                     datetime.timedelta(days=int(job_posting_date[:2]))))
                else:
                    full_date = datetime.datetime.now() - datetime.timedelta(hours=int(job_posting_date[:2]))
                    simple_date = full_date.date()
                    job_posting_dates.append(str(simple_date))

        jobs_zip_object = zip(job_titles, company_urls, job_urls, job_posting_dates)
        jobs_list = list(jobs_zip_object)
        yield JobItem(job = jobs_list)
