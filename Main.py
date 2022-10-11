from Sprint1.sprint1_userStories import *
from GEDCOM_ParseCode import *

individualDictionary, familyDictionary= getIndividualsAndFamilies("MarksFamily.ged")
# call user stories below
# US01
userStory1(individualDictionary, familyDictionary)
# US02
userStory2(individualDictionary, familyDictionary)
# US03
birthBeforeDeath(individualDictionary, familyDictionary)
# US04
marriageBeforeDivorce(individualDictionary, familyDictionary)
# US05
us05_marriage_before_death(individualDictionary, familyDictionary)
# US06
us06_divorce_before_death(individualDictionary, familyDictionary)
# US07
ageLessThan150(individualDictionary, familyDictionary)
# US08
birthBeforeMarriageOfParents(individualDictionary, familyDictionary)
# US09
birthBeforeDeathOfParents(individualDictionary, familyDictionary)
# US10
marriageAfter14(individualDictionary, familyDictionary)
# US11
noPolygamy(individualDictionary, familyDictionary)
# US12
parentsNotTooOld(individualDictionary, familyDictionary)
# US15
fewerThan15Siblings(individualDictionary, familyDictionary)
# US16
maleLastName(individualDictionary,familyDictionary)
# US22
us22_unique_ids(individualDictionary, familyDictionary)

