#!/usr/bin/env python3

# Created by Lucas Tilak
# Created:  11/11/15
# Modified: 11/11/15
# Testing Module for Database

import unittest
import MySQLdb
from testScrape import testScrape

class DBTestCase(unittest.TestCase):

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
		# Open database connection
		db = MySQLdb.connect(user="root", db="HappyApp")
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		cursor.execute( "SELECT DATABASE()")
		data = cursor.fetchone()
		self.assertEqual(str(data), "('happyapp',)", "Database should be named HappyApp")
		db.close

	def test_firstRest(self): 
		db = MySQLdb.connect(user="root", db="HappyApp")
		cursor = db.cursor()
		cursor.execute("SELECT restname FROM Restaurant;")
		results = cursor.fetchone()
		self.assertEqual(str(results), "('28th Street Tavern',)", "Restaurant query is incorrect")

	def test_tuesStime(self):
		db = MySQLdb.connect(user="root", db="HappyApp")
		cursor = db.cursor()
		cursor.execute("SELECT stime FROM Tuesday;")
		results = cursor.fetchone()
		print str(results)
		self.assertEqual(str(results), "(Decimal('16.0'),)", "Start Time test is incorrect" )

# Main: Run Test Cases
if __name__ == '__main__':
	unittest.main()
