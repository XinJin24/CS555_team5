from datetime import date, datetime, timedelta
from GEDCOM_ParseCode import *

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

