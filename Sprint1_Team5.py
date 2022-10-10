'''
Author: Group 5
CS555 - Agile Methods for Software Development
Stevens Institute of Technology
Purpose: Sprint 1 Submission
'''

from datetime import date, datetime, timedelta
import re
from prettytable import PrettyTable

# Define appropriate valid tags for inputs with respective level numbers
zeroTagTuple = ('INDI', 'FAM', 'HEAD', 'TRLR', 'NOTE')

oneTagTuple = ('NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC',
               'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL',
               'DIV')

twoTagTuple = ('DATE')

monthDictionary = {'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAY': '05', 'JUN': '06',
                   'JUL': '07', 'AUG': '08', 'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'}

individuals = PrettyTable()
families= PrettyTable()

# parse the date
def yearsDifferenceChecker(date1, date2):
    date1List = date1.split('-')
    date2List = date2.split('-')
    dateTime1 = datetime(int(date1List[0]), int(date1List[1]), int(date1List[2]))
    dateTime2 = datetime(int(date2List[0]), int(date2List[1]), int(date2List[2]))
    if dateTime2 > dateTime1:
        variance = dateTime2 - dateTime1
        return variance.days / 365.2425
    else:
        variance = dateTime1 - dateTime2
        return variance.days / 365.2425

# function to calculate age in years
def calculateAge(birthDate):
    days_in_year = 365.2425
    age = int((date.today() - birthDate).days / days_in_year)
    return age

# Function to determine if tag is valid for level number 0
def validZeroTag(value):
    if value in zeroTagTuple:
        return "Y"
    else:
        return "N"

# Function to determine if tag is valid for level number 1
def validOneTag(value):
    if value in oneTagTuple:
        return "Y"
    else:
        return "N"

# Function to determine if tag is valid for level number 2
def validTwoTag(value):
    if value in twoTagTuple:
        return "Y"
    else:
        return "N"

def zeroPrefix(value, cleanLine):
    # Two formats are possible:
    # <level_number> <id> <tag>
    # <level_number> <tag> <arguments to be ignored>
    print("--> " + cleanLine)
    if value[2] == "INDI" or value[2] == "FAM":
        print("<-- " + value[0] + "|" + value[2] + "|" + "Y" + "|" + value[1])
    elif value[1] == "HEAD" or value[1] == "TRLR" or value[1] == "NOTE":
        print("<-- " + value[0] + "|" + value[1] + "|" + "Y" + "|" + value[2])

def onePrefix(value, cleanLine):
    # Always will be format <level_number> <tag> <arguments>
    print("--> " + cleanLine)
    print("<-- " + value[0] + "|" + value[1] + "|" + validOneTag(value[1]) + "|" + value[2])

def twoPrefix(value, cleanLine):
    # Always will be format <level_number> <tag> <arguments>
    print("--> " + cleanLine)
    print("<-- " + value[0] + "|" + value[1] + "|" + validTwoTag(value[1]) + "|" + value[2])
    
#function to get the gedcom dictionaries storing the data
def getFamInd(filename):
    return individualDictionary, familyDictionary

# # US01 - Dates before current date - Dates (birth, marriage, divorce, death) should not be after the current date
# def userStory1(ID_Number,individuals, families):
#     curDate = str(date.today())
#     if(individuals.get(ID_Number)!=None):
#         if (individuals[key]['Birthday'] > curDate):
#             print("ERROR US01: "+ ID_Number + ": Birthday is after the current date")
#             return False
#         if (individuals[key]['Death'] != 'NA'):
#             if (individuals[key]['Death'] > curDate):
#                 print("ERROR US01: "+ ID_Number + ": Death is after the current date")
#                 return False
#         return True
#     else:
#         if (families[key]['Marriage'] > curDate):
#             print("ERROR US01: "+ ID_Number + ": Marriage is after the current date")
#             return False
#         if (families[key]['Divorce'] != 'NA'):
#             if (families[key]['Divorce'] > curDate):
#                 print("ERROR US01: "+ ID_Number + ": Divorce is after the current date")
#                 return False
#         return True

# # US02 - Birth before marriage - Birth should occur before marriage of an individual
# def userStory2(key, individuals, families):
#     if (individuals[key]['Spouse'] != 'NA'):
#             if (isinstance(individuals[key]['Spouse'], list)):
#                 for fam in individuals[key]['Spouse']:
#                     if (individuals[key]['Birthday'] > families[fam]['Marriage']):
#                         print("ERROR US02: "+ key+ ", " + fam + ": Birth occur after marriage")
#                         return False
#                 return True
#             else:
#                 if (individuals[key]['Birthday'] > families[individuals[key]['Spouse']]['Marriage']):
#                     print("ERROR US02: "+ key+ ", " + individuals[key]['Spouse'] + ": Birth occur after marriage")
#                     return False
#                 return True
#     return True

# US01 - Dates before current date - Dates (birth, marriage, divorce, death) should not be after the current date
def userStory1(individuals, families):
    curDate = str(date.today())
    errorDateList = []
    for key in individuals:
        if (individuals[key]['Birthday'] > curDate):
            print(key + ": Birthday is after the current date")
            errorDateList.append(individuals[key]['Birthday'])
        if (individuals[key]['Death'] != 'NA'):
            if (individuals[key]['Death'] > curDate):
                print(key + ": Death is after the current date")
                errorDateList.append(individuals[key]['Death'])
    for key in families:
        if (families[key]['Marriage'] > curDate):
            print(key + ": Marriage is after the current date")
            errorDateList.append(families[key]['Marriage'])
        if (families[key]['Divorce'] != 'NA'):
            if (families[key]['Divorce'] > curDate):
                print(key + ": Divorce is after the current date")
                errorDateList.append(families[key]['Divorce'])
    if (len(errorDateList) == 0):
        print("Dates (birth, marriage, divorce, death) are not after the current date\n")
        return 1
    else:
        print(errorDateList)
        print("Dates are after the current date\n")
        return -1

# US02 - Birth before marriage - Birth should occur before marriage of an individual
def userStory2(individuals, families):
    errorList = []
    for key in individuals:
        if (individuals[key]['Spouse'] != 'NA'):
            if (isinstance(individuals[key]['Spouse'], list)):
                for fam in individuals[key]['Spouse']:
                    if (individuals[key]['Birthday'] > families[fam]['Marriage']):
                        errorList.append((key, fam))
                        print(key + ", " + fam + ": Birth occur after marriage")
            else:
                if (individuals[key]['Birthday'] > families[individuals[key]['Spouse']]['Marriage']):
                    errorList.append((key, individuals[key]['Spouse']))
                    print(key + ", " + individuals[key]['Spouse'] + ": Birth occur after marriage")
    if (len(errorList) == 0):
        print("Birth occur before marriage\n")
        return 1
    else:
        print(errorList)
        print("Birth occur after marriage\n")
        return -1


# US03 - Birth Before Death - Birth should occur before death of an individual
def birthBeforeDeath(ID_Number, Dictionary):
    # Check to ensure individual is in the dicationy
    if Dictionary.get(ID_Number) == None:
        print("ERROR: INDIVIDUAL: US03: Individual does not exist in the dataset")
        return None
    if Dictionary[ID_Number]['Birthday'] == '':
        print("ERROR: INDIVIDUAL: US03: Individual " , ID_Number , " does not have a birthdate")
        return True
    # If individual is alive, test not needed, therefore return true
    if Dictionary[ID_Number]['Alive'] == 'True':
        return True
    else:
        # Capture birth and death from dictionary, use datetime function and compare dates
        birthdayList = Dictionary[ID_Number]['Birthday'].split('-')
        deathDayList = Dictionary[ID_Number]['Death'].split('-')
        birthDay = datetime(int(birthdayList[0]), int(birthdayList[1]), int(birthdayList[2]))
        deathDay = datetime(int(deathDayList[0]), int(deathDayList[1]), int(deathDayList[2]))
        if deathDay > birthDay:
            return True
        # This scenario could potentially occur if baby is born on day of birth, so return true
        elif deathDay == birthDay:
            return True
        # All else should return false as birth would be later than death
        else:
            print("ERROR: INDIVIDUAL: US03: Individual " + ID_Number + " " + "Birthday of " \
                   + Dictionary[ID_Number]['Birthday'] + " is before their death of " + \
                   Dictionary[ID_Number]['Death'] + ".")
            return False

# US04 - marriage before divorce - couple must be married before divorce can occur          
def marriageBeforeDivorce(ID_Number, Dictionary):
    # Check to ensure family is present in the dictionary
    if Dictionary.get(ID_Number) == None:
        return False
    # If there is no divorce, there is nothing to check, and will return true
    if Dictionary[ID_Number]['Divorce'] == 'NA':
        return True
    else:
        marriageDayList = Dictionary[ID_Number]['Marriage'].split('-')
        divorceDayList = Dictionary[ID_Number]['Divorce'].split('-')
        marriageDay = datetime(int(marriageDayList[0]), int(marriageDayList[1]), int(marriageDayList[2]))
        divorceDay = datetime(int(divorceDayList[0]), int(divorceDayList[1]), int(divorceDayList[2]))
        if divorceDay > marriageDay:
            return True
        # This scenario could potentially occur if divorced on wedding day :)
        elif divorceDay == marriageDay:
            return True
        # All else should return false as marriage would be later than divorce
        else:
            return False




#user story - 05 : Marriage before death -- recorded as error if not
def us05_marriage_before_death(key, ind, fam):
    if ind.get(key) == None:
        return False #no person found
    if (ind[key]['Spouse'] != 'NA'):
        if (ind[key]['Death'] != 'NA'):
            deathDate = ind[key]['Death']
            famkey = ind[key]['Spouse']
            marriageDate = fam[famkey]['Marriage']
            if(marriageDate > deathDate):
                print("Error US05: " + str(key) + ": Marriage of " + str(ind[key]['Name']) + "occur after death")
                return False
            else:
                # print("OK: " + str(key) + ": " + str(ind[key]['Name']) + " Marriage occurs before death  ")
                return True

        else:
            # print("OK: " + str(key) + ": " + str(ind[key]['Name']) + " Alive ")
            return True
    else:
        # print("OK: " + str(key) + ": " + str(ind[key]['Name']) + " Not Married ")
        return True


#user story - 06 : Divorce before death -- recorded as error if not
def us06_divorce_before_death(key,ind, fam):
    if ind.get(key) == None:
        return False #no person found
    if (ind[key]['Spouse'] != 'NA'):
        if (ind[key]['Death'] != 'NA'):
            deathDate = ind[key]['Death']
            famkey = ind[key]['Spouse']
            if(fam[famkey]['Divorce'] != 'NA'):
                divorceDate = fam[famkey]['Divorce']
                if(divorceDate > deathDate):
                    print("Error US06: " + str(key) +  ": Divorce of " + ind[key]['Name'] + "occur after death")
                    return False
                else:
                    # print("OK: " + str(key) + ": " + str(ind[key]['Name']) +  " Divorce occurs before death  ")
                    return True
            else:
                # print("OK: " + str(key) + ": " + str(ind[key]['Name']) + " Not Divorced ")
                return True
        else:
            # print("OK: " + str(key) + ": " + str(ind[key]['Name']) + " Alive ")
            return True
    else:
        # print("OK: " + str(key) + ": " + str(ind[key]['Name']) + " Not Married ")
        return True


# US07 - Less then 150 years old - Everyone's age should not be more than 150
def ageLessThan150(ID_Number, Dictionary):
    # Check to ensure individual is in the dictionary
    if Dictionary.get(ID_Number)==None:
        return False
    elif Dictionary[ID_Number]['Age']=="":
        print("Error US07: " , ID_Number , " , age is empty")
        return False
    else:
        #get the age
        age=Dictionary[ID_Number]['Age']
        #if the person's age is greater than 150 return false
        if(age>=150 or age<0 or age%1!=0):
            print("Error US07: " , ID_Number , ", " , age , " , age more than 150 years old or age invalid")
            return False
        else:
            return True

# US08 - Birth before marriage of parents - 
def birthBeforeMarriageOfParents(ID_Number, Dictionary,familyDictionary):
    if Dictionary.get(ID_Number) == None:
        return False
    if Dictionary[ID_Number]['Child']== 'NA':
        return True
    # get the person's birthday
    birthdayList = Dictionary[ID_Number]['Birthday'].split('-')
    # get the person's parent's family ID
    parentFamilyID=Dictionary[ID_Number]['Child']
    # get the person's parents' marriage date
    parentMarriageDateList=familyDictionary[parentFamilyID]['Marriage'].split('-')
    # parse the dates to python readable dates in order to make comparsion
    marriageDay = datetime(int(parentMarriageDateList[0]), int(parentMarriageDateList[1]), int(parentMarriageDateList[2]))
    birthDay = datetime(int(birthdayList[0]), int(birthdayList[1]), int(birthdayList[2]))
    # if the person's birthday comes later or equals to his/her parents's marriage date, return true, otherwise, return false
    if(marriageDay < birthDay):
        return True
    elif(marriageDay == birthDay):
        return True
    else:
        print("Error US08: " , ID_Number , ", Birthday: " , birthDay  , ", Parents' marriage date: ,",
                                marriageDay, " Bithday before the marriage date of parents")
        return False

# US09 - Birth before death of parents
def birthBeforeDeathOfParents(individualDictionary, familyDictionary):
    flag = True
    for fami in familyDictionary:
        if (familyDictionary[fami]["Children"] != []):
            motherDeath = individualDictionary[familyDictionary[fami]["Wife_ID"]]["Death"]
            fatherDeath = individualDictionary[familyDictionary[fami]["Husband_ID"]]["Death"]
            for child in familyDictionary[fami]["Children"]:
                childBirthday = individualDictionary[child]["Birthday"]
                if (motherDeath != "NA"):
                    if (childBirthday > motherDeath):
                        print(child + " was born after death of mother.")
                        flag = False
                if (fatherDeath != "NA"):
                    if (childBirthday > str(datetime.strptime(fatherDeath, '%Y-%m-%d') + timedelta(days=9*30))[:10]):
                        print(child + " was born 9 months after death of father")
                        flag = False
    if flag:
        print("Children are born before death of mother and before 9 months after death of father")
    return flag

# US10 - Marriage after 14
def marriageAfter14(individualDictionary, familyDictionary):
    flag = True
    for fami in familyDictionary:
        marriageDate = familyDictionary[fami]["Marriage"]
        wifeBirthday = individualDictionary[familyDictionary[fami]["Wife_ID"]]["Birthday"]
        husbandBirthday = individualDictionary[familyDictionary[fami]["Husband_ID"]]["Birthday"]
        if(marriageDate < str(datetime.strptime(wifeBirthday, '%Y-%m-%d') + timedelta(days=14 * 365))[:10]):
            print(fami + " wife got married before 14 years old.")
            flag = False
        if(marriageDate < str(datetime.strptime(husbandBirthday, '%Y-%m-%d') + timedelta(days=14 * 365))[:10]):
            print(fami + " husband got married before 14 years old.")
            flag = False
    if flag:
        print("Marriages are at least 14 years after birth of both spouses (parents are at least 14 years old)")
    return flag

# US11 - Marriage should not occur during marriage to another
def noPolygamy(IndividualDictionary, FamilyDictionary):
    for key, values in IndividualDictionary.items():
        if len(values['Spouse']) > 1:
            spouseTestList = values['Spouse']
            individual = values['ID']
            for item in range(1,len(spouseTestList)):
                marriageDate = FamilyDictionary[spouseTestList[item]]['Marriage']
                priorSeparation = FamilyDictionary[spouseTestList[item-1]]['Divorce']
                if priorSeparation == 'NA':
                    if FamilyDictionary[spouseTestList[item-1]]['Husband_ID'] == individual:
                        spouseID = FamilyDictionary[spouseTestList[item-1]]['Wife_ID']
                    else:
                        spouseID = FamilyDictionary[spouseTestList[item-1]]['Husband_ID']

                    deathDate = IndividualDictionary[spouseID]['Death']
                    if deathDate == 'NA':
                        print("This person married to two people at once")
                        continue
                    deathDateList = deathDate.split('-')
                    deathDateCompare = datetime(int(deathDateList[0]), int(deathDateList[1]), int(deathDateList[2]))
                    marriageDateList = marriageDate.split('-')
                    marriageDateCompare = datetime(int(marriageDateList[0]), int(marriageDateList[1]), int(marriageDateList[2]))

                    if marriageDateCompare > deathDateCompare:
                        continue
                    else:
                        print("This person married to two people at once")
                        continue
                else:
                    priorSeparationList = priorSeparation.split('-')
                    priorSeparationDateCompare = datetime(int(priorSeparationList[0]), int(priorSeparationList[1]), int(priorSeparationList[2]))
                    marriageDateList = marriageDate.split('-')
                    marriageDateCompare = datetime(int(marriageDateList[0]), int(marriageDateList[1]), int(marriageDateList[2]))

                    if marriageDateCompare > priorSeparationDateCompare:
                        continue
                    else:
                        print("This person mairried to two people at once")
                        continue
        else:
            continue

# US12 - Parents not too old -- Mother 60, Father 80
def parentsNotTooOld(IndividualDictionary, FamilyDictionary):
    for key, values in individualDictionary.items():
        # child = list(individualDictionary.keys())[list(individualDictionary.values()).index(key)]
        child = values['Child']
        birthday = values['Birthday']
        if child == 'NA':
            continue
        if familyDictionary[child] != 'NA':
            husbandID = familyDictionary[child]['Husband_ID']
            wifeID = familyDictionary[child]['Wife_ID']
            husbandBirthday = individualDictionary[husbandID]['Birthday']
            wifeBirthday = individualDictionary[wifeID]['Birthday']
            if husbandBirthday == 'NA' and wifeBirthday == 'NA':
                print("Parents dates are empty, return true")
            if husbandBirthday != 'NA':
                if yearsDifferenceChecker(husbandBirthday, birthday) >= 80:
                    print(values['Name'] + "Persons dad is more than 80 years older than child")

            if wifeBirthday != 'NA':
                if yearsDifferenceChecker(wifeBirthday, birthday) >= 60:
                    print(values['Name'] + "Persons mother is more than 60 years older than child")
        else:
            continue
#US15 -There should be fewer than 15 siblings in a family
def fewerThan15Siblings(individualDictionary, familyDictionary):
    for key, values in familyDictionary.items():
        headCount=len(values['Children'])
        if(headCount>=15):
            print("ERROR US15 Fmaily ID: ",key,", has more than 15 siblings")
        continue

def getIndividualsAndFamilies(fileName):
    with open(fileName) as file:
        # Instantiate a dictionary to capture individual attributes
        individualDictionary = {}
        keyValue = ''
        # Iterate through each line of file
        for line in file:
            # read line and remove new line character at end
            cleanLine = line.rstrip()
            # create a list of each line, splitting on space
            lineList = cleanLine.split(' ')
            # instantiate a blank string to be used below
            remainderString = ""
            # iterate through each line list captured above, range is start on third index
            for item in lineList[2:]:
                # build string from third index and beyond of list
                remainderString = remainderString + " " + item
            # for string created, remove leading or ending white space
            remainderString = remainderString.strip()
            # create final list to be used as input
            finalList = lineList[0], lineList[1], remainderString
            # conditions to determine which calls based on level number

            if finalList[0] == '0':

                if validZeroTag(finalList[2]) == 'Y' and finalList[2] == 'INDI':

                    keyValue = re.sub('[^A-Za-z0-9]+', '', finalList[1])
                    individualDictionary[keyValue] = {'ID': keyValue, 'Name': '', 'Gender': '',
                                                      'Birthday': '', 'Age': '', 'Alive': 'True', 'Death': 'NA',
                                                      'Child': 'NA', 'Spouse': []}
                else:
                    continue
            else:
                if finalList[0] == '1' and validOneTag(finalList[1]) == 'Y' and finalList[1] == 'NAME':
                    individualDictionary[keyValue]['Name'] = finalList[2]
                elif finalList[0] == '1' and validOneTag(finalList[1]) == 'Y' and finalList[1] == 'SEX':
                    individualDictionary[keyValue]['Gender'] = finalList[2]
                elif finalList[0] == '1' and validOneTag(finalList[1]) == 'Y' and finalList[1] == 'FAMS':
                    spouseList = individualDictionary[keyValue]['Spouse']
                    spouse = re.sub('[^A-Za-z0-9]+', '', finalList[2])
                    spouseList.append(spouse)
                    individualDictionary[keyValue]['Spouse'] = spouseList
                    # spouse = re.sub('[^A-Za-z0-9]+', '', finalList[2])
                    # individualDictionary[keyValue]['Spouse'] = spouse
                elif finalList[0] == '1' and validOneTag(finalList[1]) == 'Y' and finalList[1] == 'FAMC':
                    child = re.sub('[^A-Za-z0-9]+', '', finalList[2])
                    individualDictionary[keyValue]['Child'] = child
                elif finalList[0] == '2' and validTwoTag(finalList[1]) == 'Y' and finalList[1] == 'DATE':
                    dateKeyValue = individualDictionary[keyValue]['Birthday']
                    if dateKeyValue != '':
                        deathDayUnformatted = finalList[2].split(' ')
                        deathDayFormatted = deathDayUnformatted[2] + '-' + monthDictionary[
                            deathDayUnformatted[1]] + '-' + \
                                            deathDayUnformatted[0]
                        individualDictionary[keyValue]['Death'] = deathDayFormatted
                        individualDictionary[keyValue]['Alive'] = 'False'
                    else:
                        birthDayUnformatted = finalList[2].split(' ')
                        birthDayFormatted = birthDayUnformatted[2] + '-' + monthDictionary[
                            birthDayUnformatted[1]] + '-' + birthDayUnformatted[0]
                        individualDictionary[keyValue]['Birthday'] = birthDayFormatted

                        # populate birthdate
                        year = int(birthDayUnformatted[2])
                        month = int(monthDictionary[birthDayUnformatted[1]])
                        day = int(birthDayUnformatted[0])
                        currentAge = calculateAge(date(year, month, day))
                        individualDictionary[keyValue]['Age'] = currentAge
                else:
                    continue
    with open(fileName) as file:
        # Instantiate a dictionary to capture individual attributes
        familyDictionary = {}
        familyKeyValue = ''
        # Iterate through each line of file
        for line in file:
            # read line and remove new line character at end
            cleanLine = line.rstrip()
            # create a list of each line, splitting on space
            lineList = cleanLine.split(' ')
            # instantiate a blank string to be used below
            remainderString = ""
            # iterate through each line list captured above, range is start on third index
            for item in lineList[2:]:
                # build string from third index and beyond of list
                remainderString = remainderString + " " + item
            # for string created, remove leading or ending white space
            remainderString = remainderString.strip()
            # create final list to be used as input
            finalList = lineList[0], lineList[1], remainderString
            # conditions to determine which calls based on level number
            # print(finalList)

            if finalList[0] == '0' and finalList[2] == 'FAM':

                familyKeyValue = re.sub('[^A-Za-z0-9]+', '', finalList[1])
                familyDictionary[familyKeyValue] = {'ID': familyKeyValue, 'Marriage': '', 'Divorce': 'NA',
                                                    'Husband_ID': '', 'Husband_Name': '', 'Wife_ID': '',
                                                    'Wife_Name': '', 'Children': []}

            elif finalList[0] == '1' and validOneTag(finalList[1]) == 'Y' and finalList[1] == 'HUSB':
                husband_id = re.sub('[^A-Za-z0-9]+', '', finalList[2])
                familyDictionary[familyKeyValue]['Husband_ID'] = husband_id
                familyDictionary[familyKeyValue]['Husband_Name'] = individualDictionary[husband_id]['Name']
            elif finalList[0] == '1' and validOneTag(finalList[1]) == 'Y' and finalList[1] == 'WIFE':
                wife_id = re.sub('[^A-Za-z0-9]+', '', finalList[2])
                familyDictionary[familyKeyValue]['Wife_ID'] = wife_id
                familyDictionary[familyKeyValue]['Wife_Name'] = individualDictionary[wife_id]['Name']
            elif finalList[0] == '1' and validOneTag(finalList[1]) == 'Y' and finalList[1] == 'CHIL':
                childrenList = familyDictionary[familyKeyValue]['Children']
                child = re.sub('[^A-Za-z0-9]+', '', finalList[2])
                childrenList.append(child)
                familyDictionary[familyKeyValue]['Children'] = childrenList
            elif finalList[0] == '1' and finalList[1] == 'MARR':

                # if married, move the cursor to the next line to fetch Married Date record
                line1 = next(file)
                cleanLine = line1.rstrip()
                lineList = cleanLine.split(' ')
                remainderString = ""
                for item in lineList[2:]:
                    remainderString = remainderString + " " + item
                remainderString = remainderString.strip()
                finalList2 = lineList[0], lineList[1], remainderString
                married_date = finalList2[2]
                marriedUnformatted = married_date.split(' ')
                marriageFormatted = marriedUnformatted[2] + '-' + monthDictionary[marriedUnformatted[1]] + '-' + \
                                    marriedUnformatted[0]
                familyDictionary[familyKeyValue]['Marriage'] = marriageFormatted

            elif finalList[0] == '1' and finalList[1] == 'DIV':
                # move the cursor to the next line to check if there is divorce record
                line2 = next(file)
                cleanLine = line2.rstrip()
                lineList = cleanLine.split(' ')
                remainderString = ""
                for item in lineList[2:]:
                    remainderString = remainderString + " " + item
                remainderString = remainderString.strip()
                finalList2 = lineList[0], lineList[1], remainderString
                divorceUnformatted = finalList2[2].split(' ')
                divorceFormatted = divorceUnformatted[2] + '-' + monthDictionary[divorceUnformatted[1]] + '-' + \
                                   divorceUnformatted[0]
                familyDictionary[familyKeyValue]['Divorce'] = divorceFormatted

            else:
                continue
    return individualDictionary, familyDictionary
# Main method to open file - input file name below
# print("What file would you like to process?")
# inputFile = str(input())
inputFile = "MarksFamily.ged"
individualDictionary,familyDictionary=getIndividualsAndFamilies(inputFile)

print("\n")
print("Individuals:")
individuals.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
for key in individualDictionary:
        spouseList = individualDictionary.get(key).get('Spouse')
        if len(spouseList) != 0:
            spouseValue = spouseList[-1]
        else:
            spouseValue = 'NA'
        individuals.add_row([individualDictionary.get(key).get('ID')
                    ,individualDictionary.get(key).get('Name')
                    ,individualDictionary.get(key).get('Gender')
                    ,individualDictionary.get(key).get('Birthday')
                    ,individualDictionary.get(key).get('Age')
                    ,individualDictionary.get(key).get('Alive')
                    ,individualDictionary.get(key).get('Death')
                    ,individualDictionary.get(key).get('Child')
                    ,spouseValue])

print(individuals)


print("\n")
print("Families:")
families.field_names=["ID","Married","Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
for key in familyDictionary:
        families.add_row([familyDictionary.get(key).get('ID')
                    ,familyDictionary.get(key).get('Marriage')
                    ,familyDictionary.get(key).get('Divorce')
                    ,familyDictionary.get(key).get('Husband_ID')
                    ,familyDictionary.get(key).get('Husband_Name')
                    ,familyDictionary.get(key).get('Wife_ID')
                    ,familyDictionary.get(key).get('Wife_Name')
                    ,familyDictionary.get(key).get('Children')])
print(families)


# call user stories below
#US12
#parentsNotTooOld(individualDictionary, familyDictionary)
#US15
#fewerThan15Siblings(individualDictionary, familyDictionary)
#US11
#noPolygamy(individualDictionary, familyDictionary)
#US09
birthBeforeDeathOfParents(individualDictionary, familyDictionary)
#US10
marriageAfter14(individualDictionary, familyDictionary)



