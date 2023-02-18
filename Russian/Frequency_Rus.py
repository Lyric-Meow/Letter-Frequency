
# Copyright © 2023 Erow. All rights reserved.

a = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "щ", "ш", "ъ", "ы", "ь", "э", "ю", "я"]

import json

with open("in_Rus.txt", "r", encoding="utf-8") as my_file:
    fileIn = my_file.read()

en = []

for i in range(33):
     en.append([0,a[i]])

count = 0

for i in fileIn:
    if i.lower() in a:
            #print(i, end="")
            en[a.index(i.lower())][0] += 1
            count += 1
#print()

fileOut = ""

fileOutTwo = ""

fileOutThree = ""

en.sort(reverse=False, key=lambda x: x[1])
en.sort(reverse=True, key=lambda x: x[0])

for j in range(len(en)):
    fileOut += (f"{en[j][1] or None}" + "\t|\t" + f"{en[j][0]}\n")
#print(fileOut)

last = 100
new = 100
for j in range(len(en)):
    new = round(100 / count * en[j][0], 2)
    if (new < 6 and last >= 6) or (new < 3 and last >= 3) or (new < 2 and last >= 2) or (new < 1 and last >= 1) or (new < 0.5 and last >= 0.5):
        fileOutTwo += "\n"
    fileOutTwo += (f"{en[j][1] or None}" + "\t|\t" + f"{round(100 / count * en[j][0], 2)}\n")

    import locale
    locale.setlocale(locale.LC_ALL, '')
    fileOutThree += f"{en[j][1] or None}" + "\t" + locale.format("%f", round(100 / count * en[j][0], 2) / 100) + "\n"
    
        

    last = round(100 / count * en[j][0], 2)
    

with open('counts_Rus.txt', 'w', encoding="utf-8") as outfile:
    outfile.write(fileOut)

with open('procent_Rus.txt', 'w', encoding="utf-8") as outfile:
    outfile.write(fileOutTwo)

with open('procentForExcel_Rus.txt', 'w', encoding="utf-8") as outfile:
    outfile.write(fileOutThree)

