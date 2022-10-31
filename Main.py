from Sprint1.sprint1_userStories import *
from Sprint2.sprint2_userStories import *
from Sprint3.sprint3_userStories import *
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
#US13
us13_sibling_spacing(individualDictionary,familyDictionary)
#US14
us14_multiple_births_less_5(individualDictionary,familyDictionary)
# US15
fewerThan15Siblings(individualDictionary, familyDictionary)
# US16
maleLastName(individualDictionary,familyDictionary)
# US21
us21GenderRoles(individualDictionary, familyDictionary)
# US22
us22_unique_ids(individualDictionary, familyDictionary)
#US23
us23UniqueNameandbirth(individualDictionary, familyDictionary)
# US24
uniqueFamiliesBySpouses(individualDictionary,familyDictionary)
# US25
uniqueFirstNamesinFamilies(individualDictionary,familyDictionary)
