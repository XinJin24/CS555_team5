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
                                                    'Husband_ID': '', 'Husband_Name': 'dsds /sa/', 'Wife_ID': '',
                                                    'Wife_Name': '', 'Children': [1]}


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

    def test_maleLastName_5(self):
        result=maleLastName(individualDictionary, familyDictionary5)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
