# Import all libraries needed for the tutorial
import pandas as pd
import requests
from bs4 import BeautifulSoup
from makePDFs import printPDFs
from time import sleep

#parses the rawtext into panda format
#add playerdata back
def generateStats(playerdata, teamName):

    #Keys of all potential outcomes, directions and trajectory.
    #Basically looking for these words in the rawtext

    # print(playerdata)
    roster = playerdata["Names"].tolist()
    # print(roster)

    potOutcome = ["grounded", "flied", "lined", "double", "popped", "singled",
                  "doubled", "tripled", "homered"]
    direction = ['p', '3b.', 'catcher', 'shortstop', 'pitcher', '1b', 'first',
                 '2b', 'c', 'second', '3b', 'third', 'ss',
                 'lf', 'left', 'cf', 'center', 'rf', 'right', 'middle', 'short']

    outcomes = ["grounded", "flied", "lined", "double", "popped", "singled", "reached"
                  "doubled", "tripled", "homered", "struck", "out", "pinch", "stole",
                  ]
    #arrays for various categories
    names = [];
    results = [];
    area = [];

    #the dict works like this: {"player1": [# of strikes, # of walks, # of stolen bases],
    #   "player2": [# of strikes, # of walks, # of stolen bases],
    #   "player3": [# of strikes, # of walks, # of stolen bases]... etc}
    playerDict = {};

    #reading the raw data
    f = open('./interdata/scraperaw.txt')
    line = f.readline()

    count = 0
    temp = ''
    while line:


        #splits each line by individual words
        words = line.split(' ')

        newlines = []
        for each in words:
            each = each.strip(',')
            each = each.strip('.\n')
            newlines.append(each)
        words = newlines



        #marker to see if the player name has been added to the array
        num1 = 0


        #loop through every word and find the words that match the ones in the
        #keys
        #
        #

        # print(words)
        # names.append(words[0].strip(',').lower())
        tempName = words[0].lower()



        # if (len(tempName) > 2 and len(words[1]) > 2 and words[1] not in outcomes):
        #     tempName = words[1].lower() + ', ' + tempName[0]

        print("THIS IS ROSTER:")
        print(roster)
        if len(words[1]) <= 2:

            tempName = tempName + ', ' + words[1].lower()

        elif (len(tempName) <= 2):
            tempName = words[1].lower() + ', ' + tempName

        tempName2 = tempName
        for i in range(len(roster)):
            print("THIS IS TEMPNAME")
            print(tempName)
            each = roster[i].lower()
            index = each.find(tempName2)
            print("THIS IS INDEX")
            print(index)
            if (index != -1):
                tempName = roster[i]
                break

        #adds the players to a dictionary and calculates the number of strikes
        #walks and steals for each player
        #the dict works like this: {"player": [# of strikes, # of walks, # of stolen bases]}
        if ('struck' in words):
            #add the player name if not in dictionary, initalize all values to
            #0, and then add the count for the appropriate value
            if (tempName not in playerDict.keys()):
                playerDict[tempName] = [0, 0, 0]
                playerDict[tempName][0] = 1
            else:
                playerDict[tempName][0] = playerDict[tempName][0] + 1
        elif ('walked' in words):
            #add 1 to count
            if (tempName not in playerDict.keys()):
                playerDict[tempName] = [0, 0, 0]
                playerDict[tempName][1] = 1
            else:
                playerDict[tempName][1] = playerDict[tempName][1] + 1
        elif ('stole' in words):
            if (tempName not in playerDict.keys()):
                playerDict[tempName] = [0, 0, 0]
                playerDict[tempName][2] = 1
            else:
                playerDict[tempName][2] = playerDict[tempName][2] + 1

        # checks to see if a player bunted first and then adds the player to
        # players array and adds the result as bunt
        if ('bunt' in words):
            dirFlag = True

            names.append(tempName)

            results.append('bunt')
            for each in words:
                if dirFlag:
                    if (each == 'down'):
                        for each in words:
                            if each in direction:
                                area.append('down ' + each)
                                dirFlag = False

                    if (each == 'through'):
                        for other in words:
                            if (other in direction):
                                # print('inside')
                                if (other == 'rf' or other == 'right' or other == 'left' or other == 'lf'):
                                    area.append('through ' + other)
                                    dirFlag = False
                    else:
                        if (dirFlag):
                            if (each in direction):
                                area.append(each)
                                dirFlag = False
            if dirFlag:
                area.append('pitcher')
                dirFlag = False

        else:
            for each in words:

                resFlag = True
                dirFlag = True
                if (each in potOutcome) and (resFlag):

                    result = each
                    for each in words:

                        if dirFlag and resFlag:
                            if ('center' in words):
                                for other in words:
                                    if (other in direction) and (other != 'center'):
                                        # print('inside')
                                        if (other == 'rf' or other == 'right' or other == 'left' or other == 'lf'):
                                            area.append(other + ' center')
                                            dirFlag = False
                                            names.append(tempName)
                                            results.append(result)
                                            resFlag = False

                            if (each == 'down'):
                                for each in words:
                                    if each in direction:
                                        area.append('down ' + each)
                                        dirFlag = False
                                        names.append(tempName)
                                        results.append(result)
                                        resFlag = False

                            if (each == 'through'):
                                for other in words:
                                    if (other in direction):
                                        # print('inside')
                                        if (other == 'rf' or other == 'right' or other == 'left' or other == 'lf'):
                                            area.append('through ' + other)
                                            dirFlag = False
                                            names.append(tempName)
                                            results.append(result)
                                            resFlag = False

                            else:
                                if (dirFlag):
                                    if (each in direction):
                                        area.append(each)
                                        dirFlag = False
                                        names.append(tempName)
                                        results.append(result)
                                        resFlag = False

        # checks to see if the name is added in results but not already in
        # the player dict,
        if ((tempName not in playerDict.keys()) and (tempName in names)):
            playerDict[tempName] = [0, 0, 0]

        line = f.readline()

    f.close()

    s = pd.Series(names)
    p = pd.Series(results)
    a = pd.Series(area)
    data = pd.DataFrame({'Names': s, 'Results': p, 'Area': a})
    pd.set_option('display.max_rows', 220)
    print(data)
    print(playerDict)
    # TODO: uncomment

    printPDFs(data, playerdata, playerDict, teamName)


def getAllPlayers(url):
    quote_page = url
    # query the website and return the html to the variable page
    hdr = {
        'Moneyball': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    session = requests.Session()
    req = session.get(quote_page, headers=hdr)
    soup = BeautifulSoup(req.content, 'html.parser')
    print('got players\n' + str(soup))
    tester = soup.findAll('a')
    #now we have the url for the team roster
    teamRoster = 'http://stats.ncaa.org' + str(tester[9])[9:33]
    session.close()
    sleep(1)


    return (getPlayerStats(teamRoster))

def getPlayerStats(url):
    quote_page = url
    # query the website and return the html to the variable page
    hdr = {
        'Moneyball': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    session = requests.Session()
    req = session.get(quote_page, headers=hdr)
    soup = BeautifulSoup(req.content, 'html.parser')
    name_boxes = soup.findAll('a')
    i = 0
    playerurls = []
    playernames = []
    for box in name_boxes:
        print('Another One')
        #first 13 are useless
        if (i >= 13):
            #need these to access each players stats
            playerurls.append ('http://stats.ncaa.org' + (str(name_boxes[i])[9:52]) + str(name_boxes[i])[56:80])
            #need this to match up on PDFs later
            playernames.append(str(name_boxes[i])[82:-4])
        i += 1
    allStatsForEveryone = []
    j=0
    session.close()
    sleep(1)


    #we need to visit each player page
    for player in playerurls:
        quote_page2 = player
        hdr = {
            'Moneyball': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        session = requests.Session()
        req = session.get(quote_page2, headers=hdr)
        soup2 = BeautifulSoup(req.content, 'html.parser')
        print('Got player URL')
        #getting what houses the data
        dataFields = soup2.findAll('tr', attrs={'class': 'text'})
        #Getting this seasons stats row
        dataStr = str(dataFields[len(dataFields) - 1])
        stats = []
        #getting each individual statfrom that row
        for k in range(len(dataStr) - 8):
            if dataStr[k:k + 5] == '<div>':
                stats.append("".join(dataStr[k + 25:k + 40].split()))
        listOfStats = [2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 23, 24]
        # length 17 becasue counting stinks
        statNames = ['BA (2)', 'OBPct(3)', 'SLGPct(4)', 'AB(5)', 'R(6)', 'H(7)', '2B(8)', '3B(9)', 'HR(11)', 'BB(13)', 'HBP(14)', 'RBI(15)','SF(16)', 'SH(17)', 'K(18)', 'SB(23)', 'CS(24)']
        finalStats = []
        #getting only the stats we want

        for jk in range(len(stats)):
            if jk in listOfStats:
                toAdd = stats[jk]
                #if the stat is blank, it wont be 0
                if len(toAdd) < 6:
                    finalStats.append(toAdd)
                else:
                    finalStats.append('0')
        j += 1
        #calculating woba
        woba = round(float(float(finalStats[2]) + float(finalStats[1]) * 2) / 3, 3)
        stealAttempts = (int(finalStats[13]) + int(finalStats[12]))


        # firsbase = int(listOfStats[4]) - int(listOfStats[5]) - int(listOfStats[6]) - int(listOfStats[7])
        finalStats.append(woba)
        finalStats.append(stealAttempts)

        # finalStats.append(firsbase)
        statNames.append('WOBA')
        statNames.append('SBA')
        # statNames.append('1b')
        allStatsForEveryone.append(finalStats)
        session.close()
        sleep(1)



    pnames = pd.Series(playernames)
    sdata = pd.Series(allStatsForEveryone)

    data = pd.DataFrame({'Names': pnames, 'Stats': sdata})


    return (data)





# if __name__ == "__main__":
#     generateStats()

# if __name__ == "__main__":
#     generateStats()

    # <a href="/player/index?game_sport_year_ctl_id=13430&amp;stats_player_seq=1648871">Cooper, Mikayla</a>
    # print(firstTable.get("href"))
