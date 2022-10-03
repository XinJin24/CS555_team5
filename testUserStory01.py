import unittest
from userStory0102 import getIndividualsAndFamilies, userStory1
import datetime


class TestUserStory01(unittest.TestCase):
    def testBornToday(self):
        individuals, families = getIndividualsAndFamilies('Joseph_Marks_Family.ged')
        birthday = datetime.date.today()
        individuals['I1']['Birthday'] = str(birthday)
        self.assertEqual(userStory1(individuals, families), 1)

    def testBornAfterToday(self):
        individuals, families = getIndividualsAndFamilies('Joseph_Marks_Family.ged')
        birthday = datetime.date.today() + datetime.timedelta(days=1)
        individuals['I1']['Birthday'] = str(birthday)
        self.assertEqual(userStory1(individuals, families), -1)

    def testBornBeforeToday(self):
        individuals, families = getIndividualsAndFamilies('Joseph_Marks_Family.ged')
        birthday = datetime.date.today() - datetime.timedelta(days=1)
        individuals['I1']['Birthday'] = str(birthday)
        self.assertEqual(userStory1(individuals, families), 1)

    def testMarriageAfterToday(self):
        individuals, families = getIndividualsAndFamilies('Joseph_Marks_Family.ged')
        marriage = datetime.date.today() + datetime.timedelta(days=1)
        families['F1']['Marriage'] = str(marriage)
        self.assertEqual(userStory1(individuals, families), -1)
    
    def testMarriageBeforeToday(self):
        individuals, families = getIndividualsAndFamilies('Joseph_Marks_Family.ged')
        marriage = datetime.date.today() - datetime.timedelta(days=1)
        families['F1']['Marriage'] = str(marriage)
        self.assertEqual(userStory1(individuals, families), 1)


if __name__ == "__main__":
    unittest.main()