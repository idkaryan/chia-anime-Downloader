# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class EpbotSpider(scrapy.Spider):
    name = 'epbot'
    allowed_domains = ['chia-anime.tv', 'animepremium.tv']
    finalLinks = []
    animename = ""
    aL=""
    
    def start_requests(self):
        if(self.aL==""):
            print("anime webpage not defined.\ne.g Use argument 'scrapy crawl epbot -a aL='http://ww2.chia-anime.tv/episode/hajime-no-ippo/'")
            return
        
        self.animename = self.aL.split('/')[-2]
        if self.aL is not None:
            yield scrapy.Request(url=self.aL, callback=self.parse)
        pass
        
    def parse(self, response):
        epageLinks = response.xpath('//h3[@itemprop="episodeNumber"]/a/@href').extract()
        for link in epageLinks:
            yield response.follow(link, callback=self.dplinks)
        
        pass

#   get download page links
    def dplinks(self, response):
        downloadPageLink = response.xpath('//a[@id="download"]/@href').extract_first()
        yield (SplashRequest(url=downloadPageLink, callback=self.finallinks, args={ 'wait' : 2 }))
        pass

#   get final page links
    def finallinks(self, response):
        fLink = response.xpath('//a[@class="bttn green"]/@href').extract()
        fName = response.xpath('//span[@class="label label-default"]/font/text()').extract()
        if fLink is not "":
            print('Successfully got the link for : ' + fName[0])
            self.finalLinks.append(fLink[0])
            yield{'link' : fLink[0]}
            
            f = open(self.animename+'.txt', 'a')
            f.write(fLink[0] + '\n')
            f.close()
        else:
            print('Failed to get the link for : ' + fName[0])
        pass
    
    def closed(self, reason):
        if(self.aL == ""):
            return
        print("\nLinks saved : "+str(len(self.finalLinks)))
        print("Check " + self.animename + ".txt for direct links :)")
        pass
