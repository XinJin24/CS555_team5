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
    for key, values in familyDictionary.items():
        childrenList = []
        sortedChildrenList = []
        children = values['Children']
        # print(children)
        for child in children:
            age = individualDictionary[child]['Age']
            childTuple = (child, age)
            childrenList.append(childTuple)
            # print(childrenList)
        childrenList.sort(reverse=True, key=lambda x: x[1])
        # print(childrenList)
        if len(childrenList) != 0:
            for i in childrenList:
                sortedChildrenList.append(i[0])

        if len(sortedChildrenList) != 0:
            print(sortedChildrenList)

# US 28 -  List all deceased individuals in a GEDCOM file
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
