# Import all libraries needed for the tutorial
import pandas as pd
from numpy import random
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number
import string
import requests
#from makePDFs import printPDFs

def generateStats():
    potOutcome = ["grounded", "flied", "lined", "double", "popped", "singled", "doubled", "tripled", "homered"]
    direction = ['p', '3b.', 'catcher', 'shortstop', 'pitcher', '1b', 'first', '2b', 'c', 'second', '3b', 'third', 'ss', 'lf', 'left', 'cf', 'center', 'rf', 'right', 'middle', 'short']
    trajectory = ['grounded', 'flied', 'lined']


    names = [];
    results = [];
    area = [];
    traj = [];
    f = open('./../interdata/scraperaw.txt')
    line = f.readline()

    count = 0
    temp = ''
    while line:
        #print(line)

        words = line.split(' ')
        #print(words)
        #

        num1 = 0
        for each in words:

            if (each in potOutcome):
                #print(words)
                if (num1 == 0):
                    #temp = words[words.index(each)]
                    nextName = words[0].lower()
                    if nextName[1] == '.' or len(nextName) < 2:
                        nextName = nextName + ' ' + words[1].lower()
                    names.append(nextName)
                    results.append(each.lower())
                    num1 = 1


                    num = 0;

                    newlines = []
                    for each in words:
                        newlines.append(each.strip(','))
                    words = newlines


                    newlines = []
                    for each in words:
                        newlines.append(each.strip('.\n'))
                    words = newlines

                    for each in words:

                        flag = False
                        if (each == 'down'):
                            flag = True

                        if (num == 0):

                            if (each in direction or each == "down"):
                                if (flag == True):
                                    #if (each == 'rf' or each == 'right' or each == 'left' or each == 'lf'):
                                    temp = 'down '

                                #print(each)
                                #print(words)
                                if (num == 0):

                                    #print(each)

                                    count += 1
                                            #print(count)
                                    #temp2 = words[words.index(each)]
                                    #print(temp2)
                                    if each != 'down':
                                        if (each == 'rf' or each == 'right' or each == 'left' or each == 'lf'):
                                            area.append(temp + each.lower())
                                        else:
                                            area.append(each.lower())
                                        #print(area)

                                        num = 1
                                        temp = ''

                                    #print(count)

                                    #print(count)







        line = f.readline()

    f.close()

    s = pd.Series(names)
    p = pd.Series(results)
    a = pd.Series(area)
    data = pd.DataFrame({'Names':s, 'Results':p, 'Area':a})
    pd.set_option('display.max_rows', 170)
    print(data)
    #printPDFs(data)

def getPlayerStats(teamname, url):
    quote_page = url
    # query the website and return the html to the variable page
    hdr = { 'Moneyball' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' }
    session = requests.Session()
    req = session.get(quote_page, headers=hdr)
    soup = BeautifulSoup(req.content, 'html.parser')
    name_box = soup.findAll('td', attrs={'colspan': '26'})
    firstTeam = "".join(((str(name_box))[18:18+len(teamname)]).split())
    secondTeam = "".join(((str(name_box))[-7-len(teamname):-7]).split())
    player_names = soup.findAll('td', attrs={'width':'20%'})
    playerurls = []
    for player in player_names:
        playerStr = str(player)
        if playerStr[17:19] == "<a" and playerStr[26:29] == "/pl":
            playerurls.append(playerStr[26:97])
    #if teamname == firstTeam:





