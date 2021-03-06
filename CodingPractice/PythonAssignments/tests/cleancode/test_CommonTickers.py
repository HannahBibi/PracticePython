import unittest
from CodingPractice.PythonAssignments.cleancode.StockExchangeUtils import common_tickers


class CommonTickersTests(unittest.TestCase):

    def test_00_common_tickers(self):
        NYSE = {'APPL', 'IBM', 'ORCL', 'AAC', 'AAD'}
        LON = {'APPL', 'IBM', 'LXE', 'AAC'}
        self.assertEqual({'APPL', 'IBM', 'AAC'}, common_tickers(NYSE, LON))

    def test_01_uncommon_tickers(self):
        NYSE = {'APP', 'IBB', 'ORCL', 'AAR', 'AAD'}
        LON = {'APPL', 'IBM', 'LXE', 'AAC'}
        self.assertEqual(set(), common_tickers(NYSE, LON))

    def test_02_first_is_empty_set(self):
        NYSE = set()
        LON = {'APPL', 'IBM', 'LXE', 'AAC'}
        self.assertEqual(set(), common_tickers(NYSE, LON))

    def test_03_second_is_empty_set(self):
        NYSE = {'APPL', 'IBM', 'ORCL', 'AAC', 'AAD'}
        LON = set()
        self.assertEqual(set(), common_tickers(NYSE, LON))

    def test_04_both_empty(self):
        NYSE = set()
        LON = set()
        self.assertEqual(set(), common_tickers(NYSE, LON))

    def test_05_both_equal(self):
        NYSE = {'APPL', 'IBM', 'ORCL', 'AAC', 'AAD'}
        LON = {'APPL', 'IBM', 'LXE', 'AAC'}
        self.assertEqual(common_tickers(LON, NYSE), common_tickers(NYSE, LON))


if __name__ == '__main__':
    unittest.main()
