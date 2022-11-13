import unittest
from sprint4_userStories import *

individualDictionary = {}
familyDictionary = {}

# manually create two dictionaries for US26 and US34
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

# manually create two dictionaries for US32 and US33
individualDictionary_32_1 = {}
familyDictionary_32_1 = {}
individualDictionary_32_1["I1"] = {'ID': 'I1', 'Name': 'Harry /Potter/', 'Gender': 'F', 'Birthday': '1983-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
individualDictionary_32_1["I2"] = {'ID': 'I2', 'Name': 'jack /Potter/', 'Gender': 'F', 'Birthday': '1983-11-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
individualDictionary_32_1["I3"] = {'ID': 'I3', 'Name': 'jelly /Potter/', 'Gender': 'F', 'Birthday': '1983-12-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
individualDictionary_32_1["I4"] = {'ID': 'I4', 'Name': 'jason /Potter/', 'Gender': 'F', 'Birthday': '1983-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
individualDictionary_32_1["I5"] = {'ID': 'I5', 'Name': 'luis /Potter/', 'Gender': 'F', 'Birthday': '1983-1-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}

individualDictionary_32_2 = {}
familyDictionary_32_2 = {}
individualDictionary_32_2["I6"] = {'ID': 'I6', 'Name': 'sam /Potter/', 'Gender': 'F', 'Birthday': '1983-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
individualDictionary_32_2["I7"] = {'ID': 'I7', 'Name': 'lly /Potter/', 'Gender': 'F', 'Birthday': '1983-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
individualDictionary_32_2["I8"] = {'ID': 'I8', 'Name': 'ben /Potter/', 'Gender': 'F', 'Birthday': '1983-4-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}


individualDictionary_32_3 = {}
familyDictionary_32_3 = {}
individualDictionary_32_3["I7"] = {'ID': 'I7', 'Name': 'lly /Potter/', 'Gender': 'F', 'Birthday': 'NA', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
individualDictionary_32_3["I8"] = {'ID': 'I8', 'Name': 'ben /Potter/', 'Gender': 'F', 'Birthday': 'NA', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}

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

class userStories32And33Test(unittest.TestCase):
     # test US32 List multiple births
     def test_listMultipleBirths_1(self):
         result = listMultipleBirths(individualDictionary_32_1, familyDictionary_32_1)
         self.assertFalse(result)

     def test_listMultipleBirths_2(self):
         result = listMultipleBirths(individualDictionary_32_2, familyDictionary_32_2)
         self.assertFalse(result)
    
     def test_listMultipleBirths_3(self):
         result = listMultipleBirths(individualDictionary_32_3, familyDictionary_32_3)
         self.assertTrue(result)

     # test US33 List orphans
     def test_listOrphans_1(self):
         result = listOrphans(individualDictionary, familyDictionary)
         self.assertFalse(result)

     def test_listOrphans_2(self):
         individualDictionary["I13"]['Birthday'] = '1965-09-21'
         result = listOrphans(individualDictionary, familyDictionary)
         self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
