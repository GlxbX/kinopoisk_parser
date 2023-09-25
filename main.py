from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent

import json 
import time

from bs4 import BeautifulSoup as bs

class Parser:
    def __init__(self, headless=False):

        #options
        options = webdriver.ChromeOptions()

        ua = UserAgent()
        user_agent = ua.random

        options.add_argument(f"user-agent={user_agent}")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-gpu")
        options.add_argument("--mute-audio")
        options.add_argument("--no-sandbox")
    
        if headless:
            options.add_argument("headless")

        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('useAutomationExtension', False)
  
        #driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        
    def parse_top_1000(self):
        data = {}
        c = 1
        for page in range(1,21):
            self.driver.get(f"https://www.kinopoisk.ru/lists/movies/top_1000/?page={page}")
            WebDriverWait(self.driver, 100,0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "styles_mainTitle__IFQyZ.styles_activeMovieTittle__kJdJj")))
            
            source_data = self.driver.page_source
            soup = bs(source_data, "lxml")

            movie_divs = soup.find_all("div", class_ = "styles_root__ti07r")

            for div in movie_divs:
    
                movie_data ={}

                movie_data["name"] = div.find("span", class_ = "styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj").text

                rt = div.find_all("div", class_ ="styles_kinopoiskValueBlock__qhRaI")
                if len(rt)!=0:
                    movie_data["rating"] = float(rt[0].text)
                else:
                    movie_data["rating"] = "No rating yet"
                
                movie_data["year"] = div.find("span", class_ = "desktop-list-main-info_secondaryText__M_aus").text[2:6]

             
                country_producer = div.find("span", class_ = "desktop-list-main-info_truncatedText__IMQRP").text
                movie_data["country"] = country_producer.split("•")[0][:-1]
                movie_data["producer"] = country_producer.split(":")[-1][1:]

                a = div.find_all("a", class_ = "style_button__PNtXT style_buttonSize24__efn1J style_buttonPlus__TjQez style_buttonLight____6ma style_withIconLeft___Myt9")
                if len(a)!=0:
                    movie_data["available on kinopoisk"] = True 
                else:
                    movie_data["available on kinopoisk"] = False 
                    
                data[c]=movie_data
                c+=1
        with open("top1000.json", "w", encoding='utf-8') as outfile:
            json.dump(data,outfile,ensure_ascii=False)


def main():
    start_time = time.time()

    parser = Parser(headless=True)
    parser.parse_top_1000()

    print(f"Successfully parsed in {int(time.time()-start_time)} seconds")

if __name__ == "__main__":
    main()
