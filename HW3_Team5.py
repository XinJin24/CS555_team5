'''
Author: Group 5
CS555 - Agile Methods for Software Development
Stevens Institute of Technology
Purpose: Program to test GEDCOM data
'''

from datetime import date
import re

# Define appropriate valid tags for inputs with respective level numbers
zeroTagTuple = ('INDI', 'FAM', 'HEAD', 'TRLR', 'NOTE')

oneTagTuple = ('NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC',
               'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL',
               'DIV')

twoTagTuple = ('DATE')

monthDictionary = {'JAN': '01', 'FEB': '02', 'MAR': '03', 'APR': '04', 'MAY': '05', 'JUN': '06',
                   'JUL': '07', 'AUG': '08', 'SEP': '09', 'OCT': '10', 'NOV': '11', 'DEC': '12'}

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

# Main method to open file - input file name below
with open("Joseph_Marks_Family.ged") as file:
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
                                                            'Child' : '', 'Spouse': ''}
            else:
                continue
        else:
            if finalList[0] == '1' and validOneTag(finalList[1]) == 'Y' and finalList[1] == 'NAME':
                individualDictionary[keyValue]['Name'] = finalList[2]
            elif finalList[0] == '1' and validOneTag(finalList[1]) == 'Y' and finalList[1] == 'SEX':
                individualDictionary[keyValue]['Gender'] = finalList[2]
            elif finalList[0] == '1' and validOneTag(finalList[1]) == 'Y' and finalList[1] == 'FAMS':
                spouse = re.sub('[^A-Za-z0-9]+', '', finalList[2])
                individualDictionary[keyValue]['Spouse'] = spouse
            elif finalList[0] == '1' and validOneTag(finalList[1]) == 'Y' and finalList[1] == 'FAMC':
                child = re.sub('[^A-Za-z0-9]+', '', finalList[2])
                individualDictionary[keyValue]['Child'] = child
            elif finalList[0] == '2' and validTwoTag(finalList[1]) == 'Y' and finalList[1] == 'DATE':
                dateKeyValue = individualDictionary[keyValue]['Birthday']
                if dateKeyValue != '':
                    deathDayUnformatted = finalList[2].split(' ')
                    deathDayFormatted = deathDayUnformatted[2] + '-' + monthDictionary[deathDayUnformatted[1]] + '-' + \
                                        deathDayUnformatted[0]
                    individualDictionary[keyValue]['Death'] = deathDayFormatted
                    individualDictionary[keyValue]['Alive'] = 'False'
                else:
                    birthDayUnformatted = finalList[2].split(' ')
                    birthDayFormatted = birthDayUnformatted[2] + '-' + monthDictionary[birthDayUnformatted[1]] + '-' + birthDayUnformatted[0]
                    individualDictionary[keyValue]['Birthday'] = birthDayFormatted

                    # populate birthdate
                    year = int(birthDayUnformatted[2])
                    month = int(monthDictionary[birthDayUnformatted[1]])
                    day = int(birthDayUnformatted[0])
                    currentAge = calculateAge(date(year, month, day))
                    individualDictionary[keyValue]['Age'] = currentAge
            else:
                continue

print("\n")
print("Individual Dictionary:")
print(individualDictionary)
print("\n")

with open("Joseph_Marks_Family.ged") as file:
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
            familyDictionary[familyKeyValue] = {'ID': familyKeyValue, 'Marriage': '', 'Divorce': '',
                                                        'Husband_ID': '', 'Husband_Name': '', 'Wife_ID': '',
                                                        'Wife_Name': '', 'Children' : []}


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
        elif finalList[0] == '2' and validTwoTag(finalList[1]) == 'Y' and finalList[1] == 'DATE':
            # MARRIAGE DATE AND DIVORCE DATE ARE NOT PROPERLY POPULATING IN DICTIONARY...
            continue
        else:
            continue



print("\n")
print("Family Dictionary:")
print(familyDictionary)
print("\n")
# print(individualDictionary)
#print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format('ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse'))

#for value in individualDictionary.items():
#    print(value)













