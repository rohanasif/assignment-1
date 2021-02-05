import scrapy
import datetime

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    start_urls = [
        'https://news.ycombinator.com/jobs'
    ]

    def parse(self, response):

        # Job Titles Code:
        job_titles = response.css(".storylink::text").getall()
        titles = []
        for item in job_titles:
            if 'hiring ' in item:
                item = item.split("hiring ")[1]
                if item.startswith('– '):
                    item = item.replace('– ', '')
            elif 'Hiring ' in item:
                item = item.split("Hiring ")[1]
                if item.startswith('– '):
                    item = item.replace('– ', '')
            titles.append(item)

        # Temporary list:
        full_jobs = response.css("tr.athing")
        main_site_list = []
        for item in full_jobs.getall():
            if "sitebit" in item:
                main_site_list.insert(full_jobs.getall().index(item), item)
            else:
                main_site_list.insert(full_jobs.getall().index(item), "")


        #print(len(full_jobs))
        #print(full_jobs)
        print(main_site_list)

        # Company Links Code:
        company_links = response.css(".sitestr::text").getall()

        # Job Links Code:
        job_links = response.css(".storylink ::attr(href)").getall()
        ycombinatorlink = 'https://news.ycombinator.com/'
        links = []
        for item in job_links:
            if 'http' not in item:
                item = ycombinatorlink + item
            links.append(item)

        # Time Ago Code:
        time_ago = response.css(".age a::text").getall()
        dates = []
        for item in time_ago:
            if 'days' in item or 'day' in item:
                dates.append(str(datetime.date.today()-datetime.timedelta(days=int(item[:2]))))
            else:
                full_date = datetime.datetime.now()-datetime.timedelta(hours=int(item[:2]))
                simple_date = full_date.date()
                dates.append(str(simple_date))


# job_titles = response.css(".storylink::text")[i].getall().lower().split("hiring")[1] # for job titles
# company_links = response.css(".sitestr::text").getall() # for company site (ycombinator links missing)
# job_links = response.css(".storylink ::attr(href)").getall() # for job sites (ycombinator jobs have id(RESOLVED))
# time_ago = response.css(".age a::text").getall()  # datetime.datetime.now()-datetime.timedelta(days_ago)) gives the
# posted date
