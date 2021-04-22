# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    # define the fields for your item here like:
    job_title = scrapy.Field()
    company_url = scrapy.Field()
    job_url = scrapy.Field()
    job_posting_date = scrapy.Field()
