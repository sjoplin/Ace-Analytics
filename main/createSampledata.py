# Import all libraries needed for the tutorial
import pandas as pd
import requests
from bs4 import BeautifulSoup
from makePDFs import printPDFs


#parses the rawtext into panda format
def generateStats(playerdata):

    #Keys of all potential outcomes, directions and trajectory.
    #Basically looking for these words in the rawtext

    potOutcome = ["grounded", "flied", "lined", "double", "popped", "singled",
                  "doubled", "tripled", "homered"]
    direction = ['p', '3b.', 'catcher', 'shortstop', 'pitcher', '1b', 'first',
                 '2b', 'c', 'second', '3b', 'third', 'ss',
                 'lf', 'left', 'cf', 'center', 'rf', 'right', 'middle', 'short']
    # trajectory = ['grounded', 'flied', 'lined']

    #arrays for various categories
    names = [];
    results = [];
    area = [];
    # traj = [];

    #reading the raw data
    f = open('./../interdata/scraperaw.txt')
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

        # newlines = []
        # for each in words:
        #     newlines.append(each.strip('.\n'))
        # words = newlines


        #marker to see if the player name has been added to the array
        num1 = 0

        #loop through every word and find the words that match the ones in the
        #keys
        #
        #

        # print(words)
        # names.append(words[0].strip(',').lower())

        if ('bunt' in words):
            dirFlag = True
            names.append(words[0].lower())
            results.append('bunt')
            for each in words:
                # print(each)
                # if (each == 'through'):
                #     for other in words:
                #         if (other in direction):
                #             # print('inside')
                #             area.append('through ' + other)
                # else:
                #     if (dirFlag):
                #         if (each in direction):
                #             area.append(each)
                #             dirFlag = False
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
                    # if resFlag:
                        # print('test')
                    # names.append(words[0].lower())
                    # results.append(each)
                    # resFlag = False
            # print(each)

                    for each in words:

                        if dirFlag and resFlag:
                            if ('center' in words):
                                for other in words:
                                    if (other in direction) and (other != 'center'):
                                        # print('inside')
                                        if (other == 'rf' or other == 'right' or other == 'left' or other == 'lf'):
                                            area.append(other + ' center')
                                            dirFlag = False
                                            names.append(words[0].lower())
                                            results.append(result)
                                            resFlag = False

                            if (each == 'down'):
                                for each in words:
                                    if each in direction:
                                        area.append('down ' + each)
                                        dirFlag = False
                                        names.append(words[0].lower())
                                        results.append(result)
                                        resFlag = False

                            if (each == 'through'):
                                for other in words:
                                    if (other in direction):
                                        # print('inside')
                                        if (other == 'rf' or other == 'right' or other == 'left' or other == 'lf'):
                                            area.append('through ' + other)
                                            dirFlag = False
                                            names.append(words[0].lower())
                                            results.append(result)
                                            resFlag = False

                            else:
                                if (dirFlag):
                                    if (each in direction):
                                        area.append(each)
                                        dirFlag = False
                                        names.append(words[0].lower())
                                        results.append(result)
                                        resFlag = False




        # for each in words:

        #     #if the word exists in the potOutcomes then add the name to the
        #     #names, result and direction arrays
        #     if (each in potOutcome):

        #         #checks to see if the playername has been added
        #         if (num1 == 0):
        #             nextName = words[0].lower()
        #             if nextName[1] == '.' or len(nextName) < 2:
        #                 nextName = nextName + ' ' + words[1].lower()
        #                 print(nextName[1])

        #             #adds player name and result
        #             names.append(nextName)

        #             results.append(each.lower())
        #             num1 = 1

        #             #marker to see if direction was added
        #             num = 0;

        #             newlines = []
        #             for each in words:
        #                 newlines.append(each.strip(','))
        #             words = newlines

        #             newlines = []
        #             for each in words:
        #                 newlines.append(each.strip('.\n'))
        #             words = newlines

        #             for each in words:

        #                 flag = False

        #                 #checks to see if the keyword "down" is in the direction
        #                 if (each == 'down'):
        #                     flag = True

        #                 if (num == 0):

        #                     if (each in direction or each == "down"):
        #                         if (flag == True):
        #                             temp = 'down '

        #                         if (num == 0):

        #                             #adds the direction "down" + direction or
        #                             #just the dierection depending on the
        #                             #keyword
        #                             if each != 'down':
        #                                 if (each == 'rf' or each == 'right' or each == 'left' or each == 'lf'):
        #                                     area.append(temp + each.lower())
        #                                 else:
        #                                     area.append(each.lower())

        #                                 num = 1
        #                                 temp = ''


        line = f.readline()

    f.close()

    s = pd.Series(names)
    p = pd.Series(results)
    a = pd.Series(area)
    data = pd.DataFrame({'Names': s, 'Results': p, 'Area': a})
    pd.set_option('display.max_rows', 220)
    print(data)
    # TODO: uncomment
    printPDFs(data, playerdata)


def getPlayerStats(teamname, url):
    quote_page = url
    # query the website and return the html to the variable page
    hdr = {
        'Moneyball': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    session = requests.Session()
    req = session.get(quote_page, headers=hdr)
    soup = BeautifulSoup(req.content, 'html.parser')
    name_box = soup.findAll('td', attrs={'colspan': '26'})
    firstTeam = "".join(((str(name_box))[18:18 + len(teamname)]).split())
    secondTeam = "".join(((str(name_box))[-7 - len(teamname):-7]).split())
    player_names = soup.findAll('td', attrs={'width': '20%'})
    playerurls = []
    for player in player_names:
        playerStr = str(player)
        if playerStr[17:19] == "<a" and playerStr[26:29] == "/pl":
            playerurls.append(playerStr[26:97])
    # if teamname == firstTeam:
    alltable = soup.findAll('table', attrs={'class': 'mytable'})

    if firstTeam == "".join(teamname.split()):
        correctTable = str(alltable[1])
    else:
        correctTable = str(alltable[2])

    playerMainUrls = []
    playerMainNames = []
    for i in range(len(correctTable) - 5):
        if correctTable[i:i + 4] == 'href':
            playerMainUrls.append("".join(correctTable[i + 7:i + 77]))
            everythingname = ("".join(correctTable[i + 79:i + 108]))
            splitname = everythingname.split(',')
            playerMainNames.append(splitname[0])

    allStatsForEveryone = []
    j = 0
    for player in playerMainUrls:
        quote_page2 = 'http://stats.ncaa.org/' + player
        hdr = {
            'Moneyball': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        session = requests.Session()
        req = session.get(quote_page2, headers=hdr)
        soup2 = BeautifulSoup(req.content, 'html.parser')
        dataFields = soup2.findAll('tr', attrs={'class': 'text'})
        dataStr = str(dataFields[len(dataFields) - 1])

        stats = []
        for k in range(len(dataStr) - 8):
            if dataStr[k:k + 5] == '<div>':
                stats.append("".join(dataStr[k + 25:k + 40].split()))
        listOfStats = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 18, 23, 24]
        # length 14 becasue counting stinks
        statNames = ['BA', 'OBPct', 'SLGPct', 'AB', 'H', '2B', '3B', 'HR', 'BB', 'SF', 'SH', 'K', 'SB', 'CS']
        finalStats = []
        for jk in range(len(stats)):
            if jk in listOfStats:
                toAdd = stats[jk]
                if len(toAdd) < 6:
                    finalStats.append(toAdd)
                else:
                    finalStats.append('0')
        j += 1
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
    pnames = pd.Series(playerMainNames)
    sdata = pd.Series(allStatsForEveryone)
    data = pd.DataFrame({'Names': pnames, 'Stats': sdata})
    return (data)

# if __name__ == "__main__":
#     generateStats()

    # <a href="/player/index?game_sport_year_ctl_id=13430&amp;stats_player_seq=1648871">Cooper, Mikayla</a>
    # print(firstTable.get("href"))
