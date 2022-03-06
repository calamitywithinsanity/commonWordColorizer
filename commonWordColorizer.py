#!/usr/bin/env python3

#Turning words different colors to show how common they are! D:

from html.entities import html5
import re

bandDescription = open("GVFDescription.txt")
bandDescriptionContent = bandDescription.read()
bandDescriptionContent = bandDescriptionContent.lower()
bandDescriptionContent = re.sub(r'[^a-zA-Z ]+','', bandDescriptionContent)

for i in bandDescriptionContent:
    bandDescriptionContentWordArray = bandDescriptionContent.split()

bandDescriptionContentWordArrayValue = [0] * len(bandDescriptionContentWordArray)
htmlPrep = []

def wordlist(file):
    topNumber = open(file)
    topNumberContent = topNumber.read()
    topNumberContentWordlist = topNumberContent.split()

    for i in range(len(bandDescriptionContentWordArrayValue)):
        if bandDescriptionContentWordArray[i] in topNumberContentWordlist:
            bandDescriptionContentWordArrayValue[i] = bandDescriptionContentWordArrayValue[i] + 1
        else:
            continue 

#########################everything beyond top list = black
wordlist("top8181.csv") #top8181 = darkest gray
wordlist("top3000.csv") #top3000 = dark gray
wordlist("top1000.csv") #top1000 = medium gray
wordlist("top100.csv") #top100 = light gray

for i in range(len(bandDescriptionContentWordArrayValue)):
    wordAtI = " " + str(bandDescriptionContentWordArray[i]) + " "

    if bandDescriptionContentWordArrayValue[i] == 4:
        htmlPrep.append("<span style=\"color:#CBCBCB;\"> " + wordAtI + " </span>")
    if bandDescriptionContentWordArrayValue[i] == 3:
        htmlPrep.append("<span style=\"color:#9A9A9A;\"> " + wordAtI + " </span>")
    if bandDescriptionContentWordArrayValue[i] == 2:
        htmlPrep.append("<span style=\"color:#656565;\"> " + wordAtI + " </span>")
    if bandDescriptionContentWordArrayValue[i] == 1:
        htmlPrep.append("<span style=\"color:#343434;\"> " + wordAtI + " </span>")
    if bandDescriptionContentWordArrayValue[i] == 0:
        htmlPrep.append("<span style=\"color:#000000;\"><strong> " + wordAtI + " </strong></span>")

htmlPrep = '\u2005'.join(htmlPrep)

file = open('htmlBoilerplate.html', 'w')

htmlBeginning = "<html><head><title>Title</title></head><body><h2>Common Word Colorizer</h2>"
htmlMiddle = str(htmlPrep)
htmlEnd = "</body></html>"

html_template = htmlBeginning + htmlMiddle + htmlEnd
  
#writing the code into the file
file.write(html_template)
  
# close the file
file.close()