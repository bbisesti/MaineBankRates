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


class NorwayRatesSpider(scrapy.Spider):
    
    # Name of Spider
    name = 'NorwayRates'
    
    # URLs to crawl
    start_urls = [
        'https://www.norwaysavings.bank/rates/'
    ]
    
    def parse(self, response):
        
        newAccount = ''
        AccountType = ''
        depositRates = []
        
        # Checking Account Rates
        for row in response.xpath('//table[@id="personal_checking_table"]//tr'):
            if row.xpath('normalize-space(td[3]//text())').extract_first().rstrip('%').rstrip('*') != '':
                depositRate = DepositItem()
                if newAccount != row.xpath('normalize-space(td[1]//text())').extract_first().rstrip('%').rstrip('*'):
                    AccountType = row.xpath('normalize-space(td[1]//text())').extract_first().rstrip('%').rstrip('*')

                depositRate['institution_id'] = 2
                depositRate['type'] = AccountType
                depositRate['minBalance'] = row.xpath('normalize-space(td[2]//text())').extract_first().rstrip('%').rstrip('*')
                depositRate['interestRate'] = row.xpath('normalize-space(td[4]//text())').extract_first().rstrip('%').rstrip('*')
                depositRate['apr'] = row.xpath('normalize-space(td[3]//text())').extract_first().rstrip('%').rstrip('*')
                depositRates.append(depositRate)
                
        # Savings Account Rates
        for row in response.xpath('//table[@id="saving_account_rates_table"]//tr'):
            if row.xpath('normalize-space(td[3]//text())').extract_first().rstrip('%').rstrip('*') != '':
                depositRate = DepositItem()
                if newAccount != row.xpath('normalize-space(td[1]//text())').extract_first().rstrip('%').rstrip('*'):
                    AccountType = row.xpath('normalize-space(td[1]//text())').extract_first().rstrip('%').rstrip('*')

                depositRate['institution_id'] = 2
                depositRate['type'] = AccountType
                depositRate['minBalance'] = row.xpath('normalize-space(td[2]//text())').extract_first().rstrip('%').rstrip('*')
                depositRate['interestRate'] = row.xpath('normalize-space(td[4]//text())').extract_first().rstrip('%').rstrip('*')
                depositRate['apr'] = row.xpath('normalize-space(td[3]//text())').extract_first().rstrip('%').rstrip('*')
                depositRates.append(depositRate)
                
        # Health Savings Account Rates
        for row in response.xpath('//table[@id="health_savings_account_rates_table"]//tr'):
            if row.xpath('normalize-space(td[3]//text())').extract_first().rstrip('%').rstrip('*') != '':
                depositRate = DepositItem()

                depositRate['institution_id'] = 2
                depositRate['type'] = 'Health Savings Account'
                depositRate['minBalance'] = row.xpath('normalize-space(td[1]//text())').extract_first().rstrip('%').rstrip('*')
                depositRate['interestRate'] = row.xpath('normalize-space(td[3]//text())').extract_first().rstrip('%').rstrip('*')
                depositRate['apr'] = row.xpath('normalize-space(td[2]//text())').extract_first().rstrip('%').rstrip('*')
                depositRates.append(depositRate)
                
        # CD and IRAs
        for row in response.xpath('//table[@id="cd_ira_rate_table"]//tr'):
            if row.xpath('normalize-space(td[5]//text())').extract_first().rstrip('%').rstrip('*') != '':
                depositRate = DepositItem()

                depositRate['institution_id'] = 2
                depositRate['type'] = row.xpath('normalize-space(td[2]//text())').extract_first().rstrip('%').rstrip('*')
                depositRate['minBalance'] = row.xpath('normalize-space(td[3]//text())').extract_first().rstrip('%').rstrip('*')
                depositRate['interestRate'] = row.xpath('normalize-space(td[5]//text())').extract_first().rstrip('%').rstrip('*')
                depositRate['apr'] = row.xpath('normalize-space(td[4]//text())').extract_first().rstrip('%').rstrip('*')
                depositRates.append(depositRate)
                
        # Business Savings Account Rates
        for row in response.xpath('//table[@id="saving_account_rates_table"]//tr'):
            if row.xpath('normalize-space(td[3]//text())').extract_first().rstrip('%').rstrip('*') != '':
                depositRate = DepositItem()
                if newAccount != row.xpath('normalize-space(td[1]//text())').extract_first().rstrip('%').rstrip('*'):
                    AccountType = row.xpath('normalize-space(td[1]//text())').extract_first().rstrip('%').rstrip('*')

                depositRate['institution_id'] = 2
                depositRate['type'] = AccountType
                depositRate['minBalance'] = row.xpath('normalize-space(td[2]//text())').extract_first().rstrip('%').rstrip('*')
                depositRate['interestRate'] = row.xpath('normalize-space(td[4]//text())').extract_first().rstrip('%').rstrip('*')
                depositRate['apr'] = row.xpath('normalize-space(td[3]//text())').extract_first().rstrip('%').rstrip('*')
                depositRates.append(depositRate)
                
        db.insertDepositRates(depositRates)