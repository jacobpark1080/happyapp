#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andy Sayler
# Summer 2014
# CSCI 3308
# Univerity of Colorado
# Text Processing Module

import unittest
import textproc

class TextprocTestCase(unittest.TestCase):

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
        text = "tesing123"
        p = textproc.Processor(text)
        self.assertEqual(p.text, text, "'text' does not match input")

    # Add Your Test Cases Here...
    def test_count(self):
	word = "four"
	p = textproc.Processor(word)
	self.assertEqual(p.count(), len(p), "Word length doesn't equal length")

    def test_countalpha(self):
	word = "A four 12 5 A b"
	p = textproc.Processor(word)
	self.assertEqual(p.count_alpha(), 7, "Count_Alpha Error")

    def test_countnumeric(self):
	word = "555 hello 555"
	p = textproc.Processor(word)
	self.assertEqual(p.count_numeric(), 6, "Count_Numeric Error")

    def test_countvowels(self):
	word = "aeiou hi tho"
	p = textproc.Processor(word)
	self.assertEqual(p.count_vowels(), 7, "Count_Vowels Error")

    def test_isphonenumber(self):
	num = "707-537-5595"
	p = textproc.Processor(num)
	self.assertEqual(p.is_phonenumber(), True, "IsPhoneNumber Error")



# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
