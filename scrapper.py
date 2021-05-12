from bs4 import BeautifulSoup
import requests,csv
from selenium import webdriver

browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars')

headers = ["name","radius","mass","distance"]
star_data = []

page = requests.get('https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars')
soup = BeautifulSoup(browser.page_source, "html.parser")

def scrape():
    for table_tag in soup.find_all('table', attrs={'class','wikitable sortable jquery-tablesorter'}):
        for table_body_tag in table_tag.find_all("tbody"):
            temp_list = []
            tr_tags = table_body_tag.find_all("tr")
            for index,tr_tag in enumerate(tr_tags):
                if index == 1:
                    temp_list.append(tr_tag.find_all("a")[0]).contents[0]
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except Exception as e:
                        print(e)
                        temp_list.append("")
            star_data.append(temp_list)


with open("C-127_project/star_data.csv","a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(star_data)
    print("Done!")