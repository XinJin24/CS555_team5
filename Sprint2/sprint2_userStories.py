from datetime import date, datetime, timedelta
from GEDCOM_ParseCode import *

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

