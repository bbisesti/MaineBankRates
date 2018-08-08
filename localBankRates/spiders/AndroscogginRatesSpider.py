# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:54:54 2018

@author: Brett
"""

# Scrapy
import scrapy

# Logging
import logging

# Items
from localBankRates.items import DepositItem, LoanItem

# Database
from ..DatabaseConnection import DatabaseConnection as db


# Helpful for going through HTML tables
# https://www.simplified.guide/scrapy/scrape-table

class AndroscogginRatesSpider(scrapy.Spider):
        
    
    # Name of spider
    name = 'AndroscogginRates'
    
    # 
    start_urls = [
            'https://www.androscogginbank.com/Home/Rate-Center',
            'https://www.androscogginbank.com/Home/Rate-Center/Deposit-Rates'
            #'https://www.androscogginbank.com/Home/Rate-Center/Consumer-Loan-Rates'
            ]
            
    def parse(self, response):
        
        if response.request.url == 'https://www.androscogginbank.com/Home/Rate-Center':
            depositRates = []
            for row in response.xpath('//*[@class="persrates"]//tbody//tr'):
                if row.xpath('normalize-space(td[3]//p//text())').extract_first().rstrip('%') != '':
                    depositRate = DepositItem()
                    depositRate['institution_id'] = 1
                    depositRate['type'] = row.xpath('normalize-space(td[1]//p//text())').extract_first().rstrip('*')
                    depositRate['minBalance'] = row.xpath('normalize-space(td[2]//p//text())').extract_first().rstrip('*').lstrip('$')
                    depositRate['interestRate'] = row.xpath('normalize-space(td[3]//p//text())').extract_first().rstrip('%')
                    depositRate['apr'] = row.xpath('normalize-space(td[4]//p//text())').extract_first().rstrip('%')
                    depositRates.append(depositRate)
            db.insertDepositRates(depositRates)
           
                    
        if response.request.url == 'https://www.androscogginbank.com/Home/Rate-Center/Deposit-Rates':
            depositRates = []
            count = 0
            for row in response.xpath('//*[@class="persrates"]//tbody//tr'):
                if row.xpath('normalize-space(td[4]//p//text())').extract_first().rstrip('%') != '':
                    depositRate = DepositItem()
                    newAccountType = ''
                    if count == 0:
                        AccountType = row.xpath('normalize-space(td[1]//p//text())').extract_first().rstrip('*')
                    else:
                        newAccountType = row.xpath('normalize-space(td[1]//p//text())').extract_first().rstrip('*')
                        if len(newAccountType) > 0:
                            AccountType = newAccountType

                    count = count + 1
                    depositRate = DepositItem()
                    depositRate['institution_id'] = 1
                    depositRate['type'] = AccountType
                    depositRate['minBalance'] = row.xpath('normalize-space(td[3]//p//text())').extract_first().rstrip('%').rstrip('*')
                    depositRate['interestRate'] = row.xpath('normalize-space(td[4]//p//text())').extract_first().rstrip('%')
                    depositRate['apr'] = row.xpath('normalize-space(td[5]//p//text())').extract_first().rstrip('%')
                    depositRates.append(depositRate)
            db.insertDepositRates(depositRates)

        if response.request.url == 'https://www.androscogginbank.com/Home/Rate-Center/Consumer-Loan-Rates':
            count = 0
            for table in response.xpath('//*[@class="persrates"]'):
                loanRate = LoanItem()
                consumerLoanType = table.xpath('normalize-space(//caption//text())').extract_first().rstrip('*')
                count = 0
                for row in table.xpath('//tbody//tr'):
                    newAgeType: ''
                    if count == 0:
                        AgeType = row.xpath('normalize-space(td[1]//p//text())').extract_first().rstrip('*')
                    else:
                        newAgeType = row.xpath('normalize-space(td[1]//p//text())').extract_first().rstrip('*')
                        if len(newAgeType) > 0:
                            AgeType = newAgeType
                    
                    count = count + 1
                    if "rowspan" not in row.xpath('normalize-space(td[1])'):
                        loanRate['type'] = consumerLoanType
                        loanRate['age'] = AgeType
                        loanRate['term'] = row.xpath('normalize-space(td[3]//p//text())').extract_first().rstrip('*')
                        loanRate['rate'] = row.xpath('normalize-space(td[4]//p//text())').extract_first().rstrip('%')
                        loanRate['apr'] = row.xpath('normalize-space(td[5]//p//text())').extract_first().rstrip('%')
                        yield loanRate
                    else:
                        loanRate['type'] = consumerLoanType
                        loanRate['age'] = AgeType
                        loanRate['term'] = row.xpath('normalize-space(td[2]//p//text())').extract_first().rstrip('*')
                        loanRate['rate'] = row.xpath('normalize-space(td[3]//p//text())').extract_first().rstrip('%')
                        loanRate['apr'] = row.xpath('normalize-space(td[4]//p//text())').extract_first().rstrip('%')
                        yield loanRate