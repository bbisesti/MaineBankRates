

# Database
import mysql.connector

# Logging
import logging

# Operating Systems
import os


class DatabaseConnection():
        
    def insertDepositRates(rates):
        db = mysql.connector.connect(user="mbr",passwd="Blah2018!",database="MaineBankRates")
        try:
            cur = db.cursor()
            rowsInserted = 0
            for rate in rates:
                cur.execute("insert into deposit_rates (`institution_id`,`type`,`min_balance`,`interest_rate`,`apr`) values (%(institution_id)s,%(type)s,%(minBalance)s,%(interestRate)s,%(apr)s);",dict(rate))
                db.commit()
                rowsInserted = cur.rowcount + rowsInserted
            logging.info(str(rowsInserted) + " rows inserted")
        except mysql.connector.Error as err:
            logging.error("Error with sql connection: {}".format(err))
        finally:
            cur.close()
