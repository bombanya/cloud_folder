# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 20:10:04 2019

@author: Даня
"""

import csv
FilesDataFromServer = {'0': [],
                       '1': [("It's.txt", 1), ("Hard.pdf", 2)],
                       '2': [("To.jpg", 3), ("Think up.docx", 4)],
                       '3': [("File.pptx", 5), ("Names.mp3", 6), ("Data.scv", 500)],
                       '4': [("We choose to go.txt", 7), ("To the Moon in this.txt", 8)],
                       '5': [("Decade and do the.txt", 9), ("Other things, not.txt", 10)],
                       '6': [("Because they are.txt", 11), ("Easy, but because.txt", 12)],
                       '7': [("They are hard.txt", 13), ("Because that goal.txt", 14)],
                       '8': [("Will serve to.txt", 15), ("Organize and measure.txt", 16)],
                       '9': [("The best of our.txt", 17), ("Energies and skills.txt", 18)]}

print(FilesDataFromServer)

with open('FilesDataFromServer.csv', 'w', newline='') as csvfile:
     spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|',
                             quoting=csv.QUOTE_MINIMAL)
     for i in FilesDataFromServer:
         spamwriter.writerow([i, FilesDataFromServer[i]])
