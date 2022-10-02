import unittest

import Sprint1_Team5
from Sprint1_Team5 import birthBeforeDeath

'''
Author: Joseph Marks
CS555 - Agile Methods for Software Development
Stevens Institute of Technology
Purpose: Unit Tests for User Story # 3 - birth before death 
'''

class test_birth_before_death(unittest.TestCase):

    def test_birth_before_death1(self):
        for individual in Sprint1_Team5.individualDictionary:
            self.assertTrue(birthBeforeDeath(individual), True)


if __name__ == '__main__':
    unittest.main()

