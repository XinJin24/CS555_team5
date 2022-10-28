'''Sprint 3 User story test file'''

from contextlib import nullcontext
import unittest
from sprint3_userStories import *
import datetime


#dictionaries for testing

#dictionaries for testing user stories US21 and US23
familyDictionary211={}
individualDictionary211={}
familyDictionary211['F1'] = {'ID': 'F1', 'Marriage': '1981-01-8', 'Divorce': 'NA', 'Husband_ID': 'I21', 'Husband_Name': 'Harry /Potter/', 'Wife_ID': 'I3', 'Wife_Name': 'Ginny /Weasely/', 'Children': []}
individualDictionary211["I21"] = {'ID': 'I21', 'Name': 'Harry /Potter/', 'Gender': 'F', 'Birthday': '1982-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
individualDictionary211["I3"] = {'ID': 'I3', 'Name': 'Ginny /Weasely/', 'Gender': 'M', 'Birthday': '1982-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
familyDictionary212={}
individualDictionary212={}
familyDictionary212['F1'] = {'ID': 'F1', 'Marriage': '1981-01-8', 'Divorce': 'NA', 'Husband_ID': 'I21', 'Husband_Name': 'Harry /Potter/', 'Wife_ID': 'I3', 'Wife_Name': 'Ginny /Weasely/', 'Children': []}
individualDictionary212["I21"] = {'ID': 'I21', 'Name': 'Harry /Potter/', 'Gender': 'F', 'Birthday': '1982-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
individualDictionary212["I3"] = {'ID': 'I3', 'Name': 'Ginny /Weasely/', 'Gender': 'F', 'Birthday': '1982-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
familyDictionary213={}
individualDictionary213={}
familyDictionary213['F1'] = {'ID': 'F1', 'Marriage': '1981-01-8', 'Divorce': 'NA', 'Husband_ID': 'I21', 'Husband_Name': 'Harry /Potter/', 'Wife_ID': 'I3', 'Wife_Name': 'Ginny /Weasely/', 'Children': []}
individualDictionary213["I21"] = {'ID': 'I21', 'Name': 'Harry /Potter/', 'Gender': 'M', 'Birthday': '1982-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
individualDictionary213["I3"] = {'ID': 'I3', 'Name': 'Ginny /Weasely/', 'Gender': 'M', 'Birthday': '1982-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
familyDictionary214={}
individualDictionary214={}
familyDictionary214['F1'] = {'ID': 'F1', 'Marriage': '1981-01-8', 'Divorce': 'NA', 'Husband_ID': 'I21', 'Husband_Name': 'Harry /Potter/', 'Wife_ID': 'I3', 'Wife_Name': 'Ginny /Weasely/', 'Children': []}
individualDictionary214["I21"] = {'ID': 'I21', 'Name': 'Harry /Potter/', 'Gender': ' ', 'Birthday': '1982-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
individualDictionary214["I3"] = {'ID': 'I3', 'Name': 'Ginny /Weasely/', 'Gender': ' ', 'Birthday': '1982-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}


class userStories17to25Test(unittest.TestCase):
  
  #test US21, Correct gender for role
  
    def test_us21GenderRoles_1(self): #both husband and wife gender wrong
        result = us21GenderRoles(individualDictionary211, familyDictionary211)
        self.assertFalse(result)

    def test_us21GenderRoles_2(self): #husband gender wrong
        result = us21GenderRoles(individualDictionary212, familyDictionary212)
        self.assertFalse(result)

    def test_us21GenderRoles_3(self): #wife gender wrong
        result = us21GenderRoles(individualDictionary213, familyDictionary213)
        self.assertFalse(result)

    def test_us21GenderRoles_4(self): #No gender given
        result = us21GenderRoles(individualDictionary214, familyDictionary214)
        self.assertFalse(result)
    
if __name__ == '__main__':
  unittest.main()
