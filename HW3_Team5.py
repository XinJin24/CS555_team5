'''
CS555 - Agile Methods for Software Development
Group 5 - Assignment 3 Submission
Stevens Institute of Technology
Purpose: Program to test GEDCOM data
'''

# Define appropriate valid tags for inputs with respective level numbers
zeroTagTuple = ('INDI', 'FAM', 'HEAD', 'TRLR', 'NOTE')

oneTagTuple = ('NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC',
               'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL',
               'DIV')

twoTagTuple = ('DATE')

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
with open("JosephMarks_FamilyTree.ged") as file:
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
        try:
            if finalList[0] == '0':
                zeroPrefix(finalList, cleanLine)
            elif finalList[0] == '1':
                onePrefix(finalList, cleanLine)
            elif finalList[0] == '2':
                twoPrefix(finalList, cleanLine)
            else:
                print("--> " + cleanLine)
                print("<-- " + finalList[0] + "|" + finalList[1] + "|" + "N" + "|" + finalList[2])
        except:
            continue









