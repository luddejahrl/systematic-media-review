import json
import requests
import csv
from newspaper import Article

#------------------------------------Defining GCE (Google custom search engine) parametres-----------------------------------------
# get the API KEY here: https://developers.google.com/custom-search/v1/overview
# These are profile specifik and you need to get your own to do the costume search (not hard, just search google if you're unsure)
API_KEY = "AIzaSyCXVQGXI-YUWlCXcLbhZk-zv0zuxlgqBUE"

# get your Search Engine ID on your CSE control panel (from same place as the API_KEY)
SEARCH_ENGINE_ID = "f142e568df70f4f3f"

# only query news sites
type = "nws"

# QUERY PARAMETRES
#https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list#request

#------------------------------------Defining SEARCH OPTIONS-----------------------------------------
# the search query we want
query = "“Rwanda” AND “(shoot OR machete OR stab OR explosion OR detonation OR weapon)” AND “(dead OR death OR fatal OR injury OR wound OR trauma OR kill)” 2010..2020"

excludeTerms = "wikipedia, cdc, featureshoot"


#https://www.google.com/search?q=%E2%80%9CRwanda%E2%80%9D+AND+%E2%80%9C(shoot+OR+machete+OR+stab+OR+explosion+OR+detonation+OR+weapon)%E2%80%9D+AND+%E2%80%9C(dead+OR+death+OR+fatal+OR+injury+OR+wound+OR+trauma+OR+kill)%E2%80%9D+2010..2020%22&newwindow=1&rlz=1C5CHFA_enSE963SE963&sxsrf=ALiCzsYjFs6WkVvxqOTvekb3fYt4DCaXAg:1665497405281&source=lnms&tbm=nws&sa=X&ved=2ahUKEwi86Nyprdj6AhVCx4sKHaC_C_oQ_AUoAnoECAEQBA&biw=1440&bih=789&dpr=2
# START PAGE
page = 0 #INDEX 0 for first page due to loop iteration

# HOW MANY TOTAL PAGES 
pages = 11

#https://blog.expertrec.com/google-custom-search-limit-results-2/

# HOW MANY ARTICLES PER PAGE (Maximum of 10)
articles = 10

#number article
article_nr = page

# Define the structure of the data
test_header = ['article_title', 'full text', 'url_link']

# 1. Open a new CSV file
with open('test_data_100pages.csv', 'w', encoding="UTF8") as file:
    # 2. Create a CSV writer
    writer = csv.writer(file)

    # 3. Write data to the file
    writer.writerow(test_header)


#------------------------------------LOOP to buiild database with info from google api-----------------------------------------
    #change to have the same format as the inner for loop with enumarate
    for page in range(pages):
        
        
        page+=1

        # constructing the URL
        # doc: https://developers.google.com/custom-search/v1/using_rest

        # pages
        start = (page - 1) * articles + 1
        
        #print(start)
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&tbm={type}&excludeTerms={excludeTerms}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

        ## Making the API request and using requests' json() method to automatically parse the returned JSON data to a Python dictionary:

        # make the API request
        data = requests.get(url).json()

        ## Now, this data is a dictionary containing many result tags. We are only interested in "items", which are the search results. 
        ## By default, CSE will return ten search results. Let's iterate over them:

        # get the result items
        search_items = data.get("items")

        # iterate results found per page
        for i, search_item in enumerate(search_items, start) or []:
            try:
                long_description = search_item["pagemap"]["metatags"][0]["og:description"]
            except KeyError:
                long_description = "N/A"
                
            # get the page title
            title = search_item.get("title")
            # extract the page url
            link = search_item.get("link")
            # snippet from article
            snippet = search_item.get("snippet")     
  
            article = Article(link)

            article.download()
            
            try:
                article.parse() 
                article.nlp()
                #temp = article.text
                
                title = article.title
                link = article.url
                #authors = article.authors
                #date = article.publish_date
                #image = article.top_image
                #summary = article.summary
                text = article.text 
                
                #writer.writerow([title, page_soup.get_text(), link])
                #writer.writerow([title, temp, link])
                writer.writerow([title, text, link])
            except :
                pass

            article_nr+=1
            
            print("="*10, f"Result #{article_nr}", "="*10)
            # print("Title:", title)
            
            # print(snippet)

            # print("URL:", link, "\n")










