import unittest
from sprint3_userStories import *

individualDictionary = {}
familyDictionary = {}

# manually create two dictionaries for US17 and US18
individualDictionary["I13"] = {'ID': 'I13', 'Name': 'Jack /Marks/', 'Gender': 'M', 'Birthday': '1922-09-21', 'Age': 100,
                               'Alive': 'False', 'Death': '2004-05-9', 'Child': 'NA', 'Spouse': ['F3', 'F6']}
individualDictionary["I28"] = {'ID': 'I28', 'Name': 'Ella /Pavlishchev/', 'Gender': 'F', 'Birthday': '1930-07-29', 'Age': 92,
                               'Alive': 'False', 'Death': '2019-05-14', 'Child': 'NA', 'Spouse': ['F6']}
individualDictionary['I29'] = {'ID': 'I29', 'Name': 'Ivan /Marks/', 'Gender': 'M', 'Birthday': '1966-11-16', 'Age': 55,
                               'Alive': 'True', 'Death': 'NA', 'Child': 'F6', 'Spouse': []}
individualDictionary['I99'] = {'ID': 'I99', 'Name': 'Anna /Marks/', 'Gender': 'F', 'Birthday': '1976-11-16', 'Age': 45,
                               'Alive': 'True', 'Death': 'NA', 'Child': 'F6', 'Spouse': ['F3']}

familyDictionary['F6'] = {'ID': 'F6', 'Marriage': '1963-10-9', 'Divorce': 'NA', 'Husband_ID': 'I13', 'Husband_Name': 'Jack /Marks/',
                          'Wife_ID': 'I28', 'Wife_Name': 'Ella /Pavlishchev/', 'Children': ['I29']}
familyDictionary['F3'] = {'ID': 'F3', 'Marriage': '1993-10-9', 'Divorce': 'NA', 'Husband_ID': 'I13', 'Husband_Name': 'Jack /Marks/',
                          'Wife_ID': 'I99', 'Wife_Name': 'Anna /Marks/', 'Children': []}

class userStories26And34Test(unittest.TestCase):
     # test US26 Corresponding entries
     def test_correspondingEntries_1(self):
         result = correspondingEntries(individualDictionary, familyDictionary)
         self.assertTrue(result)

     def test_correspondingEntries_2(self):
         individualDictionary["I13"]['Spouse'] = ['F66']
         result = correspondingEntries(individualDictionary, familyDictionary)
         self.assertFalse(result)

     # test US34 List large age differences
     def test_listLargeAgeDifferences_1(self):
         result = listLargeAgeDifferences(individualDictionary, familyDictionary)
         self.assertFalse(result)

     def test_listLargeAgeDifferences_2(self):
         individualDictionary["I13"]['Birthday'] = '1965-09-21'
         result = listLargeAgeDifferences(individualDictionary, familyDictionary)
         self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
