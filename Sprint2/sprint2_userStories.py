from datetime import date, datetime, timedelta
from GEDCOM_ParseCode import *

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

