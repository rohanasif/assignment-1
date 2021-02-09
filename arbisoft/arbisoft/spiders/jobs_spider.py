import scrapy
import datetime

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    start_urls = [
        'https://news.ycombinator.com/jobs'
    ]

    def parse(self, response):

        items = response.css("tr.athing, td.subtext")
        all_job_titles = []
        all_company_urls = []
        all_job_urls = []
        all_job_posting_dates = []
        for item in items:

            job_title = item.css("td.title a.storylink::text").get()
            company_url = item.css("td.title span.sitebit.comhead a span.sitestr::text").get()
            job_url = item.css("td.title a.storylink ::attr(href)").get()
            job_posting_date = item.css("span.age a::text").get()

            if job_title is not None:
                if 'hiring ' in job_title:
                    job_title = job_title.split("hiring ")[1]
                    if job_title.startswith('– '):
                        job_title = job_title.replace('– ', '')
                elif 'Hiring ' in job_title:
                    job_title = job_title.split("Hiring ")[1]
                    if job_title.startswith('– '):
                        job_title = job_title.replace('– ', '')
                all_job_titles.append(job_title)
                all_company_urls.append(company_url or '')

            if job_url is not None:
                ycombinatorlink = 'https://news.ycombinator.com/'
                if 'http' not in job_url:
                    job_url = ycombinatorlink + job_url
                all_job_urls.append(job_url)

            if job_posting_date is not None:
                if 'days' in job_posting_date or 'day' in job_posting_date:
                    all_job_posting_dates.append(str(datetime.date.today() -
                                                     datetime.timedelta(days=int(job_posting_date[:2]))))
                else:
                    full_date = datetime.datetime.now() - datetime.timedelta(hours=int(job_posting_date[:2]))
                    simple_date = full_date.date()
                    all_job_posting_dates.append(str(simple_date))

        all_jobs_zip_object = zip(all_job_titles, all_company_urls, all_job_urls, all_job_posting_dates)
        all_jobs_list = list(all_jobs_zip_object)
        print(all_jobs_list)
        print(len(all_jobs_list))
