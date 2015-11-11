# -*- coding: utf-8 -*-

# Andy Sayler
# Summer 2014
# CSCI 3308
# University of Colorado
# Text Processing Module

"""
A simple module with various Text Processing Capabilities

"""

# Imports

import re

# Exceptions

class ScrapeError(Exception):
    """
    Base Class for Scrape Exceptions

    """

    def __init__(self, msg):
        """
        ScrapeError Constructor

        :param msg: error message
        :return: ScrapeError instance

        """

        super().__init__(msg)

# Public Classes

class Scrape:
    """
    Class for Processing Scrape Results

    """

    def __init__(self, text):
        """
        Scrape Constructor

        :param str text: Scrape to Analyze
        :return: Scrape instance

        """

        if type(text) is not str:
            raise TextProcError("Processors require strings")

        self.text = text

    def __len__(self):
        """
        Length of text

        :return: Length

        """
	
	

        return len(self.text)

    def count(self):
        """
        Count number of characters in text

        :return: Length

        """
	
        return len(self)

    def count_alpha(self):
        """
        Count number of alphabetic characters in text

        :return: Number of alphabetic characters

        """

        alpha = re.compile(r'[a-zA-Z]')
        return len(alpha.findall(self.text))

    def count_numeric(self):
        """
        Count number of numeric characters in text

        :return: Number of numeric characters

        """

        alpha = re.compile(r'[0-9]')
        return len(alpha.findall(self.text))

    def count_vowels(self):
        """
        Count number of vowels in text

        :return: Number of vowels

        """

        vowels = re.compile(r'[aeiou]', re.IGNORECASE)
        return len(vowels.findall(self.text))

    def is_phonenumber(self):
        """
        Check if text is a valid US phone number

        :return: True or False

        """

        phonenum = re.compile(r'^[0-9]{3}-1*[0-9]{3}-1*[0-9]{4}$')
        if phonenum.match(self.text) is None:
            return False
        else:
            return True
