#! python3

import requests
import bs4
import math
import os
import pyperclip
     
animePageLink = '';
animePageLink = "http://ww2.chia-anime.tv/episode/91-days/";
#animePageLink = input("1. Go to chia-anime.tv.\n2. Enter any anime's main page link : ")

episodeLinks = []
finalPages = []
downloadLinks = []

# this right here is for pages when we get a 404 not found error, 522 server error, etc.
# it'll just store links to those episodes and present in the end.
failedPages = []

animePageBS4 = requests.get(animePageLink, timeout=None)
try:
	animePageBS4.raise_for_status()
except Exception as exc:
	print('%s' %(exc))





animePageClass = bs4.BeautifulSoup(animePageBS4.text, "html.parser")
animePageEPS = animePageClass.select('#countrydivcontainer div .post div a')
for i in range(len(animePageEPS)):
    episodeLinks.append(animePageEPS[i].attrs['href'])





for i in range(len(episodeLinks)):
    percentageDone = i/len(episodeLinks);
    
    watchPage = requests.get(episodeLinks[i],timeout=(30, 30));
    try:
                watchPage.raise_for_status()
    except Exception as exc:
                failedPages.append(episodeLinks[i]);
            
    watchPageClass = bs4.BeautifulSoup(watchPage.text, "html.parser")
    finalPage = watchPageClass.select('#video-content #download')
    if len(finalPage) >= 1:
            finalPages.append(finalPage[0].attrs['href'])



for i in range(len(finalPages)):
    percentageDone = i/len(finalPages);
    dP = requests.get(finalPages[i],timeout=None);
    try:
                dP.raise_for_status()
    except Exception as exc:
                failedPages.append(finalPages[i])
    dPclass = bs4.BeautifulSoup(dP.text, "html.parser")
    links = dPclass.select('td .bttn');

    finalLink = "";
    for r in range(len(links)):
        if links[r].getText() == 'Server Zero':
            finalLink = links[r].attrs['href']

    if len(finalLink) >= 1:
            downloadLinks.append(finalLink);


if len(failedPages) > 0:
        print('check for these manually : ');
        for i in range(len(failedPages)):
                print(failedPages[i]);

pyperclip.copy('\n'.join(downloadLinks));

print('\n\nENJOY : \n\n');

for i in range(len(downloadLinks)):
    print(downloadLinks[i])

print('\n\nLinks copied to clipboard\n');
os.system('pause');
