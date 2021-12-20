import time
from datetime import datetime
import os
import json

index = 0
calender = {
    1: "Du papier toilette",
    2: "Une voiture télécomandée",
    3: "Une brouette",
    4: "Du tea froid",
    5: "Un gateau au chocolat",
    6: "Un casque",
    7: "une bouteille d'eau",
    8: "Un Imerde 12 pro max",
    9: "Du lait matérnel",
    10: "100 CHF",
    11: "Un chocolat",
    12: "Une PS5",
    13: "Une souris",
    14: "Une horloge",
    15: "Un Luca",
    16: "Un choufleur",
    17: "Un PC transportable",
    18: "Un switch",
    19: "Une chanson",
    20: "Des gouttes pour les yeux",
    21: "Un écran",
    22: "100 CHFs",
    23: "Une clé USB",
    24: "Un Mars",
    25: "Un Timothée"
}

f = open('save.json', "r")
data = json.loads(f.read())
f.close()

while(index != 666):
    print (data)
    tempInterface = " "
    for x in range(30):
        tempInterface = tempInterface + "_"
    print (tempInterface)
    tempInterface = ""
    for x in range(10):
        if (x + 1 < 10):
            num = " " + str(x + 1)
        else:
            num = str(x + 1)
        if (data['calendar'][0][str(x + 1)] == str("1")):
            tempInterface = tempInterface + "|" + str("  ")
        else:
            tempInterface = tempInterface + "|" +  str(num)
        
    tempInterface = tempInterface + "|"
    print (tempInterface)
    tempInterface = ""
    for x in range(10):
        if (x + 11 < 10):
            num = " " + str(x + 11)
        else:
            num = str(x + 11)
        if (data['calendar'][0][str(x + 11)] == str("1")):
            tempInterface = tempInterface + "|" + str("  ")
        else:
            tempInterface = tempInterface + "|" +  str(num)

    tempInterface = tempInterface + "|"
    print (tempInterface)
    tempInterface = ""
    for x in range(5):
        if (x + 21 < 10):
            num = " " + str(x + 21)
        else:
            num = str(x + 21)
        if (data['calendar'][0][str(x + 21)] == str("1")):
            tempInterface = tempInterface + "|" + str("  ")
        else:
            tempInterface = tempInterface + "|" +  str(num)

    tempInterface = tempInterface + "|"
    print (tempInterface)
    print ("Select case to Open (666 for exit):")
    index = int(input())
    
    if (index < 26 or index > 0):
        date = datetime.now()
        if (date.day >= index and data['calendar'][0][str(index)] == str(0)):
            print ("Voici de que vous avez recu : \"" + str(calender[index]) + "\"")
            data['calendar'][0][str(index)] = str(1)
            input()
        else:
            if (index!= 666):
                print ("ERREUR : tricheur de merde, tu veux tricher enculé")
                input()
    os.system('cls')

with open('save.json', 'w') as outfile:
    json.dump(data, outfile)