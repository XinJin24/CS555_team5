from datetime import datetime, timedelta

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

# US17 - No marriages to descendants
def noMarriagesToDescendants(individualDictionary, familyDictionary):
    flag = True
    for indi in individualDictionary:
        parentsFamily = individualDictionary[indi]['Child']
        childFamily = individualDictionary[indi]['Spouse']
        if (childFamily != [] and parentsFamily != 'NA'):
            father = familyDictionary[parentsFamily]['Husband_ID']
            mother = familyDictionary[parentsFamily]['Wife_ID']
            for fam in childFamily:
                if (familyDictionary[fam]['Husband_ID'] == father):
                    flag = False
                    printError("17", indi, "is married to her father.")
                if (familyDictionary[fam]['Wife_ID'] == mother):
                    flag = False
                    printError("17", indi, "is married to his mother.")
    return flag

# US18 - Siblings should not marry
def siblingsShouldNotMarry(individualDictionary, familyDictionary):
    flag = True
    for fami in familyDictionary:
        wifeFamily = individualDictionary[familyDictionary[fami]["Wife_ID"]]['Child']
        husbandFamily = individualDictionary[familyDictionary[fami]["Husband_ID"]]['Child']
        if(wifeFamily != 'NA' and husbandFamily != 'NA'):
            if (wifeFamily == husbandFamily):
                flag = False
                printError("18", fami, "Siblings marry one another.")
    return flag

#User story - 21 : Correct gender for role
'''Husband in family should be male and wife in family should be female'''

def us21GenderRoles(ind, fam):
     flag = True
     for famkey, value in fam.items():
         husband_id = value['Husband_ID']
         wife_id = value['Wife_ID']

         for indkey, value in ind.items():
             if value['ID'] == husband_id:
                 husband = value
             if value['ID'] == wife_id:
                 wife = value

         if husband['Gender'] != 'M':
             flag = False
             if husband['Gender'] == ' ':
                 print("ERROR US21: Individual " + husband['ID'] + " Husband gender not given")
             else:
                 print("ERROR US21: Individual "+husband['ID']+" Husband is not Male")
         if wife['Gender'] != 'F':
             flag = False
             if wife['Gender'] == ' ':
                 print("ERROR US21: Individual " + wife['ID'] + " Wife gender not given")
             else:
                 print("ERROR US21: Individual "+wife['ID']+" Wife is not Female")

     return flag

#User story - 23 : Unique name and birth date
'''No more than one individual with the same name and birth date should appear in a GEDCOM file'''
def us23UniqueNameandbirth(ind,fam):
    flag = True
    name_and_bd_dict = {}
    for indkey, value in ind.items():
        name1 = value['Name']
        bd1 = value['Birthday']
        if name1 not in name_and_bd_dict:
            name_and_bd_dict[name1] = (indkey, bd1)
        else:
            comparekey, comparebd = name_and_bd_dict[name1]
            if comparebd == bd1:
                flag = False
                print("ERROR US21: Individuals "+ indkey +" and " + comparekey + " has same name and birthdays")

    return flag


# US24 - Unique families by spouses
# No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file
def uniqueFamiliesBySpouses(individualDictionary, familyDictionary):
    flag=True
    for key,value in familyDictionary.items():
        for key2,value2 in familyDictionary.items():
            if(key!=key2 and (value['Husband_Name']==value2['Husband_Name'] or value['Wife_Name']==value2['Wife_Name'])
            and value['Marriage']==value2['Marriage']):
                flag=False
                print("ERROR US24: Family ID : " , key , " has a same spouse and a same marriage date in other family")
    return flag


# US25 - Unique first names in families
# No more than one child with the same name and birth date should appear in a family
def uniqueFirstNamesinFamilies(individualDictionary, familyDictionary):
    flag =True
    for key, value in familyDictionary.items():
        childrenDictionary={}
        if(value['Children']=='NA'):
            continue
        if(len(value['Children'])==1):
            continue
        for child in value['Children']:
            childrenDictionary[child]={'ID':child,'Name':individualDictionary[child]['Name'],'Birthday':individualDictionary[child]['Birthday']}
        
        for key1,value1 in childrenDictionary.items():
            for key2,value2 in childrenDictionary.items():
                if(key1!=key2 and value1['Name']==value2['Name'] and value1['Birthday']==value2['Birthday']):
                    flag=False
                    print("ERROR US25: Family ID : " , key , ", Child ID :", key1, " has another child with the same name and birth date")
    return flag
