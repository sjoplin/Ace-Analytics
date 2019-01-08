# import libraries
import requests
from bs4 import BeautifulSoup
from createSampledata import generateStats, getPlayerStats


# specify the url

def main():
    # list_urls = ['4580415', '4577144', '4577145', '4576367', '4572959', '4571240', '4570564', '4568118', '4564636', '4564039']
    # scrape('Georgia Tech', list_urls)
    singleurlscrape('Florida St.', 'http://stats.ncaa.org/teams/312381')


def scrape(data, teamName, list_urls):
    fullText = ''

    for url in list_urls:
        quote_page = url
        # query the website and return the html to the variable page
        hdr = {
            'Moneyball': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        session = requests.Session()
        req = session.get(quote_page, headers=hdr)
        # page = urllib2.urlopen(req)

        # parse the html using beautiful soup and store in variable soup
        # this is the html code of the website
        soup = BeautifulSoup(req.content, 'html.parser')

        # getting the first instance of a school name (the away team)
        school_box = soup.find('td', attrs={'class': 'boldtext', 'width': '40%'})
        # only the name of the school, none of the tags
        awayTeam = str(school_box)[48:-5]
        awayTeam = "".join(awayTeam.split())
        teamName = "".join(teamName.split())
        # print(awayTeam + ' == ' + teamName + ':  ' +str(awayTeam == teamName))
        if awayTeam == teamName:
            homeOAway = 3
        else:
            homeOAway = 1
        # getting all of the boxes that contain the play by play score
        all_boxes = soup.findAll('td', attrs={'class': 'smtext'})

        for name_box in all_boxes:
            if homeOAway % 3 is 0:
                nextText = str(name_box)[19:]
                if nextText[0] is not '<' and nextText[5] is not '=':
                    fullText = fullText + nextText[:-5] + '\n'
            homeOAway += 1

    f = open("./../interdata/scraperaw.txt", "w+")
    for line in fullText:
        f.write(line)
    f.close()
    generateStats(data)


def singleurlscrape(teamName, teamhomepage):
    quote_page = teamhomepage
    hdr = {
        'Moneyball': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    session = requests.Session()
    req = session.get(quote_page, headers=hdr)
    soup = BeautifulSoup(req.content, 'html.parser')
    all_boxes = soup.findAll('a', attrs={'class': 'skipMask', 'target': 'TEAM_WIN'})
    # print(all_boxes)
    fullURLExt = []
    numGames = 0

    for name_box in all_boxes:
        numGames += 1
        nextText = str(name_box)

        nextText = (nextText[26:-32])[0:31]
        if "".join(nextText[-1]) is '"':
            fullURLExt.append("".join(nextText[:-1]))
        else:
            fullURLExt.append("".join(nextText))
    finalURLS = []

    for i in range(10):
        finalURLS.append(getFinalURL('http://stats.ncaa.org' + (str(fullURLExt[numGames - i - 1]))[:]))
    data = getPlayerStats(teamName, 'http://stats.ncaa.org' + (str(fullURLExt[-1])))
    scrape(data, teamName, finalURLS)


def getFinalURL(gameurl):
    quote_page = gameurl
    hdr = {
        'Moneyball': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    session = requests.Session()
    req = session.get(quote_page, headers=hdr)
    soup = BeautifulSoup(req.content, 'html.parser')
    urlend = soup.findAll('ul', attrs={'class': 'level1'})
    urlend = (str(urlend)[134:-233])
    return ('http://stats.ncaa.org' + urlend)


if __name__ == "__main__":
    main()
