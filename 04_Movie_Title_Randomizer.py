# Movie Title Randomizer (from Excel where there are merged cells with the Movie titles)

import random
from openpyxl import Workbook, load_workbook
wb = load_workbook('D:/Movies.xlsx', data_only=True)
ws = wb.active

#data_only=True -> copying values from excel instead of formulas for the Haveseen value
#after line 67356 there is still a title at the moment (guide line 31)

cellnumber = random.randrange(6,6736)

cell = 'C' + str(cellnumber)
movietitle = ws[cell].value

cellRYear = 'E' + str(cellnumber)
ReleaseYear = ws[cellRYear].value


cellHSeen = 'N' + str(cellnumber)
HaveSeen = ws[cellHSeen].value


print()


if movietitle != None:
    print('Your movie this afternoon: ' + str(movietitle) + '(' + str(ReleaseYear) + ')')
    if HaveSeen == 1: 
        print('You have seen this movie only once since 05/2012.\n')
    else:
        print('You have seen this movie ' + str(HaveSeen) +  ' times since 05/2012.\n')
    quit() 

while movietitle == None:
    cellnumber += 1
    cell = 'C' + str(cellnumber)
    movietitle = ws[cell].value
    cellRYear = 'E' + str(cellnumber)
    ReleaseYear = ws[cellRYear].value
    cellHSeen = 'N' + str(cellnumber)
    HaveSeen = ws[cellHSeen].value
    
print('Your movie tonight: ' + str(movietitle) + '(' + str(ReleaseYear) + ')')

if HaveSeen == 1: 
    print('You have seen this movie only once since 05/2012.\n')
else:
    print('You have seen this movie ' + str(HaveSeen) +  ' times since 05/2012.\n')