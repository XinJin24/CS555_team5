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

#user stories
def userStory1(individuals, families):
    curDate = str(date.today())
    for key in individuals:
        if (individuals[key]['Birthday'] > curDate):
            print("ERROR: US01 ",key + ": Birthday is after the current date")
        if (individuals[key]['Death'] != 'NA'):
            if (individuals[key]['Death'] > curDate):
                print("ERROR: US01 ",key + ": Death is after the current date")
    for key in families:
        if (families[key]['Marriage'] > curDate):
            print("ERROR: US01 ",key + ": Marriage is after the current date")
        if (families[key]['Divorce'] != 'NA'):
            if (families[key]['Divorce'] > curDate):
                print("ERROR: US01 ",key + ": Divorce is after the current date")

# US02 - Birth before marriage - Birth should occur before marriage of an individual
def userStory2(individuals, families):
    for key in individuals:
        if (individuals[key]['Spouse'] != 'NA'):
            if (isinstance(individuals[key]['Spouse'], list)):
                for fam in individuals[key]['Spouse']:
                    if (individuals[key]['Birthday'] > families[fam]['Marriage']):
                        print("ERROR: US02 ",key + ", " + fam + ": Birth occur after marriage")
            else:
                if (individuals[key]['Birthday'] > families[individuals[key]['Spouse']]['Marriage']):
                    print("ERROR: US02 ", key + ", " + individuals[key]['Spouse'] + ": Birth occur after marriage")
    


# US03 - Birth Before Death - Birth should occur before death of an individual
def birthBeforeDeath(individualDictionary, familyDictionary):
    for personID, personInfo in individualDictionary.items():
        # Check to ensure individual is in the dicationy
        if(personID==None):
            print("ERROR: INDIVIDUAL: US03: Individual does not exist in the dataset")
            continue
        if(personInfo['Birthday'] == ''):      
            print("ERROR: INDIVIDUAL: US03: Individual " , personID , " does not have a birthdate")
            continue
        # If individual is alive, test not needed, therefore return true
        if(personInfo['Alive'] == 'True'):
            continue
        # Capture birth and death from dictionary, use datetime function and compare dates
        birthdayList = personInfo['Birthday'].split('-')
        deathDayList = personInfo['Death'].split('-')
        birthDay = datetime(int(birthdayList[0]), int(birthdayList[1]), int(birthdayList[2]))
        deathDay = datetime(int(deathDayList[0]), int(deathDayList[1]), int(deathDayList[2]))
        if deathDay > birthDay:
            continue
        # This scenario could potentially occur if baby is born on day of birth, so return true
        elif deathDay == birthDay:
            continue
        # All else should return false as birth would be later than death
        else:
            print("ERROR: INDIVIDUAL: US03: Individual " + personID + " " + "Birthday of " \
                   + personInfo['Birthday'] + " is before their death of " + \
                   personInfo['Death'] + ".")
            continue

# US04 - marriage before divorce - couple must be married before divorce can occur          
def marriageBeforeDivorce(individualDictionary, familyDictionary):
    # Check to ensure family is present in the dictionary
    for familyID, familyInfo in familyDictionary.items():
        if(familyID==None):
            continue
        # If there is no divorce, there is nothing to check, and will return true
        if(familyInfo['Divorce'] == 'NA'):
            continue
        marriageDayList = familyInfo['Marriage'].split('-')
        divorceDayList = familyInfo['Divorce'].split('-')
        marriageDay = datetime(int(marriageDayList[0]), int(marriageDayList[1]), int(marriageDayList[2]))
        divorceDay = datetime(int(divorceDayList[0]), int(divorceDayList[1]), int(divorceDayList[2]))
        if divorceDay < marriageDay:
            print("ERROR US04 family ID: ",familyID, "Divorce hanppened before the date of marriage")



#user story - 05 : Marriage before death -- recorded as error if not
def us05_marriage_before_death(ind, fam):
    for key,value in ind.items():
        if (value['Spouse'] != 'NA'):
            if (value['Death'] != 'NA'):
                deathDate = value['Death']
                if(len(value['Spouse'])!=0):
                    famkey = value['Spouse'][0]
                    marriageDate = fam[famkey]['Marriage']
                    if(marriageDate > deathDate):
                        print("Error US05: Person: " + key + ", "  + ": Marriage date on " , marriageDate + " occur after death date: "+deathDate)
                        continue
                continue



#user story - 06 : Divorce before death -- recorded as error if not
def us06_divorce_before_death(ind, fam):
    for key,value in ind.items():
        if(value['Alive']=='False'):
            continue
        if(value['Spouse']=='NA'):
            continue
        deathDate = value['Death']
        if(len(value['Spouse'])!=0):
            divorceDate = fam[value['Spouse'][0]]['Divorce']
            if(divorceDate > deathDate):
                print("Error US06: Person: " , key , ", " , ": Divorce of " , divorceDate, "occur after death ",deathDate)
                continue
        continue

# US07 - Less then 150 years old - Everyone's age should not be more than 150
def ageLessThan150(individualDictionary, familyDictionary):
    for key, values in individualDictionary.items():
        if values['Age']<0 or values['Age']>=150:
            print("Error US07: person" , key , ", age " , values['Age'], " , more than 150 years old or age invalid")
        continue

# US08 - Birth before marriage of parents - 
def birthBeforeMarriageOfParents(individualDictionary, familyDictionary):
    for familyID, familyInfo in familyDictionary.items():
        if(familyInfo['Children']=='NA'):
            continue
        marriage_date=familyInfo['Marriage'].split('-')
        marriage_date=datetime(int(marriage_date[0]), int(marriage_date[1]), int(marriage_date[2]))
        for child in familyInfo['Children']:
            child_birthday=individualDictionary[child]['Birthday'].split('-')
            child_birthday=datetime(int(child_birthday[0]), int(child_birthday[1]), int(child_birthday[2]))
            if(child_birthday<=marriage_date):
                print("ERROR US 08, child", individualDictionary[child]['Name'], "is born before the marraige of his/her parents")
            continue
        continue

# US09 - Birth before death of parents
def birthBeforeDeathOfParents(individualDictionary, familyDictionary):
    for fami in familyDictionary:
        if (familyDictionary[fami]["Children"] != []):
            motherDeath = individualDictionary[familyDictionary[fami]["Wife_ID"]]["Death"]
            fatherDeath = individualDictionary[familyDictionary[fami]["Husband_ID"]]["Death"]
            for child in familyDictionary[fami]["Children"]:
                childBirthday = individualDictionary[child]["Birthday"]
                if (motherDeath != "NA"):
                    if (childBirthday > motherDeath):
                        print("ERROR 09 ",child + " was born after death of mother.")
                if (fatherDeath != "NA"):
                    if (childBirthday > str(datetime.strptime(fatherDeath, '%Y-%m-%d') + timedelta(days=9*30))[:10]):
                        print("ERROR 09 ", child + " was born 9 months after death of father")

# US10 - Marriage after 14
def marriageAfter14(individualDictionary, familyDictionary):
    for fami in familyDictionary:
        marriageDate = familyDictionary[fami]["Marriage"]
        wifeBirthday = individualDictionary[familyDictionary[fami]["Wife_ID"]]["Birthday"]
        husbandBirthday = individualDictionary[familyDictionary[fami]["Husband_ID"]]["Birthday"]
        if(marriageDate < str(datetime.strptime(wifeBirthday, '%Y-%m-%d') + timedelta(days=14 * 365))[:10]):
            print("ERROR US10"+ fami + " wife got married before 14 years old.")
        if(marriageDate < str(datetime.strptime(husbandBirthday, '%Y-%m-%d') + timedelta(days=14 * 365))[:10]):
            print("ERROR US10"+ fami + " husband got married before 14 years old.")

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
                        print("ERROR: US11 Person",key, "married to two people at once")
                        continue
                    deathDateList = deathDate.split('-')
                    deathDateCompare = datetime(int(deathDateList[0]), int(deathDateList[1]), int(deathDateList[2]))
                    marriageDateList = marriageDate.split('-')
                    marriageDateCompare = datetime(int(marriageDateList[0]), int(marriageDateList[1]), int(marriageDateList[2]))

                    if marriageDateCompare > deathDateCompare:
                        continue
                    else:
                        print("ERROR: US11 Person",key, "married to two people at once")
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

#user story - 13 : Siblings spacing -- recorded as error if not
'''Birth dates of siblings should be more than 8 months apart or 
less than 2 days apart (twins may be born one day apart, e.g. 11:59 PM and 12:02 AM 
the following calendar day) '''

def us13_sibling_spacing(ind,fam):
    flag = True
    for key in fam:
        if fam[key]['Children'] != []:
            bd_list_of_siblings = []
            for i in fam[key]['Children']:
                d = datetime.datetime.strptime(ind[i]['Birthday'], "%Y-%m-%d")
                bd_list_of_siblings.append(d)
            count_of_siblings = len(bd_list_of_siblings)
            if count_of_siblings ==1:
                flag = True
                msg = "OK:US13 " + str(key) + str(fam[key]['Husband_Name']) + " and " + str(fam[key]['Wife_Name']) + "Only one Child : OK"
                # print(msg)
            else:
                i = 0
                while i < count_of_siblings - 1:
                    spacing = bd_list_of_siblings[i+1] - bd_list_of_siblings[i]
                    if spacing > timedelta(days=2) and spacing < timedelta(days=243):
                        i = i+1
                        flag = False
                        msg = "ERROR: US13 " + str(fam[key]['Husband_Name']) + " and " + str(fam[key]['Wife_Name']) + "Wrong spacing b/w siblings"
                        # print(msg)
                    else:
                        i = i + 1
                        flag = True
                        msg = "OK:US13 " + str(key) + str(fam[key]['Husband_Name']) + " and " + str(fam[key]['Wife_Name']) + "No Error"
                        # print(msg)

        else:
            flag = True
            msg = "OK:US13 " + str(key) + str(fam[key]['Husband_Name']) + " and " + str(fam[key]['Wife_Name']) + "No Children : OK"
            # print(msg)
    return flag

#user story - 14 : Multiple births <= 5 -- recorded as error if not
'''No more than five siblings should be born at the same time '''

def us14_multiple_births_less_5(ind,fam):
    flag = True
    for key in fam:
        if fam[key]['Children'] != []:
            bd_list_of_siblings=[]
            for i in fam[key]['Children']:
                bd_list_of_siblings.append(ind[i]['Birthday'])
            frequency_of_bd = Counter(bd_list_of_siblings).most_common(1)
            # print(frequency_of_bd)
            for (x,y) in frequency_of_bd:
                if y>5:
                    msg= "ERROR US14: "+ str(key) + " Family has more than 5 siblings born at same time"
                    flag = False
                    # print(msg)
                else:
                    msg = "OK:US14 " + str(key) + str(fam[key]['Husband_Name']) + " and " + str(fam[key]['Wife_Name'])  +  " Family : No error. Less than 5 siblings"
                    flag = True
                    # print(msg)
        else:
            msg = "OK:US14 " + str(key) + str(fam[key]['Husband_Name']) + " and " + str(fam[key]['Wife_Name']) + " Family : No error. Have no children"
            flag = True
            # print(msg)
    return flag
            
#US15 -There should be fewer than 15 siblings in a family
def fewerThan15Siblings(individualDictionary, familyDictionary):
    for key, values in familyDictionary.items():
        headCount=len(values['Children'])
        if(headCount>=15):
            print("ERROR US15 Fmaily ID: ",key,", has more than 15 siblings")
        continue
# US16 - All male members of a family should have the same last name
def maleLastName(individualDictionary, familyDictionary):
    for key, values in familyDictionary.items():
        husband_lastName=values["Husband_Name"].split('/')[1]
        lastNameList=[husband_lastName]
        if values["Children"]=='NA':
            continue
        for child in values["Children"]:
            if(individualDictionary[child]['Gender']=='F'):
                continue
            lastNameList.append(individualDictionary[child]['Name'].split('/')[1])
        if len(lastNameList)==1:
            continue
        for lastname in lastNameList:
            if lastname!=husband_lastName:
                print("ERROR US 16 Family ",key,", some males in the family has differnet last name." )
        continue


#US22 -Unique IDs
def uniqueIDs(individualDictionary, familyDictionary):
    if z in set_of_IDs:
        return False

def us22_unique_ids(ind,fam):
    list_of_IDs = []
    set_of_IDs = {}
    for x in ind:
        list_of_IDs.append(x)
    for y in fam:
        list_of_IDs.append(y)
    for z in list_of_IDs:
        if z in set_of_IDs:
            print("IDs are not unique.")
            return False
    return True

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



