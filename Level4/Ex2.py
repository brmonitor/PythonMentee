# Python Mentee - Level 4 - Exercises
# https://bairesdev.atlassian.net/servicedesk/customer/article/2101576225
# 2 - Create a unit testing to extensively test all possibilities of the function created in the regex exercise above.

from re import findall
import unittest


def low_seq(text):
    return findall('[a-z]_[a-z]', text)


class TestLowSeq(unittest.TestCase):

    def test1(self):
        self.assertEqual(low_seq('  a_ab_c  A-Ad_e  z_z y_w  '), ['a_a', 'b_c', 'd_e', 'z_z', 'y_w'], "Incorrect")

    def test2(self):
        self.assertEqual(low_seq('  a_ab_c  A-Ad_e   '),         ['a_a', 'b_c', 'd_e'              ], "Incorrect")

    def test3(self):
        self.assertEqual(low_seq(''),         [], "Incorrect")


if __name__ == '__main__':
    unittest.main()
