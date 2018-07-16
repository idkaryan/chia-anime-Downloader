# chia-anime-Downloader
Ever wanted all the episode download links straight to your screen or clipboard? Well, this is it.

# Steps to set up chia-anime-downloader:

1. install scrapy
```
pip install Scrapy
```
or (preferable on a Windows machine after [installing Anaconda](https://conda.io/docs/user-guide/install/windows.html))
```
conda install -c conda-forge scrapy
```


2. install docker and splash

installing splash through docker is the easiest way, so install docker first

after docker is installed, command for installing splash
```
$ docker pull scrapinghub/splash
```
command for setting it up 
```
$ docker run -p 5023:5023 -p 8050:8050 -p 8051:8051 scrapinghub/splash
```
note that you may need to start docker and use this command everytime you're using chia-anime-downloader
it sets up the localhost and allows for scraping javascript based websites



3. install scrapy_splash using the environment where you installed scrapy
```
pip install scrapy-splash
```


4. go to http://www.chia-anime.tv/index/


5. click on any anime's main page link
 
 
6. copy the address


7. run the terminal, go to the project directory and use command
```
scrapy crawl epbot -a aL="http://www.chia-anime.tv/episode/91-days/"
```
replacing http://www.chia-anime.tv/episode/91-days/ with whatever address you copied





* Steps for the older version which stopped working when chia-anime.tv started using video hosts which loaded the links dynamically using javascript. 

 1. go to http://www.chia-anime.tv/index/
 
 2. click on any anime's main page link
 
 ![step 2](http://i.imgur.com/ivSMchY.jpg)
 
 3. copy the address
 
 ![step 3](http://i.imgur.com/X7nXbwa.jpg)
 
 4. paste it into the script when asked
 
 ![step 4](http://i.imgur.com/1dRsyHs.jpg)
 
 5. press enter and wait while it fetches all links :)
 
 ![step 5](http://i.imgur.com/ZJphTjQ.jpg)


# External dependencies(for devs) : 
  - requests
  - BeautifulSoup4
  - pyperclip

```
$ pip install beautifulsoup4
$ pip install requests
$ pip install pyperclip
```
