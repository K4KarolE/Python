# Movie Title Randomizer (from Excel where there are merged cells with the Movie titles)

import random
from openpyxl import Workbook, load_workbook
wb = load_workbook('D:/Movies.xlsx')
ws = wb.active

#after line 67356 there is still a title at the moment (to line 21)

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
 #   print('You have seen this movie ' + int(HaveSeen) +  ' times.')
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
#print('You have seen this movie ' + int(HaveSeen) +  ' times.')

print()