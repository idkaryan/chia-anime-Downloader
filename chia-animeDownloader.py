#! python3

import requests
import bs4
import math
import os
import pyperclip

     
animePageLink = '';

animePageLink = input("1. Go to chia-anime.tv.\n2. Enter any anime's main page link : ")

episodeLinks = []
finalPages = []
downloadLinks = []
failedPages = []
hashCount = 0 
                
def hashUpdate(percent):
        global hashCount;
        hashTotal = math.ceil(percent * 20);
        while(hashTotal >= hashCount and hashCount < 20):
                hashCount = hashCount + 1;
                print('#',end="");



print('\n');

print('Getting links for : %s' %(animePageLink));
print('\n');
print('Initiating chiaDownloader : [ #################### ]');   
print('Initiating PHASE 1        : [ ',end="");

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
    hashUpdate(percentageDone);
    
    watchPage = requests.get(episodeLinks[i],timeout=(30, 30));
    try:
                watchPage.raise_for_status()
    except Exception as exc:
                failedPages.append(episodeLinks[i]);
            
    watchPageClass = bs4.BeautifulSoup(watchPage.text, "html.parser")
    finalPage = watchPageClass.select('#video-content #download')
    if len(finalPage) >= 1:
            finalPages.append(finalPage[0].attrs['href'])
    

print(' ]\n\n- PHASE 1 COMPLETED -\n\n');
print('Initiating PHASE 2        : [ ',end="");
hashCount = 0;

for i in range(len(finalPages)):
    percentageDone = i/len(finalPages);
    hashUpdate(percentageDone);
    dP = requests.get(finalPages[i],timeout=None);
    try:
                dP.raise_for_status()
    except Exception as exc:
                failedPages.append(finalPages[i])
    dPclass = bs4.BeautifulSoup(dP.text, "html.parser")
    links = dPclass.select('td .bttn');

    for r in range(len(links)):
        if links[r].getText() == 'Server Zero':
            finalLink = links[r].attrs['href']

    if len(finalLink) >= 1:
            downloadLinks.append(finalLink);

print(' ]\n\n- PHASE 2 COMPLETED -\n\n');
print('No of failed pages : ', len(failedPages));
print('\n')
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
