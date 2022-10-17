from contextlib import nullcontext
import unittest
from sprint2_userStories import *
import datetime

individualDictionary = {}
familyDictionary = {}

# manually create two dictionaries for US09 and US10
individualDictionary["I13"] = {'ID': 'I13', 'Name': 'Jack /Marks/', 'Gender': 'M', 'Birthday': '1922-09-21', 'Age': 100, 'Alive': 'False', 'Death': '2004-05-9', 'Child': 'NA', 'Spouse': ['F3', 'F6']}
individualDictionary["I28"] = {'ID': 'I28', 'Name': 'Ella /Pavlishchev/', 'Gender': 'F', 'Birthday': '1930-07-29', 'Age': 92, 'Alive': 'False', 'Death': '2019-05-14', 'Child': 'NA', 'Spouse': ['F6']}
individualDictionary['I29'] = {'ID': 'I29', 'Name': 'Ivan /Marks/', 'Gender': 'M', 'Birthday': '1966-11-16', 'Age': 55, 'Alive': 'True', 'Death': 'NA', 'Child': 'F6', 'Spouse': []}

familyDictionary['F6'] = {'ID': 'F6', 'Marriage': '1963-10-9', 'Divorce': 'NA', 'Husband_ID': 'I13', 'Husband_Name': 'Jack /Marks/', 'Wife_ID': 'I28', 'Wife_Name': 'Ella /Pavlishchev/', 'Children': ['I29']}

# manually create two dictionaries for US15 and US16
individualDictionary[0] = {'ID': 0, 'Name': 'dsdsds /jin/', 'Gender': 'F',
                                                            'Birthday': '', 'Age': 'NA', 'Alive': 'True', 'Death': 'NA',
                                                            'Child' : 'NA', 'Spouse': 'NA'}
individualDictionary[1] = {'ID': 1, 'Name': 'vv /aa/', 'Gender': 'M',
                                                            'Birthday': '', 'Age': 'NA', 'Alive': 'True', 'Death': 'NA',
                                                            'Child' : 'NA', 'Spouse': 'NA'}
individualDictionary[2] = {'ID': 2, 'Name': 'av /jin/', 'Gender': 'M',
                                                            'Birthday': '', 'Age': 'NA', 'Alive': 'True', 'Death': 'NA',
                                                            'Child' : 'NA', 'Spouse': 'NA'}
individualDictionary[3] = {'ID': 3, 'Name': 'sdasds /sas/', 'Gender': 'F',
                                                            'Birthday': '', 'Age': 'NA', 'Alive': 'True', 'Death': 'NA',
                                                            'Child' : 'NA', 'Spouse': 'NA'}  
individualDictionary[4] = {'ID': 4, 'Name': 'dsdsw213 /sdaa/', 'Gender': '',
                                                            'Birthday': 'M', 'Age': 'NA', 'Alive': 'True', 'Death': 'NA',
                                                            'Child' : 'NA', 'Spouse': 'NA'}
individualDictionary[5] = {'ID': 5, 'Name': 'dsdsw213 jin', 'Gender': '',
                                                            'Birthday': 'M', 'Age': 'NA', 'Alive': 'True', 'Death': 'NA',
                                                            'Child' : 'NA', 'Spouse': 'NA'}

familyDictionary1={}
familyDictionary1[0]={'ID': 0, 'Marriage': '', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': 'a /jin/', 'Wife_ID': '',
                                                    'Wife_Name': '', 'Children': [1,2]}
familyDictionary2={}
familyDictionary2[0]={'ID': 1, 'Marriage': '', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': 'dsgxz /jin/', 'Wife_ID': '',
                                                    'Wife_Name': '', 'Children': []}
familyDictionary3={}
familyDictionary3[0]={'ID': 2, 'Marriage': '', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': 'dsdsd /dsd/', 'Wife_ID': '',
                                                    'Wife_Name': '', 'Children': [0]}
familyDictionary4={}
familyDictionary4[0]={'ID': 3, 'Marriage': '', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': 'sasas /jin/', 'Wife_ID': '',
                                                    'Wife_Name': '', 'Children': [1,2,3,4]}
familyDictionary5={}
familyDictionary5[0]={'ID': 4, 'Marriage': '', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': 'dsds jin', 'Wife_ID': '',
                                                    'Wife_Name': '', 'Children': [5]}

familyDictionary6={}
familyDictionary6[0]={'ID': 4, 'Marriage': '', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': 'dsds /jin/', 'Wife_ID': '',
                                                    'Wife_Name': '', 'Children': [5]}

familyDictionary7={}
familyDictionary7[0]={'ID': 4, 'Marriage': '', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': 'dsds /jin/', 'Wife_ID': '',
                                                    'Wife_Name': '', 'Children': [2]}
class userStories9toTest(unittest.TestCase):
    #test US09, Birth before death of parents
    def test_birthBeforeDeathOfParents_1(self):
        result=birthBeforeDeathOfParents(individualDictionary, familyDictionary)
        self.assertTrue(result)

    def test_birthBeforeDeathOfParents_2(self):
        individualDictionary["I29"]['Birthday'] = '2004-05-9'
        result=birthBeforeDeathOfParents(individualDictionary, familyDictionary)
        self.assertTrue(result)

    def test_birthBeforeDeathOfParents_3(self):
        individualDictionary["I29"]['Birthday'] = '2019-03-11'
        result=birthBeforeDeathOfParents(individualDictionary, familyDictionary)
        self.assertFalse(result)

    def test_birthBeforeDeathOfParents_4(self):
        individualDictionary["I29"]['Birthday'] = '2019-05-15'
        result=birthBeforeDeathOfParents(individualDictionary, familyDictionary)
        self.assertFalse(result)

    def test_birthBeforeDeathOfParents_5(self):
        individualDictionary["I29"]['Birthday'] = '2004-08-15'
        result=birthBeforeDeathOfParents(individualDictionary, familyDictionary)
        self.assertTrue(result)

    #test US10, Marriage after 14
    def test_marriageAfter14_1(self):
        result=marriageAfter14(individualDictionary, familyDictionary)
        self.assertTrue(result)

    def test_marriageAfter14_2(self):
        familyDictionary["F6"]['Marriage'] = '1922-09-21'
        result=marriageAfter14(individualDictionary, familyDictionary)
        self.assertFalse(result)

    def test_marriageAfter14_3(self):
        familyDictionary["F6"]['Marriage'] = '1930-07-29'
        result=marriageAfter14(individualDictionary, familyDictionary)
        self.assertFalse(result)

    def test_marriageAfter14_4(self):
        familyDictionary["F6"]['Marriage'] = '1940-07-29'
        result=marriageAfter14(individualDictionary, familyDictionary)
        self.assertFalse(result)

    def test_marriageAfter14_5(self):
        familyDictionary["F6"]['Marriage'] = '1950-07-29'
        result=marriageAfter14(individualDictionary, familyDictionary)
        self.assertTrue(result)

    #test US15, There should be fewer than 15 siblings in a family
    def test_fewerThan15Siblings_1(self):
        result=fewerThan15Siblings(individualDictionary, familyDictionary1)
        self.assertTrue(result)

    def test_fewerThan15Siblings_2(self):
        result=fewerThan15Siblings(individualDictionary, familyDictionary2)
        self.assertTrue(result)

    def test_fewerThan15Siblings_3(self):
        result=fewerThan15Siblings(individualDictionary, familyDictionary3)
        self.assertTrue(result)

    def test_fewerThan15Siblings_4(self):
        result=fewerThan15Siblings(individualDictionary, familyDictionary4)
        self.assertTrue(result)

    def test_fewerThan15Siblings_5(self):
        result=fewerThan15Siblings(individualDictionary, familyDictionary5)
        self.assertTrue(result)

    #test US16, All male members of a family should have the same last name
    def test_maleLastName_1(self):
        result=maleLastName(individualDictionary, familyDictionary1)
        self.assertFalse(result)

    def test_maleLastName_2(self):
        result=maleLastName(individualDictionary, familyDictionary2)
        self.assertTrue(result)

    def test_maleLastName_3(self):
        result=maleLastName(individualDictionary, familyDictionary3)
        self.assertTrue(result)

    def test_maleLastName_4(self):
        result=maleLastName(individualDictionary, familyDictionary4)
        self.assertFalse(result)

    # dad's lastname and children' name are not surrounding by // 
    def test_maleLastName_5(self):
        result=maleLastName(individualDictionary, familyDictionary5)
        self.assertTrue(result)

    # dad's lastname is surrounding by //, but children' name is not surrounding by // 
    def test_maleLastName_6(self):
        result=maleLastName(individualDictionary, familyDictionary6)
        self.assertTrue(result)

    # dad's lastname is not surrounding by //, children' name is surrounding by // 
    def test_maleLastName_7(self):
        result=maleLastName(individualDictionary, familyDictionary7)
        self.assertTrue(result)

# US 11 Testing class
class test_no_polygamy(unittest.TestCase):

    # Function used to generate individual dictionary for testing purposes
    def generate_Individual_Dictionary(self):
        individualDictionary_US12 = {}
        individualDictionary_US12['I1'] = {'ID': 'I1', 'Name': 'Joseph /Marks/', 'Gender': 'M', 'Birthday': '1985-05-4', 'Age': 37, 'Alive': 'True', 'Death': 'NA', 'Child': 'F1', 'Spouse': []}
        individualDictionary_US12['I2'] = {'ID': 'I2', 'Name': 'Donald /Marks/', 'Gender': 'M', 'Birthday': '1949-07-6', 'Age': 73, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F1', 'F2', 'F3']}
        individualDictionary_US12['I3'] = {'ID': 'I3', 'Name': 'Joyce /Earnhardt/', 'Gender': 'F', 'Birthday': '1951-03-6', 'Age': 71, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F1']}
        individualDictionary_US12['I4'] = {'ID': 'I4', 'Name': 'Kaitlyn /Schweibinz/', 'Gender': 'F', 'Birthday': '1965-06-5', 'Age': 57, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F2']}
        individualDictionary_US12['I5'] = {'ID': 'I4', 'Name': 'Leonie /Schmidt/', 'Gender': 'F', 'Birthday': '1976-08-15', 'Age': 46, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F3']}

        return individualDictionary_US12

    # Function used to generate family dictionary for testing purposes
    def generate_Family_Dictionary(self):
        familyDictionary_US12 = {}
        familyDictionary_US12['F1'] = {'ID': 'F1', 'Marriage': '1979-04-5', 'Divorce': '1989-07-8', 'Husband_ID': 'I2', 'Husband_Name': 'Donald /Marks/', 'Wife_ID': 'I3', 'Wife_Name': 'Joyce /Earnhardt/', 'Children': ['I1']}
        familyDictionary_US12['F2'] = {'ID': 'F2', 'Marriage': '1993-07-8', 'Divorce': '1999-07-8', 'Husband_ID': 'I2', 'Husband_Name': 'Donald /Marks/', 'Wife_ID': 'I4', 'Wife_Name': 'Kaitlyn /Schweibinz/', 'Children': []}
        familyDictionary_US12['F3'] = {'ID': 'F3', 'Marriage': '1999-12-8', 'Divorce': 'NA', 'Husband_ID': 'I2', 'Husband_Name': 'Donald /Marks/', 'Wife_ID': 'I5', 'Wife_Name': 'Leonie /Schmidt/', 'Children': []}

        return familyDictionary_US12

    # One marriage, however never divorced - should violate, and return false
    def test_no_polygamy_1(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        familyDictionary['F2']['Divorce'] = 'NA'
        self.assertFalse(noPolygamy(individualDictionary, familyDictionary))

    # One marraige, and now divorce occurrs before new marraige, should not violate, and return true
    def test_no_polygamy_2(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        familyDictionary['F1']['Divorce'] = '1991-07-8'
        self.assertTrue(noPolygamy(individualDictionary, familyDictionary))

    # One marraige, and now death occurs before new marriage, should not violate, and return true
    def test_no_polygamy_3(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        familyDictionary['F2']['Divorce'] = 'NA'
        self.assertFalse(noPolygamy(individualDictionary, familyDictionary))

    # Divorce occurs after new marriage, should violate, asserting false
    def test_no_polygamy_4(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        familyDictionary['F2']['Divorce'] = '2005-07-8'
        self.assertFalse(noPolygamy(individualDictionary, familyDictionary))

    # Marriage occurs much earlier than other marriages, should violate, asserting false
    def test_no_polygamy_5(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        familyDictionary['F3']['Marriage'] = '1945-07-8'
        self.assertFalse(noPolygamy(individualDictionary, familyDictionary))

# US 12 Testing class
class test_parents_not_too_old(unittest.TestCase):

    # Function used to generate individual dictionary for testing purposes
    def generate_Individual_Dictionary(self):
        individualDictionary_US12 = {}
        individualDictionary_US12['I1'] = {'ID': 'I1', 'Name': 'Joseph /Marks/', 'Gender': 'M', 'Birthday': '1985-05-13', 'Age': 37, 'Alive': 'True', 'Death': 'NA', 'Child': 'F1', 'Spouse': []}
        individualDictionary_US12['I2'] = {'ID': 'I2', 'Name': 'Donald /Marks/', 'Gender': 'M', 'Birthday': '1949-08-15', 'Age': 173, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F1']}
        individualDictionary_US12['I3'] = {'ID': 'I3', 'Name': 'Joyce /Earnhardt/', 'Gender': 'F', 'Birthday': '1951-10-24', 'Age': 170, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F1']}

        return individualDictionary_US12

    # Function used to generate family dictionary for testing purposes
    def generate_Family_Dictionary(self):
        familyDictionary_US12 = {}
        familyDictionary_US12['F1'] = {'ID': 'F1', 'Marriage': '1975-12-24', 'Divorce': 'NA', 'Husband_ID': 'I2', 'Husband_Name': 'Donald /Marks/', 'Wife_ID': 'I3', 'Wife_Name': 'Joyce /Earnhardt/', 'Children': ['I1']}

        return familyDictionary_US12

    # Dictionaries set up so parents well below old age threshold, asserting true, will return true
    def test_parents_not_too_old_1(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        self.assertTrue(parentsNotTooOld(individualDictionary, familyDictionary))

    # Make father very old, asserting false as threshold is exceeded
    def test_parents_not_too_old_2(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        individualDictionary['I2']['Birthday'] = '1849-08-15'
        self.assertFalse(parentsNotTooOld(individualDictionary, familyDictionary))

 # Make mother very old, asserting false as threshold is exceeded
    def test_parents_not_too_old_3(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        individualDictionary['I3']['Birthday'] = '1851-08-15'
        self.assertFalse(parentsNotTooOld(individualDictionary, familyDictionary))

# Make both parents older, asserting false as threshold is exceeded
    def test_parents_not_too_old_4(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        individualDictionary['I3']['Birthday'] = '1851-08-15'
        individualDictionary['I2']['Birthday'] = '1849-08-15'
        self.assertFalse(parentsNotTooOld(individualDictionary, familyDictionary))

# Make son older than parents, asserting false as threshold is exceeded
    def test_parents_not_too_old_5(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        individualDictionary['I1']['Birthday'] = '1832-08-15'
        self.assertFalse(parentsNotTooOld(individualDictionary, familyDictionary))

if __name__ == '__main__':
    unittest.main()
