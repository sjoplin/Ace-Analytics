# import libraries
import urllib2
from bs4 import BeautifulSoup
import requests
# specify the url

def main():
    list_urls = ['4580415', '4577144', '4577145', '4576367', '4572959', '4571240', '4570564', '4568118', '4564636', '4564039']
    scrape('Georgia Tech', list_urls)

def scrape(teamName, list_urls):
    fullText = ''
    for url in list_urls:
        quote_page = 'http://stats.ncaa.org/game/play_by_play/' + url
        # query the website and return the html to the variable page
        hdr = { 'Moneyball' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36' }
        session = requests.Session()
        req = session.get(quote_page, headers=hdr)
        #page = urllib2.urlopen(req)

        # parse the html using beautiful soup and store in variable soup
        # this is the html code of the website
        soup = BeautifulSoup(req.content, 'html.parser')

        #getting the first instance of a school name (the away team)
        school_box = soup.find('td', attrs={'class': 'boldtext', 'width': '40%'})
        #only the name of the school, none of the tags
        awayTeam = str(school_box)[48:-5]
        if awayTeam is teamName:
            homeOAway = 3
        else:
            homeOAway = 1
        #getting all of the boxes that contain the play by play score
        all_boxes = soup.findAll('td', attrs={'class': 'smtext'})

        for name_box in all_boxes:
            if homeOAway % 3 is 0:
                nextText = str(name_box)[19:]
                if nextText[0] is not '<' and nextText[5] is not '=':
                    fullText = fullText + nextText[:-5] + '\n'
            homeOAway+=1


    f= open("./../interdata/scraperaw.txt","w+")
    for line in fullText:
        f.write(line)
    f.close()

if __name__ == "__main__":
    main()
