from datetime import date, datetime, timedelta

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
    print("ERROR US"+ us + " " + id + " " + message)

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
                        flag = False
                        printError("09", child, "was born after death of mother.")
                if (fatherDeath != "NA"):
                    if (childBirthday > modifiedDate(fatherDeath, 9*30)):
                        flag = False
                        printError("09", child, "was born 9 months after death of father")
    return flag

# US10 - Marriage after 14
def marriageAfter14(individualDictionary, familyDictionary):
    flag = True
    for fami in familyDictionary:
        marriageDate = familyDictionary[fami]["Marriage"]
        wifeBirthday = individualDictionary[familyDictionary[fami]["Wife_ID"]]["Birthday"]
        husbandBirthday = individualDictionary[familyDictionary[fami]["Husband_ID"]]["Birthday"]
        if(marriageDate < modifiedDate(wifeBirthday, 14 * 365)):
            flag = False
            printError("10", fami, "wife got married before 14 years old.")
        if(marriageDate < modifiedDate(husbandBirthday, 14 * 365)):
            flag = False
            printError("10", fami, "husband got married before 14 years old.")
    return flag
# US11 - Marriage should not occur during marriage to another
def noPolygamy(IndividualDictionary, FamilyDictionary):
    flag = True
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
                        flag = False
                        print("ERROR: US11 Person",key, "is married to two people at once")
                        continue
                    deathDateList = deathDate.split('-')
                    deathDateCompare = datetime(int(deathDateList[0]), int(deathDateList[1]), int(deathDateList[2]))
                    marriageDateList = marriageDate.split('-')
                    marriageDateCompare = datetime(int(marriageDateList[0]), int(marriageDateList[1]), int(marriageDateList[2]))

                    if marriageDateCompare > deathDateCompare:
                        continue
                    else:
                        print("ERROR: US11 Person",key, "is married to two people at once")
                        flag = False
                        continue
                else:
                    priorSeparationList = priorSeparation.split('-')
                    priorSeparationDateCompare = datetime(int(priorSeparationList[0]), int(priorSeparationList[1]), int(priorSeparationList[2]))
                    marriageDateList = marriageDate.split('-')
                    marriageDateCompare = datetime(int(marriageDateList[0]), int(marriageDateList[1]), int(marriageDateList[2]))

                    if marriageDateCompare > priorSeparationDateCompare:
                        continue
                    else:
                        print("ERROR: US11 person ", key, " is married to two people at once")
                        flag = False
                        continue
        else:
            continue
    return flag

# US12 - Parents not too old -- Mother 60, Father 80
def parentsNotTooOld(individualDictionary, familyDictionary):
    flag = True
    for key, values in individualDictionary.items():
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
                    flag = False
                    print("ERROR US12 ", values['Name'] + "Persons dad is more than 80 years older than child")

            if wifeBirthday != 'NA':
                if yearsDifferenceChecker(wifeBirthday, birthday) >= 60:
                    flag = False
                    print("ERROR US12 ", values['Name'] + "Persons mother is more than 60 years older than child")
        else:
            continue
    return flag

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
    flag = True
    for key, values in familyDictionary.items():
        headCount=len(values['Children'])
        if(headCount>=15):
            print("ERROR US15 Fmaily ID: ",key,", has more than 15 siblings")
            flag= False
        continue
    return flag
# US16 - All male members of a family should have the same last name
def maleLastName(individualDictionary, familyDictionary):
    flag= True
    for key, values in familyDictionary.items():
        if(values["Husband_Name"]=='NA'):
            continue
        # if the last name is not in first /lastname/ format, skip
        if "/" not in values["Husband_Name"]:
            husband_lastName=values["Husband_Name"].split(' ')[1]
        else:
            husband_lastName=values["Husband_Name"].split('/')[1]
        # create a empty list to store children's last name
        lastNameList=[]
        if values["Children"]=='NA':
            continue
        for child in values["Children"]:
            if(individualDictionary[child]=='NA'):
                continue
            if(individualDictionary[child]['Gender']=='F'):
                continue

            if "/" not in individualDictionary[child]['Name']:
                lastNameList.append(individualDictionary[child]['Name'].split(' ')[1])
            else:
                lastNameList.append(individualDictionary[child]['Name'].split('/')[1])
        if len(lastNameList)==1:
            continue
        for lastname in lastNameList:
            if lastname!=husband_lastName:
                print("ERROR US 16 Family ",key,", some males in the family has differnet last name." )
                flag=False
        continue
    return flag

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

