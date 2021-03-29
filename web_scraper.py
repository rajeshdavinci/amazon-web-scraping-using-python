import json
from bs4 import BeautifulSoup
from selenium import webdriver

def get_url(search_term):
    template = "https://www.amazon.com/s?k={}&ref=nb_sb_noss_1" 
    search_term = search_term.replace(' ', '+')
    url = template.format(search_term) 
    url += '&page{}'
    return url 
	

	
def extract_record(item):
    atag = item.h2.a 
    description = atag.text.strip()
    url = 'https://www.amazon.com' + atag.get('href')

    try:
        price_parent = item.find ('span','a-price')
        price = price_parent.find ('span','a-offscreen').text
    except:
        return

    except AttributeError:
        rating = ''
        review_count = ''

    result = [description, price, url]
    return result
  



def main(search_term):
    CHROMEDRIVER = "/usr/local/src/chromedriver"
    driver = webdriver.Chrome(CHROMEDRIVER)
   
    record = []
    record_result = 0
    url = get_url(search_term) 	
    driver.get(url) 
    driver.maximize_window()
    soup = BeautifulSoup(driver.page_source, 'html.parser') 
    results = soup.find_all('div', {'data-component-type': 's-search-result'})         
        
    for item in results:
        if record_result <= 2:
           record = extract_record(item)
           record_list = json.dumps(record)
           print(record_list)             
           record_result += 1

            
    driver.close()			

main('dell inspiron 3505')  