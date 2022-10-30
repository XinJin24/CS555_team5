'''Sprint 3 '''

from datetime import date, datetime, timedelta

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
