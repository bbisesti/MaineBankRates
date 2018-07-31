# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:54:54 2018

@author: Brett
"""

import scrapy

import logging


# Helpful for going through HTML tables
# https://www.simplified.guide/scrapy/scrape-table

class AndroscogginRatesSpider(scrapy.Spider):
    
    # Name of spider
    name = 'AndroscogginRates'
    
    # 
    start_urls = [
            'https://www.androscogginbank.com/Home/Rate-Center',
            'https://www.androscogginbank.com/Home/Rate-Center/Deposit-Rates'
            ]
            
    def parse(self, response):
        
        if response.request.url == 'https://www.androscogginbank.com/Home/Rate-Center':
            for row in response.xpath('//*[@class="persrates"]//tbody//tr'):
                yield {
                        'Account Type': row.xpath('normalize-space(td[1]//p//text())').extract_first().rstrip('*'),
                        'Minimum Balance': row.xpath('normalize-space(td[2]//p//text())').extract_first().rstrip('*'),
                        'Interest Rate': row.xpath('normalize-space(td[3]//p//text())').extract_first().rstrip('%'),
                        'Annual Percentage Yield': row.xpath('normalize-space(td[4]//p//text())').extract_first().rstrip('%')
                        }
        if response.request.url == 'https://www.androscogginbank.com/Home/Rate-Center/Deposit-Rates':
            count = 0
            for row in response.xpath('//*[@class="persrates"]//tbody//tr'):
                newAccountType = ''
                if count == 0:
                    AccountType = row.xpath('normalize-space(td[1]//p//text())').extract_first().rstrip('*')
                else:
                    newAccountType = row.xpath('normalize-space(td[1]//p//text())').extract_first().rstrip('*')
                    if len(newAccountType) > 0:
                        AccountType = newAccountType

                                        
                count = count + 1
                logging.info(count)
                yield {
                        'Account Type': AccountType,
                        'Minimum Balance': row.xpath('normalize-space(td[2]//p//text())').extract_first().rstrip('*'),
                        'Interest Rate': row.xpath('normalize-space(td[3]//p//text())').extract_first().rstrip('%'),
                        'Annual Percentage Yield': row.xpath('normalize-space(td[4]//p//text())').extract_first().rstrip('%')
                        }