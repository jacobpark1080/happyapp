#!/usr/bin/env python3

# Zack Allen
# Created:  11/11/15
# Modified: 11/11/15
# Testing Module for Scrape

import unittest
import testScrape

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
		self.assertEqual(scrapeDay, day, "Scrape Day is Incorrect")

	def test_firstRest(self):
		day
