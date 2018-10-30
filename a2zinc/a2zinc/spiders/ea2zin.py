# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class Ea2zinSpider(scrapy.Spider):
    name = 'ea2zin'
    allowed_domains = ['cedia.a2zinc.net']
    start_urls = ['https://cedia.a2zinc.net/CEDIA2018/Public/exhibitors.aspx?Index=All#']

    def parse(self, response):
        # links - extracting urls to get company details
        links = response.xpath('//*[@class="exhibitorName"]/@href').extract()
        for link in links:
            url = 'https://cedia.a2zinc.net/CEDIA2018/Public/' + link
            src = url
            yield Request(src, callback=self.parse_comp,
                          meta={'src': src})

    def parse_comp(self, response):
        # xpaths to extract details of a company_details
        company_name = response.xpath('//*[@class="panel-body"]/h1/text()').extract_first()
        city = response.xpath('//*[@class="BoothContactCity"]/text()').extract_first()
        country = response.xpath('//*[@class="BoothContactCountry"]/text()').extract_first()
        src = response.meta.get('src')
        state = response.xpath('//*[@class="BoothContactState"]/text()').extract_first()
        facebook = response.xpath('//a[contains(@href,"facebook")]/@href').extract_first()
        linkedin = response.xpath('//a[contains(@href,"linkedin")]/@href').extract_first()
        domain = response.xpath('//*[@class="BoothContactUrl"]/a/text()').extract_first()
        email = response.xpath('//p/span/a/@href').extract_first()
        twitter = response.xpath('//a[contains(@href,"twitter")]/@href').extract_first()
        instagram = response.xpath('//a[contains(@href,"instagram")]/@href').extract_first()
        pinterest = response.xpath('//a[contains(@href,"pinterest")]/@href').extract_first()
        googleplus = response.xpath('//a[contains(@href,"googleplus")]/@href').extract_first()

        # use of yield keyword to return data
        yield {'company_name': company_name, 'address1': None, 'address2': None, 'city': city, 'state': state,
               'country': country, 'zipcode': None, 'domain': domain, 'src': src,
               'facebook': facebook, 'twitter': twitter, 'linkedin': linkedin, 'googleplus': googleplus,
               'instagram': instagram,
               'pinterest': pinterest, 'phone_no': None, 'fax_no': None, 'email': email}
