"""
Unit test.
"""

# Read env variables from a local .env file, to fake the variables normally provided by the cage container
import dotenv
dotenv.load_dotenv('.env')
import unittest
import logging
import process

class Test(unittest.TestCase):
    def test_data_quality_check(self):
        """
        Try the process to check data quality
        """
        test_event = {
            'type': 'CHECK_DATA_QUALITY'
        }

        process.event_processor(test_event)
    
    def test_common_customers_demo(self):
        """
        Try the process  without going through the redis queue
        """
        test_event = {
            'type': 'CHECK_COMMON_DEMO_CUSTOMERS'
        }
        
        process.event_processor(test_event)