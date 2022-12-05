import json
from unittest import result
import requests
import pandas as pd
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import nltk
from newspaper import Article



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


## METHOD - [https://www.thepythoncode.com/article/use-google-custom-search-engine-api-in-python]


#------------------------------------Defining GCE (Google custom search engine) parametres-----------------------------------------
# get the API KEY here: https://developers.google.com/custom-search/v1/overview
## These are profile specifik and you need to get your own to do the costume search (not hard, just search google if you're unsure)
API_KEY = "AIzaSyCXVQGXI-YUWlCXcLbhZk-zv0zuxlgqBUE"

# get your Search Engine ID on your CSE control panel (from same place as the API_KEY)
SEARCH_ENGINE_ID = "f142e568df70f4f3f"



#------------------------------------Defining SEARCH OPTIONS-----------------------------------------
# the search query we want
query = "“Rwanda” AND “(shoot OR machete OR stab OR explosion OR detonation OR weapon)” AND “(dead OR death OR fatal OR injury OR wound OR trauma OR kill)” 2010..2020"

# Define the structure of the data
#test_header = ['full text']

# 1. Open a new CSV file
with open('full_text_test.csv', 'w', encoding="UTF8") as file:
    # 2. Create a CSV writer
    writer = csv.writer(file)

    # 3. Write data to the file
    #writer.writerow(test_header)

    # constructing the URL
    # doc: https://developers.google.com/custom-search/v1/using_rest
    # calculating start, (page=2) => (start=11), (page=3) => (start=21) 
    
    start = 1

    #print(start)
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

    ## Making the API request and using the requests' json() method to automatically parse the returned JSON data to a Python dictionary:

    # make the API request
    data = requests.get(url).json()

    ## Now, this data is a dictionary containing many result tags. We are only interested in "items", which are the search results. 
    ## By default, CSE will return ten search results. Let's iterate over them:

    # get the result items
    search_items = data.get("items")

    # iterate results found per page
        
    search_item = search_items[0]
    
    try:
        long_description = search_item["pagemap"]["metatags"][0]["og:description"]
    except KeyError:
        long_description = "N/A"
    # get the page title
    title = search_item.get("title")
    # page snippet
    snippet = search_item.get("snippet")
    # alternatively, you can get the HTML snippet (bolded keywords)
    html_snippet = search_item.get("htmlSnippet")
    # extract the page url
    link = search_item.get("link")
    # print the results
            
    driver.get(link)
    
    page_soup = BeautifulSoup(driver.page_source, 'lxml') #'html.parser'?        
    
    print("="*10, f"Result", "="*10)
    print("Title:", title)
    
    #full_article_text = page_soup.get_text()
    #full_article_text = page_soup.find_all(itemprop="text")
    #full_article_text = page_soup.find_all('p')[0].get_text()
    #full_article_text = page_soup.find_all('p') # may work as of now
    
    
    #for i in page_soup.get_text():
    #    full_article_text = page_soup.select("body div p")[i].get_text()
    
    #full_article_text = page_soup.select("body div p")
    #full_article_text # list of elements
    #full_article_text = page_soup.findAll(text=True)
    
    # >>> txt = """\
    # ... <p>Red</p>
    # ... <p><i>Blue</i></p>
    # ... <p>Yellow</p>
    # ... <p>Light <b>green</b></p>
    # ... """
    # >>> import BeautifulSoup
    # >>> BeautifulSoup.__version__
    # '3.0.7a'
    # >>> soup = BeautifulSoup.BeautifulSoup(txt)
    # >>> for node in soup.findAll('p'):
    # ...     print ''.join(node.findAll(text=True))
    
    #txt = ""
    
    # for node in page_soup.findAll('p'):
    #     #print(''.join(node.findAll(text=True)))
    #     full_article_text.join(node.findAll(text=True))
    
    p_tags = page_soup.select("body div p")
    
    #print(p_tags)
    
    full_article_text = ""
    
    #https://oxylabs.io/blog/news-scraping
    
    for each in p_tags: 
        full_article_text += str(each.get_text()) + "\n" # concatenate 
        
    #FOLLOW WITH NEWSPAPER OR NEWSPAPER3K TO REMOVE COOKIES TEXT ETC?
    
    # article = Article(full_article_text)
    # article = Article(url)
    # article.download()
    # article.parse()
    # nltk.download('punkt')
    # article.nlp()
    
    # article.authors
    # article.publish_date
    # print(article.text)
        
    
    writer.writerow(["full body text"])
    
    writer.writerow([full_article_text])

    print("URL:", link, "\n")
    
    
    
    
    
    #within html -> within body (as deep as you can go) ---- [html body p] or [body p]

    
    
    










