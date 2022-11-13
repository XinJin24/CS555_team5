import calendar
from datetime import datetime, timedelta, date

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

def modifiedDate(date, days):
    if days >= 0:
        return str(datetime.strptime(date, '%Y-%m-%d') + timedelta(days=days))[:10]
    else:
        return str(datetime.strptime(date, '%Y-%m-%d') - timedelta(days=days))[:10]

def printError(us, id, message):
    print("ERROR US" + us + " " + id + " " + message)

def preciseAge(birthDate):
    bdList = birthDate.split('-')
    dateTime1 = datetime(int(bdList[0]), int(bdList[1]), int(bdList[2]))
    timeDifference = datetime.now() - dateTime1
    return timeDifference.days




# US26 Corresponding entries
def correspondingEntries(individualDictionary, familyDictionary):
    flag = True
    for indi in individualDictionary:
        child = individualDictionary[indi]['Child']
        spouse = individualDictionary[indi]['Spouse']
        if (child != 'NA'):
            if child not in familyDictionary:
                flag = False
                printError("26", child, "has no corresponding entry.")
        if (spouse != []):
            for s in spouse:
                if s not in familyDictionary:
                    flag = False
                    printError("26", s, "has no corresponding entry.")
    for fam in familyDictionary:
        husband = familyDictionary[fam]['Husband_ID']
        wife = familyDictionary[fam]['Wife_ID']
        children = familyDictionary[fam]['Children']
        if (husband != 'NA'):
            if husband not in individualDictionary:
                flag = False
                printError("26", husband, "has no corresponding entry.")
        if (wife != 'NA'):
            if wife not in individualDictionary:
                flag = False
                printError("26", wife, "has no corresponding entry.")
        if (children != []):
            for child in children:
                if child not in individualDictionary:
                    flag = False
                    printError("26", child, "has no corresponding entry.")
    return flag

# US 28 -  List siblings in families by decreasing age, i.e. oldest siblings first
def list_siblings_decreasing_age(individualDictionary, familyDictionary):
    returnSiblingList = []
    for key, values in familyDictionary.items():
        childrenList = []
        sortedChildrenList = []
        children = values['Children']
        # print(children)
        for child in children:
            birthDate = individualDictionary[child]['Birthday']
            age = preciseAge(birthDate)
            childTuple = (child, age)
            childrenList.append(childTuple)
            # print(childrenList)
        childrenList.sort(reverse=True, key=lambda x: x[1])
        # print(childrenList)
        if len(childrenList) != 0:
            for i in childrenList:
                sortedChildrenList.append(i[0])

        if len(sortedChildrenList) != 0:
            returnSiblingList.append(sortedChildrenList)

    return returnSiblingList

# US 29 -  List all deceased individuals in a GEDCOM file
def list_all_deceased_individuals(individualDictionary, familyDictionary):
    deceasedList = []
    for keys, values in individualDictionary.items():
        if values['Alive'] == 'False':
            deceasedTuple = (values['ID'], values['Name'], values['Death'])
            deceasedList.append(deceasedTuple)
        else:
            continue
    return deceasedList




# US34 List large age differences
def listLargeAgeDifferences(individualDictionary, familyDictionary):
    flag = True
    days_in_year = 365.2425
    for fami in familyDictionary:
        marriage = datetime.strptime(familyDictionary[fami]['Marriage'], "%Y-%m-%d")
        wifeAge = int((marriage - datetime.strptime(individualDictionary[familyDictionary[fami]["Wife_ID"]]['Birthday']
                                                    , "%Y-%m-%d")).days / days_in_year)
        husbandAge = int((marriage - datetime.strptime(individualDictionary[familyDictionary[fami]["Husband_ID"]]['Birthday']
                                                    , "%Y-%m-%d")).days / days_in_year)
        if (max(wifeAge, husbandAge) / min(wifeAge, husbandAge) >= 2):
            flag = False
            printError("34", fami, "were married when the older spouse was more than twice as old as the younger spouse.")
    return flag

# US32 List multiple births, List all multiple births in a GEDCOM file
def listMultipleBirths(individualDictionary, familyDictionary):
    flag = True
    birthMap={}
    for key, value in individualDictionary.items():
        if(value['Birthday']=='NA'):
            continue
        birthday=datetime.datetime.strptime(value['Birthday'], "%Y-%m-%d")
        birthday.month
        day=birthday.month,birthday.day
        if(day in birthMap):
            peopleList = birthMap[day]
            
            peopleList.append(key)
            birthMap[day]=peopleList
        else:
            list=[key]
            birthMap[day]=list
    for key,item in birthMap.items():
        if(len(item)>=2):
            flag = False
            namesString=""
            for index, person in enumerate(item):
                if index != len(item) - 1:
                    namesString+=individualDictionary[person]['Name'].split('/')[0]+individualDictionary[person]['Name'].split('/')[1]+", "
                else: 
                    namesString+=individualDictionary[person]['Name'].split('/')[0]+individualDictionary[person]['Name'].split('/')[1]+", "
            print(namesString," has the same birthday on ",calendar.month_name[key[0]]," ",key[1],".")
    return flag
    

# US33 List orphans, List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file
def listOrphans(individualDictionary, familyDictionary):
    orphansList=[]
    flag=True
    for key, value in familyDictionary.items():
        if(individualDictionary[value['Husband_ID']]['Death']!='NA' and individualDictionary[value['Wife_ID']]['Death']!='NA' and len(value['Children'])>=1):
            husbandDeathDate=datetime.date(int(individualDictionary[value['Husband_ID']]['Death'].split('-')[0]),int(individualDictionary[value['Husband_ID']]['Death'].split('-')[1]),int(individualDictionary[value['Husband_ID']]['Death'].split('-')[2]))
            wifeDeathDate=datetime.date(int(individualDictionary[value['Wife_ID']]['Death'].split('-')[0]),int(individualDictionary[value['Wife_ID']]['Death'].split('-')[1]),int(individualDictionary[value['Wife_ID']]['Death'].split('-')[2]))
            for child in value['Children']:
                childBirthday=individualDictionary[child]['Birthday']
                childBirthday=datetime.datetime.strptime(childBirthday, "%Y-%m-%d")
                dateTurnTo18=datetime.date(childBirthday.year+18, childBirthday.month, childBirthday.day)
                if(husbandDeathDate<dateTurnTo18 and wifeDeathDate<dateTurnTo18):
                    orphansList.append(child)
                    flag=False
    if(len(orphansList)==0):
        return flag
    else:
        printMessage=""
        for index, orphan in enumerate(orphansList):
            if index != len(orphansList) - 1:
                printMessage+=orphan," ",individualDictionary[orphan]['Name'].split('/')[0]," ",individualDictionary[orphan]['Name'].split('/')[1],", "
        print(printMessage, "are orphans.")
    return flag

    
