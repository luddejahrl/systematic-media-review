## Google search implementation
from pickle import NONE
import pandas as pd
import json
import requests
import csv
import openpyxl #import read_excel
import nltk
from newspaper import Article
import numpy as np

#------------------------------------Defining GCE (Google custom search engine) parametres-----------------------------------------
# get the API KEY here: https://developers.google.com/custom-search/v1/overview
## These are profile specifik and you need to get your own to do the costume search (not hard, just search google if you're unsure)
API_KEY = "AIzaSyCXVQGXI-YUWlCXcLbhZk-zv0zuxlgqBUE"

# get your Search Engine ID on your CSE control panel (from same place as the API_KEY)
SEARCH_ENGINE_ID = "f142e568df70f4f3f"

page = 0 #INDEX 0 (becomes one) for first page due to loop iteration

# HOW MANY TOTAL PAGES 
pages = 1

# HOW MANY ARTICLES PER PAGE (Maximum of 10)
articles = 10

#number article
article_nr = page

#start
start = page

#excludeTerms = "wikipedia, cdc, featureshoot"


#------------------------------------/Defining GCE (Google custom search engine) parametres-----------------------------------------

file_loc = '/Users/luddejahrl/Desktop/Systematic_media_review/Finding_and_extracting_old_news/Data_initial_SMR.xlsx'

query = ""

country_string = '"Rwanda"'

# load excel with its path
wrkbk = openpyxl.load_workbook(file_loc)

sh = wrkbk.active        

#ITERATE THROUGH THE EXCEL FILE TO GET THE ARTICLES FOR THE HEADLINES
for row in sh.iter_rows(min_row=2, min_col=1, max_row=257, max_col=4):
    
    #INCLUDE PUBLISHER?
    query = country_string + " " + str(row[0].value) + " " + str(row[1].value) + " 2010..2020"
    
    #print(query)
        
    start = (page - 1) * articles + 1
    
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

    # make the API request
    data = requests.get(url).json()
    
    # get the result items
    search_items = data.get("items")
    
    #ITERATE THROUGH THE RESULTS OF THE PAGE 
    for i, search_item in enumerate(search_items, start) or []:
        try:
            long_description = search_item["pagemap"]["metatags"][0]["og:description"]
        except KeyError:
                long_description = "N/A"
    
        # get the page title
        title = search_item.get("title")
        
        # extract the page url
        link = search_item.get("link")

        #check parametres if they are the same article else pass along
        #if (title is close enough) - if (publish date is the same)
        if ():
            #-----Newspaper3k--------
            article = Article(link)

            article.download()
            
            try:
                article.parse() 
                article.nlp()
                
                title = article.title
                link = article.url
                text = article.text 
            except :
                pass
        else:
            pass
            
        
    
    

#------------------------------------Defining SEARCH -----------------------------------------
