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
familyDictionary231={}
individualDictionary231={}
individualDictionary231["I23"] = {'ID': 'I23', 'Name': 'Harry /Potter/', 'Gender': 'M', 'Birthday': '1982-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
individualDictionary231["I3"] = {'ID': 'I3', 'Name': 'Harry /Potter/', 'Gender': 'M', 'Birthday': '1982-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
individualDictionary232={}
individualDictionary232["I23"] = {'ID': 'I23', 'Name': 'Harry /Potter/', 'Gender': 'M', 'Birthday': '1982-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
individualDictionary232["I3"] = {'ID': 'I3', 'Name': 'Ginny /Potter/', 'Gender': 'F', 'Birthday': '1982-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
individualDictionary233={}
individualDictionary233["I23"] = {'ID': 'I23', 'Name': 'Harry /Potter/', 'Gender': 'M', 'Birthday': '1982-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}
individualDictionary233["I3"] = {'ID': 'I3', 'Name': 'Harry /Potter/', 'Gender': 'F', 'Birthday': '1983-10-05', 'Age': 22, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': 'NA'}


familyDictionary324_1={}
familyDictionary324_1['1']={'ID': '1', 'Marriage': '1962-04-7', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': '1', 'Wife_ID': '',
                                                    'Wife_Name': '11', 'Children': []}
familyDictionary324_1['2']={'ID': '2', 'Marriage': '1962-04-7', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': '2', 'Wife_ID': '',
                                                    'Wife_Name': '11', 'Children': []}    
familyDictionary324_2={}     
familyDictionary324_2['2']={'ID': '2', 'Marriage': '1962-04-7', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': '2', 'Wife_ID': '11',
                                                    'Wife_Name': '', 'Children': []}                                                            
familyDictionary324_2['3']={'ID': '3', 'Marriage': '1962-04-7', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': '2', 'Wife_ID': '',
                                                    'Wife_Name': '33', 'Children': []}
familyDictionary324_3={}    
familyDictionary324_3['3']={'ID': '3', 'Marriage': '1962-04-7', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': '2', 'Wife_ID': '',
                                                    'Wife_Name': '33', 'Children': []}                                                 
familyDictionary324_3['4']={'ID': '4', 'Marriage': '1962-04-7', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': '121', 'Wife_ID': '',
                                                    'Wife_Name': '21212', 'Children': []}   
familyDictionary324_4={} 
familyDictionary324_4['4']={'ID': '4', 'Marriage': '1962-04-7', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': '121', 'Wife_ID': '21212',
                                                    'Wife_Name': '', 'Children': []}                                                         
familyDictionary324_4['5']={'ID': '5', 'Marriage': '1962-04-8', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': '3dd32', 'Wife_ID': '',
                                                    'Wife_Name': 'dsdwedewewdw434', 'Children': []}
familyDictionary324_5={} 
familyDictionary324_5['5']={'ID': '5', 'Marriage': '1962-04-8', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': '3dd32', 'Wife_ID': '',
                                                    'Wife_Name': 'dsdsd', 'Children': []}

familyDictionary324_5['6']={'ID': '6', 'Marriage': '1962-04-1', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': '3dd32', 'Wife_ID': '',
                                                    'Wife_Name': 'dsdsd', 'Children': []}     


individualDictionary325_1={}
familyDictionary325_1={}
individualDictionary325_1['1'] = {'ID': '1', 'Name': '', 'Gender': '',
                                                      'Birthday': '', 'Age': '', 'Alive': 'True', 'Death': 'NA',
                                                      'Child': 'NA', 'Spouse': []}
familyDictionary325_1['1']={'ID': '1', 'Marriage': '', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': '', 'Wife_ID': '',
                                                    'Wife_Name': '', 'Children': []}                                                  

individualDictionary325_2={}
familyDictionary325_2={}
individualDictionary325_2['1'] = {'ID': '1', 'Name': 'abc', 'Gender': '',
                                                      'Birthday': '1962-04-1', 'Age': '', 'Alive': 'True', 'Death': 'NA',
                                                      'Child': 'NA', 'Spouse': []}
individualDictionary325_2['2'] = {'ID': '2', 'Name': 'abc', 'Gender': '',
                                                      'Birthday': '1962-04-2', 'Age': '', 'Alive': 'True', 'Death': 'NA',
                                                      'Child': 'NA', 'Spouse': []}                                                     
familyDictionary325_2['1']={'ID': '1', 'Marriage': '', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': '', 'Wife_ID': '',
                                                    'Wife_Name': '', 'Children': ['1','2']}  

individualDictionary325_3={}
familyDictionary325_3={}
individualDictionary325_3['1'] = {'ID': '1', 'Name': 'abcd', 'Gender': '',
                                                      'Birthday': '1962-04-1', 'Age': '', 'Alive': 'True', 'Death': 'NA',
                                                      'Child': 'NA', 'Spouse': []}
individualDictionary325_3['2'] = {'ID': '2', 'Name': 'abc', 'Gender': '',
                                                      'Birthday': '1962-04-1', 'Age': '', 'Alive': 'True', 'Death': 'NA',
                                                      'Child': 'NA', 'Spouse': []}                                                     
familyDictionary325_3['1']={'ID': '1', 'Marriage': '', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': '', 'Wife_ID': '',
                                                    'Wife_Name': '', 'Children': ['1','2']}     

individualDictionary325_4={}
familyDictionary325_4={}
individualDictionary325_4['1'] = {'ID': '1', 'Name': 'abcde', 'Gender': '',
                                                      'Birthday': '1962-04-2', 'Age': '', 'Alive': 'True', 'Death': 'NA',
                                                      'Child': 'NA', 'Spouse': []}
individualDictionary325_4['2'] = {'ID': '2', 'Name': 'abc', 'Gender': '',
                                                      'Birthday': '1962-04-1', 'Age': '', 'Alive': 'True', 'Death': 'NA',
                                                      'Child': 'NA', 'Spouse': []}                                                     
familyDictionary325_4['1']={'ID': '1', 'Marriage': '', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': '', 'Wife_ID': '',
                                                    'Wife_Name': '', 'Children': ['1','2']}     

individualDictionary325_5={}
familyDictionary325_5={}
individualDictionary325_5['1'] = {'ID': '1', 'Name': 'abc', 'Gender': '',
                                                      'Birthday': '1962-04-1', 'Age': '', 'Alive': 'True', 'Death': 'NA',
                                                      'Child': 'NA', 'Spouse': []}
individualDictionary325_5['2'] = {'ID': '2', 'Name': 'abc', 'Gender': '',
                                                      'Birthday': '1962-04-1', 'Age': '', 'Alive': 'True', 'Death': 'NA',
                                                      'Child': 'NA', 'Spouse': []}                                                     
familyDictionary325_5['1']={'ID': '1', 'Marriage': '', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': '', 'Wife_ID': '',
                                                    'Wife_Name': '', 'Children': ['1','2']}  

class userStories17And18Test(unittest.TestCase):
     #test US17, No marriages to descendants
     def test_noMarriagesToDescendants_1(self):
         result = noMarriagesToDescendants(individualDictionary, familyDictionary)
         self.assertFalse(result)

     def test_noMarriagesToDescendants_2(self):
         individualDictionary['I99']['Spouse'] = []
         individualDictionary["I13"]['Spouse'] = ['F6']
         result = noMarriagesToDescendants(individualDictionary, familyDictionary)
         self.assertTrue(result)

     # test US18, Siblings should not marry
     def test_siblingsShouldNotMarry_3(self):
         result = siblingsShouldNotMarry(individualDictionary, familyDictionary)
         self.assertTrue(result)

     def test_siblingsShouldNotMarry_4(self):
         individualDictionary['I29']['Spouse'] = ['F3']
         individualDictionary['I99']['Spouse'] = ['F3']
         familyDictionary['F3'] = {'ID': 'F3', 'Marriage': '1993-10-9', 'Divorce': 'NA', 'Husband_ID': 'I29', 'Husband_Name': 'Ivan /Marks/',
                           'Wife_ID': 'I99', 'Wife_Name': 'Anna /Marks/', 'Children': []}
         result = siblingsShouldNotMarry(individualDictionary, familyDictionary)
         self.assertFalse(result)
        
class test_us19_no_marriage_to_first_cousin(unittest.TestCase):

    def generate_Individual_Dictionary(self):
        individualDictionary = {}
        individualDictionary['I1'] = {'ID': 'I1', 'Name': 'Joseph /Marks/', 'Gender': 'M', 'Birthday': '1985-05-13', 'Age': 37, 'Alive': 'True', 'Death': 'NA', 'Child': 'F1', 'Spouse': []}
        individualDictionary['I2'] = {'ID': 'I2', 'Name': 'Joyce /Earnhart/', 'Gender': 'F', 'Birthday': '1951-10-7', 'Age': 71, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F1']}
        individualDictionary['I3'] = {'ID': 'I3', 'Name': 'Don /Marks/', 'Gender': 'M', 'Birthday': '1949-08-15', 'Age': 73, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F1']}
        individualDictionary['I4'] = {'ID': 'I4', 'Name': 'Jacob /Marks/', 'Gender': 'M', 'Birthday': '1982-05-10', 'Age': 40, 'Alive': 'True', 'Death': 'NA', 'Child': 'F1', 'Spouse': ['F2']}
        individualDictionary['I5'] = {'ID': 'I5', 'Name': 'Amanda /Jordan/', 'Gender': 'F', 'Birthday': '1981-03-5', 'Age': 41, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F2']}
        individualDictionary['I6'] = {'ID': 'I6', 'Name': 'Nikola /Marks/', 'Gender': 'F', 'Birthday': '1999-10-7', 'Age': 23, 'Alive': 'True', 'Death': 'NA', 'Child': 'F2', 'Spouse': []}
        individualDictionary['I7'] = {'ID': 'I7', 'Name': 'Anton /Marks/', 'Gender': 'M', 'Birthday': '1998-05-16', 'Age': 24, 'Alive': 'True', 'Death': 'NA', 'Child': 'F2', 'Spouse': []}

        return individualDictionary

    def generate_Family_Dictionary(self):
        familyDictionary = {}
        familyDictionary['F1'] = {'ID': 'F1', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I3', 'Husband_Name': 'Don /Marks/', 'Wife_ID': 'I2', 'Wife_Name': 'Joyce /Earnhart/', 'Children': ['I1', 'I4']}
        familyDictionary['F2'] = {'ID': 'F2', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I4', 'Husband_Name': 'Jacob /Marks/', 'Wife_ID': 'I5', 'Wife_Name': 'Amanda /Jordan/', 'Children': ['I6', 'I7']}

        return familyDictionary

    # Normal marriages, anticipate true to be returned
    def test_us19_no_marriage_to_first_cousin_1(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        self.assertTrue(us19_no_marriage_to_first_cousin(individualDictionary, familyDictionary))

    # Multiple marriages to cousins, returns false
    def test_us19_no_marriage_to_first_cousin_2(self):
        individualDictionary = {'I1': {'ID': 'I1', 'Name': 'Joseph /Marks/', 'Gender': 'M', 'Birthday': '1985-05-14', 'Age': 37, 'Alive': 'True', 'Death': 'NA', 'Child': 'F2', 'Spouse': ['F1']}, 'I2': {'ID': 'I2', 'Name': 'Donald /Marks/', 'Gender': 'M', 'Birthday': '1949-08-15', 'Age': 73, 'Alive': 'True', 'Death': 'NA', 'Child': 'F3', 'Spouse': ['F2']}, 'I3': {'ID': 'I3', 'Name': 'Joyce /Earnhardt/', 'Gender': 'F', 'Birthday': '1951-10-24', 'Age': 71, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F2']}, 'I4': {'ID': 'I4', 'Name': 'Jacob /Marks/', 'Gender': 'M', 'Birthday': '1982-02-22', 'Age': 40, 'Alive': 'True', 'Death': 'NA', 'Child': 'F2', 'Spouse': ['F4']}, 'I5': {'ID': 'I5', 'Name': 'Jack /Marks/', 'Gender': 'M', 'Birthday': '1915-06-5', 'Age': 107, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F3']}, 'I6': {'ID': 'I6', 'Name': 'Helen /Fogler/', 'Gender': 'F', 'Birthday': '1918-09-16', 'Age': 104, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F3']}, 'I7': {'ID': 'I7', 'Name': 'Patricia /Marks/', 'Gender': 'F', 'Birthday': '1955-07-12', 'Age': 67, 'Alive': 'True', 'Death': 'NA', 'Child': 'F3', 'Spouse': ['F5']}, 'I8': {'ID': 'I8', 'Name': 'Brad /Stewart/', 'Gender': 'M', 'Birthday': '1951-07-6', 'Age': 71, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F5']}, 'I9': {'ID': 'I9', 'Name': 'Mitchell /Stewart/', 'Gender': 'M', 'Birthday': '1988-08-10', 'Age': 34, 'Alive': 'True', 'Death': 'NA', 'Child': 'F5', 'Spouse': []}, 'I10': {'ID': 'I10', 'Name': 'Alyssa /Stewart/', 'Gender': 'F', 'Birthday': '1989-05-5', 'Age': 33, 'Alive': 'True', 'Death': 'NA', 'Child': 'F5', 'Spouse': ['F4']}, 'I11': {'ID': 'I11', 'Name': 'Nikola /Stewart/', 'Gender': 'F', 'Birthday': '1989-06-8', 'Age': 33, 'Alive': 'True', 'Death': 'NA', 'Child': 'F5', 'Spouse': ['F1']}}
        familyDictionary = {'F1': {'ID': 'F1', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I1', 'Husband_Name': 'Joseph /Marks/', 'Wife_ID': 'I11', 'Wife_Name': 'Nikola /Stewart/', 'Children': []}, 'F2': {'ID': 'F2', 'Marriage': '1949-08-15', 'Divorce': 'NA', 'Husband_ID': 'I2', 'Husband_Name': 'Donald /Marks/', 'Wife_ID': 'I3', 'Wife_Name': 'Joyce /Earnhardt/', 'Children': ['I1', 'I4']}, 'F3': {'ID': 'F3', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I5', 'Husband_Name': 'Jack /Marks/', 'Wife_ID': 'I6', 'Wife_Name': 'Helen /Fogler/', 'Children': ['I2', 'I7']}, 'F4': {'ID': 'F4', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I4', 'Husband_Name': 'Jacob /Marks/', 'Wife_ID': 'I10', 'Wife_Name': 'Alyssa /Stewart/', 'Children': []}, 'F5': {'ID': 'F5', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I8', 'Husband_Name': 'Brad /Stewart/', 'Wife_ID': 'I7', 'Wife_Name': 'Patricia /Marks/', 'Children': ['I9', 'I10', 'I11']}}
        self.assertFalse(us19_no_marriage_to_first_cousin(individualDictionary, familyDictionary))

    # Multiple marriages to multiple cousins, returns false
    def test_us19_no_marriage_to_first_cousin_3(self):
        individualDictionary = {'I1': {'ID': 'I1', 'Name': 'Joseph /Marks/', 'Gender': 'M', 'Birthday': '1985-05-14', 'Age': 37, 'Alive': 'True', 'Death': 'NA', 'Child': 'F3', 'Spouse': ['F1', 'F2']}, 'I2': {'ID': 'I2', 'Name': 'Donald /Marks/', 'Gender': 'M', 'Birthday': '1949-08-15', 'Age': 73, 'Alive': 'True', 'Death': 'NA', 'Child': 'F4', 'Spouse': ['F3']}, 'I3': {'ID': 'I3', 'Name': 'Joyce /Earnhardt/', 'Gender': 'F', 'Birthday': '1951-10-24', 'Age': 71, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F3']}, 'I4': {'ID': 'I4', 'Name': 'Jacob /Marks/', 'Gender': 'M', 'Birthday': '1982-02-22', 'Age': 40, 'Alive': 'True', 'Death': 'NA', 'Child': 'F3', 'Spouse': ['F5']}, 'I5': {'ID': 'I5', 'Name': 'Jack /Marks/', 'Gender': 'M', 'Birthday': '1915-06-5', 'Age': 107, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F4']}, 'I6': {'ID': 'I6', 'Name': 'Helen /Fogler/', 'Gender': 'F', 'Birthday': '1918-09-16', 'Age': 104, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F4']}, 'I7': {'ID': 'I7', 'Name': 'Patricia /Marks/', 'Gender': 'F', 'Birthday': '1955-07-12', 'Age': 67, 'Alive': 'True', 'Death': 'NA', 'Child': 'F4', 'Spouse': ['F6']}, 'I8': {'ID': 'I8', 'Name': 'Brad /Stewart/', 'Gender': 'M', 'Birthday': '1951-07-6', 'Age': 71, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F6']}, 'I9': {'ID': 'I9', 'Name': 'Mitchell /Stewart/', 'Gender': 'M', 'Birthday': '1988-08-10', 'Age': 34, 'Alive': 'True', 'Death': 'NA', 'Child': 'F6', 'Spouse': []}, 'I10': {'ID': 'I10', 'Name': 'Alyssa /Stewart/', 'Gender': 'F', 'Birthday': '1989-05-5', 'Age': 33, 'Alive': 'True', 'Death': 'NA', 'Child': 'F6', 'Spouse': ['F5']}, 'I11': {'ID': 'I11', 'Name': 'Nikola /Stewart/', 'Gender': 'F', 'Birthday': '1989-06-8', 'Age': 33, 'Alive': 'True', 'Death': 'NA', 'Child': 'F6', 'Spouse': ['F2']}, 'I12': {'ID': 'I12', 'Name': 'Alexa /Stewart/', 'Gender': 'F', 'Birthday': '1999-06-3', 'Age': 23, 'Alive': 'True', 'Death': 'NA', 'Child': 'F6', 'Spouse': ['F1']}}
        familyDictionary = {'F1': {'ID': 'F1', 'Marriage': '2011-03-2', 'Divorce': 'NA', 'Husband_ID': 'I1', 'Husband_Name': 'Joseph /Marks/', 'Wife_ID': 'I12', 'Wife_Name': 'Alexa /Stewart/', 'Children': []}, 'F2': {'ID': 'F2', 'Marriage': '2009-02-3', 'Divorce': '2010-04-5', 'Husband_ID': 'I1', 'Husband_Name': 'Joseph /Marks/', 'Wife_ID': 'I11', 'Wife_Name': 'Nikola /Stewart/', 'Children': []}, 'F3': {'ID': 'F3', 'Marriage': '1949-08-15', 'Divorce': 'NA', 'Husband_ID': 'I2', 'Husband_Name': 'Donald /Marks/', 'Wife_ID': 'I3', 'Wife_Name': 'Joyce /Earnhardt/', 'Children': ['I1', 'I4']}, 'F4': {'ID': 'F4', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I5', 'Husband_Name': 'Jack /Marks/', 'Wife_ID': 'I6', 'Wife_Name': 'Helen /Fogler/', 'Children': ['I2', 'I7']}, 'F5': {'ID': 'F5', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I4', 'Husband_Name': 'Jacob /Marks/', 'Wife_ID': 'I10', 'Wife_Name': 'Alyssa /Stewart/', 'Children': []}, 'F6': {'ID': 'F6', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I8', 'Husband_Name': 'Brad /Stewart/', 'Wife_ID': 'I7', 'Wife_Name': 'Patricia /Marks/', 'Children': ['I9', 'I10', 'I11', 'I12']}}
        self.assertFalse(us19_no_marriage_to_first_cousin(individualDictionary, familyDictionary))

    # child marries parent, but doesn't violate the test, returns true
    def test_us19_no_marriage_to_first_cousin_4(self):
        individualDictionary = {'I1': {'ID': 'I1', 'Name': 'Joseph /Marks/', 'Gender': 'M', 'Birthday': '1985-05-13', 'Age': 37, 'Alive': 'True', 'Death': 'NA', 'Child': 'F2', 'Spouse': ['F1']}, 'I2': {'ID': 'I2', 'Name': 'Donald /Marks/', 'Gender': 'M', 'Birthday': '1951-08-15', 'Age': 71, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F2']}, 'I3': {'ID': 'I3', 'Name': 'Joyce /Earnhardt/', 'Gender': 'F', 'Birthday': '1951-10-24', 'Age': 71, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F1', 'F2']}}
        familyDictionary = {'F1': {'ID': 'F1', 'Marriage': '2007-03-4', 'Divorce': 'NA', 'Husband_ID': 'I1', 'Husband_Name': 'Joseph /Marks/', 'Wife_ID': 'I3', 'Wife_Name': 'Joyce /Earnhardt/', 'Children': []}, 'F2': {'ID': 'F2', 'Marriage': '1975-12-24', 'Divorce': '2005-03-3', 'Husband_ID': 'I2', 'Husband_Name': 'Donald /Marks/', 'Wife_ID': 'I3', 'Wife_Name': 'Joyce /Earnhardt/', 'Children': ['I1']}}
        self.assertTrue(us19_no_marriage_to_first_cousin(individualDictionary, familyDictionary))




class test_us20_aunts_uncles_dont_marry_nieces_nephews(unittest.TestCase):

    def generate_Individual_Dictionary(self):
        individualDictionary = {}
        individualDictionary['I1'] = {'ID': 'I1', 'Name': 'Joseph /Marks/', 'Gender': 'M', 'Birthday': '1985-05-13', 'Age': 37, 'Alive': 'True', 'Death': 'NA', 'Child': 'F1', 'Spouse': []}
        individualDictionary['I2'] = {'ID': 'I2', 'Name': 'Joyce /Earnhart/', 'Gender': 'F', 'Birthday': '1951-10-7', 'Age': 71, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F1']}
        individualDictionary['I3'] = {'ID': 'I3', 'Name': 'Don /Marks/', 'Gender': 'M', 'Birthday': '1949-08-15', 'Age': 73, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F1']}
        individualDictionary['I4'] = {'ID': 'I4', 'Name': 'Jacob /Marks/', 'Gender': 'M', 'Birthday': '1982-05-10', 'Age': 40, 'Alive': 'True', 'Death': 'NA', 'Child': 'F1', 'Spouse': ['F2']}
        individualDictionary['I5'] = {'ID': 'I5', 'Name': 'Amanda /Jordan/', 'Gender': 'F', 'Birthday': '1981-03-5', 'Age': 41, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F2']}
        individualDictionary['I6'] = {'ID': 'I6', 'Name': 'Nikola /Marks/', 'Gender': 'F', 'Birthday': '1999-10-7', 'Age': 23, 'Alive': 'True', 'Death': 'NA', 'Child': 'F2', 'Spouse': []}
        individualDictionary['I7'] = {'ID': 'I7', 'Name': 'Anton /Marks/', 'Gender': 'M', 'Birthday': '1998-05-16', 'Age': 24, 'Alive': 'True', 'Death': 'NA', 'Child': 'F2', 'Spouse': []}

        return individualDictionary

    def generate_Family_Dictionary(self):
        familyDictionary = {}
        familyDictionary['F1'] = {'ID': 'F1', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I3', 'Husband_Name': 'Don /Marks/', 'Wife_ID': 'I2', 'Wife_Name': 'Joyce /Earnhart/', 'Children': ['I1', 'I4']}
        familyDictionary['F2'] = {'ID': 'F2', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I4', 'Husband_Name': 'Jacob /Marks/', 'Wife_ID': 'I5', 'Wife_Name': 'Amanda /Jordan/', 'Children': ['I6', 'I7']}

        return familyDictionary

    # Standard set up with no violations - would anticipate true
    def test_us20_aunts_uncles_dont_marry_nieces_nephews_1(self):
        individualDictionary = self.generate_Individual_Dictionary()
        familyDictionary = self.generate_Family_Dictionary()
        self.assertTrue(us20_aunts_uncles_dont_marry_nieces_nephews(individualDictionary, familyDictionary))

    # Niece updated to marry uncle, should return false
    def test_us20_aunts_uncles_dont_marry_nieces_nephews_2(self):

        individualDictionary = {'I1': {'ID': 'I1', 'Name': 'Joseph /Marks/', 'Gender': 'M', 'Birthday': '1985-05-13', 'Age': 37, 'Alive': 'True', 'Death': 'NA', 'Child': 'F2', 'Spouse': ['F1']}, 'I2': {'ID': 'I2', 'Name': 'Joyce /Earnhart/', 'Gender': 'F', 'Birthday': '1951-10-7', 'Age': 71, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F2']}, 'I3': {'ID': 'I3', 'Name': 'Don /Marks/', 'Gender': 'M', 'Birthday': '1949-08-15', 'Age': 73, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F2']}, 'I4': {'ID': 'I4', 'Name': 'Jacob /Marks/', 'Gender': 'M', 'Birthday': '1982-05-10', 'Age': 40, 'Alive': 'True', 'Death': 'NA', 'Child': 'F2', 'Spouse': ['F3']}, 'I5': {'ID': 'I5', 'Name': 'Amanda /Jordan/', 'Gender': 'F', 'Birthday': '1981-03-5', 'Age': 41, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F3']}, 'I6': {'ID': 'I6', 'Name': 'Nikola /Marks/', 'Gender': 'F', 'Birthday': '1999-10-7', 'Age': 23, 'Alive': 'True', 'Death': 'NA', 'Child': 'F3', 'Spouse': ['F1']}, 'I7': {'ID': 'I7', 'Name': 'Anton /Marks/', 'Gender': 'M', 'Birthday': '1998-05-16', 'Age': 24, 'Alive': 'True', 'Death': 'NA', 'Child': 'F3', 'Spouse': []}}
        familyDictionary = {'F1': {'ID': 'F1', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I1', 'Husband_Name': 'Joseph /Marks/', 'Wife_ID': 'I6', 'Wife_Name': 'Nikola /Marks/', 'Children': []}, 'F2': {'ID': 'F2', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I3', 'Husband_Name': 'Don /Marks/', 'Wife_ID': 'I2', 'Wife_Name': 'Joyce /Earnhart/', 'Children': ['I1', 'I4']}, 'F3': {'ID': 'F3', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I4', 'Husband_Name': 'Jacob /Marks/', 'Wife_ID': 'I5', 'Wife_Name': 'Amanda /Jordan/', 'Children': ['I6', 'I7']}}
        self.assertFalse(us20_aunts_uncles_dont_marry_nieces_nephews(individualDictionary, familyDictionary))

    # Uncle originally married wife, then divorced and married niece, returns false
    def test_us20_aunts_uncles_dont_marry_nieces_nephews_3(self):

        individualDictionary = {'I1': {'ID': 'I1', 'Name': 'Joseph /Marks/', 'Gender': 'M', 'Birthday': '1985-06-7', 'Age': 37, 'Alive': 'True', 'Death': 'NA', 'Child': 'F3', 'Spouse': ['F1', 'F2']}, 'I2': {'ID': 'I2', 'Name': 'Donald /Marks/', 'Gender': 'M', 'Birthday': '1949-05-4', 'Age': 73, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F3']}, 'I3': {'ID': 'I3', 'Name': 'Joyce /Marks/', 'Gender': 'F', 'Birthday': '1951-05-5', 'Age': 71, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F3']}, 'I4': {'ID': 'I4', 'Name': 'Jacob /Marks/', 'Gender': 'M', 'Birthday': '1982-03-3', 'Age': 40, 'Alive': 'True', 'Death': 'NA', 'Child': 'F3', 'Spouse': ['F4']}, 'I5': {'ID': 'I5', 'Name': 'Amanda /Jordan/', 'Gender': 'F', 'Birthday': '1981-06-3', 'Age': 41, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F4']}, 'I6': {'ID': 'I6', 'Name': 'Nikola /Marks/', 'Gender': 'F', 'Birthday': '2003-04-4', 'Age': 19, 'Alive': 'True', 'Death': 'NA', 'Child': 'F4', 'Spouse': ['F1']}, 'I7': {'ID': 'I7', 'Name': 'Kamela /Schweibinz/', 'Gender': 'F', 'Birthday': '1999-04-2', 'Age': 23, 'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F2']}}
        familyDictionary = {'F1': {'ID': 'F1', 'Marriage': '2015-04-2', 'Divorce': 'NA', 'Husband_ID': 'I1', 'Husband_Name': 'Joseph /Marks/', 'Wife_ID': 'I6', 'Wife_Name': 'Nikola /Marks/', 'Children': []}, 'F2': {'ID': 'F2', 'Marriage': '2007-03-4', 'Divorce': '2015-02-4', 'Husband_ID': 'I1', 'Husband_Name': 'Joseph /Marks/', 'Wife_ID': 'I7', 'Wife_Name': 'Kamela /Schweibinz/', 'Children': []}, 'F3': {'ID': 'F3', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I2', 'Husband_Name': 'Donald /Marks/', 'Wife_ID': 'I3', 'Wife_Name': 'Joyce /Marks/', 'Children': ['I1', 'I4']}, 'F4': {'ID': 'F4', 'Marriage': '', 'Divorce': 'NA', 'Husband_ID': 'I4', 'Husband_Name': 'Jacob /Marks/', 'Wife_ID': 'I5', 'Wife_Name': 'Amanda /Jordan/', 'Children': ['I6']}}
        self.assertFalse(us20_aunts_uncles_dont_marry_nieces_nephews(individualDictionary, familyDictionary))

    # Child marries parent, but doesn't violate test, should return true
    def test_us20_aunts_uncles_dont_marry_nieces_nephews_4(self):
        individualDictionary = {
            'I1': {'ID': 'I1', 'Name': 'Joseph /Marks/', 'Gender': 'M', 'Birthday': '1985-05-13', 'Age': 37,
                   'Alive': 'True', 'Death': 'NA', 'Child': 'F2', 'Spouse': ['F1']},
            'I2': {'ID': 'I2', 'Name': 'Donald /Marks/', 'Gender': 'M', 'Birthday': '1951-08-15', 'Age': 71,
                   'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F2']},
            'I3': {'ID': 'I3', 'Name': 'Joyce /Earnhardt/', 'Gender': 'F', 'Birthday': '1951-10-24', 'Age': 71,
                   'Alive': 'True', 'Death': 'NA', 'Child': 'NA', 'Spouse': ['F1', 'F2']}}
        familyDictionary = {'F1': {'ID': 'F1', 'Marriage': '2007-03-4', 'Divorce': 'NA', 'Husband_ID': 'I1',
                                   'Husband_Name': 'Joseph /Marks/', 'Wife_ID': 'I3', 'Wife_Name': 'Joyce /Earnhardt/',
                                   'Children': []},
                            'F2': {'ID': 'F2', 'Marriage': '1975-12-24', 'Divorce': '2005-03-3', 'Husband_ID': 'I2',
                                   'Husband_Name': 'Donald /Marks/', 'Wife_ID': 'I3', 'Wife_Name': 'Joyce /Earnhardt/',
                                   'Children': ['I1']}}
        self.assertTrue(us20_aunts_uncles_dont_marry_nieces_nephews(individualDictionary, familyDictionary))

 
class userStories21and23Test(unittest.TestCase):
  
  #test US21, Correct gender for role
  
    def test_us21GenderRoles_1(self): #both husband and wife gender wrong
        result = us21GenderRoles(individualDictionary211, familyDictionary211)
        self.assertFalse(result)

    def test_us21GenderRoles_2(self): #only husband gender wrong
        result = us21GenderRoles(individualDictionary212, familyDictionary212)
        self.assertFalse(result)

    def test_us21GenderRoles_3(self): #only wife gender wrong
        result = us21GenderRoles(individualDictionary213, familyDictionary213)
        self.assertFalse(result)

    def test_us21GenderRoles_4(self): #No gender given
        result = us21GenderRoles(individualDictionary214, familyDictionary214)
        self.assertFalse(result)
    
    #test US23 - Unique name and birth date

    def test_us23UniqueNameandbirth_1(self): #same name and same birthday
        result = us23UniqueNameandbirth(individualDictionary231, familyDictionary231)
        self.assertFalse(result)

    def test_us23UniqueNameandbirth_2(self): #same birthday but different name
        result = us23UniqueNameandbirth(individualDictionary232, familyDictionary231)
        self.assertTrue(result)

    def test_us23UniqueNameandbirth_2(self): #same name but different birthday
        result = us23UniqueNameandbirth(individualDictionary233, familyDictionary231)
        self.assertTrue(result)


class userStories17And18Test(unittest.TestCase):
     #test US17, No marriages to descendants
     def test_noMarriagesToDescendants_1(self):
         result = noMarriagesToDescendants(individualDictionary, familyDictionary)
         self.assertFalse(result)

     def test_noMarriagesToDescendants_2(self):
         individualDictionary['I99']['Spouse'] = []
         individualDictionary["I13"]['Spouse'] = ['F6']
         result = noMarriagesToDescendants(individualDictionary, familyDictionary)
         self.assertTrue(result)

     # test US18, Siblings should not marry
     def test_siblingsShouldNotMarry_3(self):
         result = siblingsShouldNotMarry(individualDictionary, familyDictionary)
         self.assertTrue(result)

     def test_siblingsShouldNotMarry_4(self):
         individualDictionary['I29']['Spouse'] = ['F3']
         individualDictionary['I99']['Spouse'] = ['F3']
         familyDictionary['F3'] = {'ID': 'F3', 'Marriage': '1993-10-9', 'Divorce': 'NA', 'Husband_ID': 'I29', 'Husband_Name': 'Ivan /Marks/',
                           'Wife_ID': 'I99', 'Wife_Name': 'Anna /Marks/', 'Children': []}
         result = siblingsShouldNotMarry(individualDictionary, familyDictionary)
         self.assertFalse(result)
 
class userStories24and25Test(unittest.TestCase):
    
    # US24
    def test_uniqueFamiliesBySpouses_1(self): #same wife name and marriage date
        result = uniqueFamiliesBySpouses(individualDictionary211, familyDictionary324_1)
        self.assertFalse(result)

    def test_uniqueFamiliesBySpouses_2(self): #same husband name and marriage date
        result = uniqueFamiliesBySpouses(individualDictionary212, familyDictionary324_2)
        self.assertFalse(result)

    def test_uniqueFamiliesBySpouses_3(self): #same marriage date and different spouse names
        result = uniqueFamiliesBySpouses(individualDictionary213, familyDictionary324_3)
        self.assertTrue(result)

    def test_uniqueFamiliesBySpouses_4(self): #different marriage date and different spouse names
        result = uniqueFamiliesBySpouses(individualDictionary214, familyDictionary324_4)
        self.assertTrue(result)

    def test_uniqueFamiliesBySpouses_5(self): #No gender given
        result = uniqueFamiliesBySpouses(individualDictionary214, familyDictionary324_5)
        self.assertTrue(result)

    # US25
    def test_uniqueFirstNamesinFamilies_1(self): # empty name and empty birthday
        result = uniqueFirstNamesinFamilies(individualDictionary325_1, familyDictionary325_1)
        self.assertTrue(result)

    def test_uniqueFirstNamesinFamilies_2(self): # same name different birthday
        result = uniqueFirstNamesinFamilies(individualDictionary325_2, familyDictionary325_2)
        self.assertTrue(result)

    def test_uniqueFirstNamesinFamilies_3(self): # differernt name same birthday
        result = uniqueFirstNamesinFamilies(individualDictionary325_3, familyDictionary325_3)
        self.assertTrue(result)

    def test_uniqueFirstNamesinFamilies_4(self): # different name different birthday
        result = uniqueFirstNamesinFamilies(individualDictionary325_4, familyDictionary325_4)
        self.assertTrue(result)

    def test_uniqueFirstNamesinFamilies_5(self): # same name same birthday
        result = uniqueFirstNamesinFamilies(individualDictionary325_5, familyDictionary325_5)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
