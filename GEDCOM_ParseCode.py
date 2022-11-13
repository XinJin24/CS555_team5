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
                elif finalList[0] == '1' and validOneTag(finalList[1]) == 'Y' and finalList[1] == 'BIRT':
                    line1 = next(file)

                    cleanLine = line1.rstrip()
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

                    birthDayUnformatted = finalList[2].split(' ')
                    birthDayFormatted = birthDayUnformatted[2] + '-' + monthDictionary[
                        birthDayUnformatted[1]] + '-' + \
                                        birthDayUnformatted[0]
                    individualDictionary[keyValue]['Birthday'] = birthDayFormatted

                    # populate age
                    year = int(birthDayUnformatted[2])
                    month = int(monthDictionary[birthDayUnformatted[1]])
                    day = int(birthDayUnformatted[0])
                    currentAge = calculateAge(date(year, month, day))
                    individualDictionary[keyValue]['Age'] = currentAge

                elif finalList[0] == '1' and validOneTag(finalList[1]) == 'Y' and finalList[1] == 'DEAT':
                    line1 = next(file)

                    cleanLine = line1.rstrip()
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
                    deathDayUnformatted = finalList[2].split(' ')
                    deathDayFormatted = deathDayUnformatted[2] + '-' + monthDictionary[
                        deathDayUnformatted[1]] + '-' + deathDayUnformatted[0]
                    individualDictionary[keyValue]['Death'] = deathDayFormatted
                    individualDictionary[keyValue]['Alive'] = 'False'

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





