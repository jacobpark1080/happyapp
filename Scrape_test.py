#!/usr/bin/env python3

# Zack Allen
# Created:  11/11/15
# Modified: 11/11/15
# Testing Module for Scrape

import unittest
from testScrape import testScrape

class ScrapeTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		pass 

	@classmethod
	def tearDownClass(cls):
		pass

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_init(self):
		day = "monday"
		scrapeDay = testScrape(day)
		self.assertEqual(scrapeDay[0], day, "Scrape Day is Incorrect, should access Monday")

	def test_firstRest(self):
		day = "tuesday"
		scrapeDay = testScrape(day)
		self.assertEqual(scrapeDay[1], "Boulder Chophouse & Tavern", "First Restraunt from Tuesday is Incorrect")

	def test_lastRest(self):
		day = "wednesday"
		scrapeDay = testScrape(day)
		self.assertEqual(scrapeDay[2], "Zolo", "Last Restraunt from Wednesday is Incorrect")
	
	def test_firstTime(self):
		day = "thursday"
		scrapeDay = testScrape(day)
		self.assertEqual(scrapeDay[3], 16.0, "Start time for Thursday First Restaurant is Incorrect")
		self.assertEqual(scrapeDay[4], 18.0, "End time for Thursday First Restaurant is Incorrect")

	def test_lastTime(self):
                day = "friday"
                scrapeDay = testScrape(day)
                self.assertEqual(scrapeDay[5], 15.0, "Start time for Friday Last Restaurant is Incorrect")
                self.assertEqual(scrapeDay[6], 18.0, "End time for Friday Last Restaurant is Incorrect")

# Main: Run Test Cases
if __name__ == '__main__':
	unittest.main()
