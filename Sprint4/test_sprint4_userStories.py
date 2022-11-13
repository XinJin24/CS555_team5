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

# class to test user story 28
class test_list_siblings_decreasing_age(unittest.TestCase):

    def generate_Individual_Dictionary(self):
        individualDictionary = {}
        individualDictionary['I1'] = {'ID': 'I1', 'Name': 'Jack /Marks/', 'Gender': 'M', 'Birthday': '1922-06-6',
                                      'Age': 100, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F1']}

        individualDictionary['I2'] = {'ID': 'I2', 'Name': 'Helen /Fogler/', 'Gender': 'F', 'Birthday': '1926-03-6',
                                      'Age': 96, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F1']}

        individualDictionary['I3'] = {'ID': 'I3', 'Name': 'Don /Marks/', 'Gender': 'M', 'Birthday': '1949-08-15',
                                      'Age': 73, 'Alive': 'True', 'Death': 'NA', 'Child': 'F1', 'Spouse': []}

        individualDictionary['I4'] = {'ID': 'I4', 'Name': 'Chuck /Marks/', 'Gender': 'M', 'Birthday': '1951-05-4',
                                      'Age': 71, 'Alive': 'True', 'Death': 'NA', 'Child': 'F1', 'Spouse': []}

        individualDictionary['I5'] = {'ID': 'I5', 'Name': 'Jim /Marks/', 'Gender': 'M', 'Birthday': '1953-03-3',
                                      'Age': 69, 'Alive': 'True', 'Death': 'NA', 'Child': 'F1', 'Spouse': []}

        individualDictionary['I6'] = {'ID': 'I6', 'Name': 'Patricia /Marks/', 'Gender': 'F', 'Birthday': '1959-08-8',
                                      'Age': 63, 'Alive': 'True', 'Death': 'NA', 'Child': 'F1', 'Spouse': []}

        return individualDictionary

    def generate_Family_Dictionary(self):
        familyDictionary = {}

        familyDictionary['F1'] = {'ID': 'F1', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I1',
                                  'Husband_Name': 'Jack /Marks/', 'Wife_ID': 'I2', 'Wife_Name':
                                  'Helen /Fogler/', 'Children': ['I3', 'I4', 'I5', 'I6']}
        return familyDictionary

    # asserting equal - test case appropriately listed in descending order, expect to have output equal test case
    def test_list_siblings_decreasing_age1(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        self.assertEqual(list_siblings_decreasing_age(individualDictionary, familyDictionary), [['I3', 'I4', 'I5', 'I6']])

    # modified order of testing values - function will return in appropriate order, but test is not in order
    def test_list_siblings_decreasing_age2(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        self.assertNotEqual(list_siblings_decreasing_age(individualDictionary, familyDictionary), [['I3', 'I5', 'I4', 'I6']])

    # Updating dictionary for two people same age, but different DOB - testing assert equal
    def test_list_siblings_decreasing_age3(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        individualDictionary['I4']['Birthday'] = '1949-08-01'
        self.assertNotEqual(list_siblings_decreasing_age(individualDictionary, familyDictionary), [['I3', 'I4', 'I5', 'I6']])

    # siblings born on the same day
    def test_list_siblings_decreasing_age4(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        individualDictionary['I4']['Birthday'] = '1949-08-15'
        self.assertEqual(list_siblings_decreasing_age(individualDictionary, familyDictionary), [['I3', 'I4', 'I5', 'I6']])

    # siblings born on the same day
    def test_list_siblings_decreasing_age5(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        individualDictionary['I3']['Birthday'] = '1949-08-21'
        individualDictionary['I4']['Birthday'] = '1949-08-20'
        individualDictionary['I5']['Birthday'] = '1949-08-19'
        individualDictionary['I6']['Birthday'] = '1949-08-18'

        self.assertEqual(list_siblings_decreasing_age(individualDictionary, familyDictionary),
                         [['I6', 'I5', 'I4', 'I3']])

# class to test user story 29
class test_list_all_deceased_individuals(unittest.TestCase):

    def generate_Individual_Dictionary(self):
        individualDictionary = {}
        individualDictionary['I1'] = {'ID': 'I1', 'Name': 'Jack /Marks/', 'Gender': 'M', 'Birthday': '1922-06-6',
                                      'Age': 100, 'Alive': 'False', 'Death': '1999-05-09', 'Child': 'NA', 'Spouse': ['F1']}

        individualDictionary['I2'] = {'ID': 'I2', 'Name': 'Helen /Fogler/', 'Gender': 'F', 'Birthday': '1926-03-6',
                                      'Age': 96, 'Alive': 'False', 'Death': '1999-05-09', 'Child': 'NA', 'Spouse': ['F1']}

        individualDictionary['I3'] = {'ID': 'I3', 'Name': 'Don /Marks/', 'Gender': 'M', 'Birthday': '1949-08-15',
                                      'Age': 73, 'Alive': 'True', 'Death': 'NA', 'Child': 'F1', 'Spouse': []}

        individualDictionary['I4'] = {'ID': 'I4', 'Name': 'Chuck /Marks/', 'Gender': 'M', 'Birthday': '1951-05-4',
                                      'Age': 71, 'Alive': 'True', 'Death': 'NA', 'Child': 'F1', 'Spouse': []}

        individualDictionary['I5'] = {'ID': 'I5', 'Name': 'Jim /Marks/', 'Gender': 'M', 'Birthday': '1953-03-3',
                                      'Age': 69, 'Alive': 'True', 'Death': 'NA', 'Child': 'F1', 'Spouse': []}

        individualDictionary['I6'] = {'ID': 'I6', 'Name': 'Patricia /Marks/', 'Gender': 'F', 'Birthday': '1959-08-8',
                                      'Age': 63, 'Alive': 'False', 'Death': '1999-05-09', 'Child': 'F1', 'Spouse': []}

        return individualDictionary

    def generate_Family_Dictionary(self):
        familyDictionary = {}

        familyDictionary['F1'] = {'ID': 'F1', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I1',
                                  'Husband_Name': 'Jack /Marks/', 'Wife_ID': 'I2', 'Wife_Name':
                                  'Helen /Fogler/', 'Children': ['I3', 'I4', 'I5', 'I6']}
        return familyDictionary

    # asserting equal - test case appropriately listed in descending order, expect to have output equal test case
    def test_list_all_deceased_individuals1(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        testTuple = list_all_deceased_individuals(individualDictionary, familyDictionary)
        testList = []
        masterTestList = []
        for tuple in testTuple:
            testList.append(tuple[0])
        masterTestList.append(testList)
        self.assertEqual(masterTestList, [['I1', 'I2', 'I6']])

    def test_list_all_deceased_individuals2(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        individualDictionary['I1']['Alive'] = 'True'
        testTuple = list_all_deceased_individuals(individualDictionary, familyDictionary)
        testList = []
        masterTestList = []
        for tuple in testTuple:
            testList.append(tuple[0])
        masterTestList.append(testList)
        self.assertEqual(masterTestList, [['I2', 'I6']])

    def test_list_all_deceased_individuals3(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        individualDictionary['I1']['Alive'] = 'True'
        individualDictionary['I2']['Alive'] = 'True'

        testTuple = list_all_deceased_individuals(individualDictionary, familyDictionary)
        testList = []
        masterTestList = []
        for tuple in testTuple:
            testList.append(tuple[0])
        masterTestList.append(testList)
        self.assertEqual(masterTestList, [['I6']])


    def test_list_all_deceased_individuals4(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        individualDictionary['I1']['Alive'] = 'True'
        individualDictionary['I2']['Alive'] = 'True'
        individualDictionary['I6']['Alive'] = 'True'

        testTuple = list_all_deceased_individuals(individualDictionary, familyDictionary)
        testList = []
        masterTestList = []
        for tuple in testTuple:
            testList.append(tuple[0])
        masterTestList.append(testList)
        self.assertEqual(masterTestList, [[]])

    def test_list_all_deceased_individuals5(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        individualDictionary['I1']['Alive'] = 'True'
        individualDictionary['I1']['Alive'] = 'False'
        individualDictionary['I1']['Alive'] = 'True'

        testTuple = list_all_deceased_individuals(individualDictionary, familyDictionary)
        testList = []
        masterTestList = []
        for tuple in testTuple:
            testList.append(tuple[0])
        masterTestList.append(testList)
        self.assertEqual(masterTestList, [['I2', 'I6']])




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
