import json
import requests
import pandas as pd
import csv

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

# START PAGE
page = 0 #INDEX 0 for first page due to loop iteration

#number article
article_nr = page

# HOW MANY TOTAL PAGES 
pages = 10

# HOW MANY ARTICLES PER PAGE (Maximum of 10)
articles = 10



#------------------------------------Building the CSV FILE-----------------------------------------
# METHOD [https://www.codingem.com/python-write-to-csv-file/]

# Define the structure of the data
test_header = ['article_title', 'articule_snippet', 'html_snippet', 'url_link']

#SMR_header = ['article_title', 'article_publisher', 'article_langugage', 'article_date', 'event_date', 'event_location_province', 'event_location_sector___1', 'event_location_sector___2', 'event_location_sector___3', 'event_location_sector___4', 'event_location_sector___5', 'event_location_sector___6', 'event_location_sector___7', 'event_location_sector___8', 'event_location_sector___9', 'event_location_sector___10', 'event_location_sector___11', 'event_location_sector___12', 'event_location_sector___13', 'event_location_sector___14', 'event_location_sector___15', 'event_location_sector___16', 'event_location_sector___17', 'event_location_sector___18', 'event_location_sector___19', 'event_location_sector___20', 'event_location_sector___21', 'event_location_sector___22', 'event_location_sector___23', 'event_location_sector___24', 'event_location_sector___25', 'event_location_sector___26', 'event_location_sector___27', 'event_location_sector___28', 'event_location_sector___29', 'event_location_sector___30', 'event_location_sector___31', 'event_location_sector___32', 'event_mechanism	event_mechanism_rta_vehicles___1', 'event_mechanism_rta_vehicles___2', 'event_mechanism_rta_vehicles___3', 'event_mechanism_rta_vehicles___4', 'event_mechanism_rta_vehicles___5', 'event_mechanism_rta_vehicles___6', 'event_mechanism_rta_vehicles___7', 'event_mechanism_rta_vehicles_other', 'event_mechanism_rta_mechanism', 'event_mechanism_rta_mechanism_other', 'event_mechanism_natural', 'event_mechanism_natural_other', 'event_mechanism_manmade', 'event_mechanism_manmade_other', 'event_victims', 'event_casualties', 'event_demography', 'systematic_media_review_complete']

# 1. Open a new CSV file
with open('test_data_1.csv', 'w', encoding="UTF8") as file:
    # 2. Create a CSV writer
    writer = csv.writer(file)

    # 3. Write data to the file
    writer.writerow(test_header)
    




#------------------------------------LOOP to buiild db with info from google api-----------------------------------------

    for page in range(pages):
        
        page+=1

        # constructing the URL
        # doc: https://developers.google.com/custom-search/v1/using_rest
        # calculating start, (page=2) => (start=11), (page=3) => (start=21) 

        # pages
        start = (page - 1) * articles + 1
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
        for i, search_item in enumerate(search_items, start):
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
            
            article_nr+=1
            
            print("="*10, f"Result #{article_nr}", "="*10)
            print("Title:", title)
            #print("Description:", snippet)
            print("Long description:", long_description)
            #print("URL:", link, "\n")
            
            writer.writerow([title, snippet, html_snippet, link])





















#--------------------------------------------------------------------------

#METHOD: https://www.youtube.com/watch?v=ewPJs4N8d8M&ab_channel=Roshan

# key = "AIzaSyCXVQGXI-YUWlCXcLbhZk-zv0zuxlgqBUE"
# cx = "f142e568df70f4f3f"

# url = "https://www.googleapis.com/customsearch/v1"

# parameters = {"q": "“Rwanda” AND “(shoot OR machete OR stab OR explosion OR detonation OR weapon)” AND “(dead OR death OR fatal OR injury OR wound OR trauma OR kill)” 2010..2020",
#               "cx": cx,
#               "key": key,
#               }

# page = requests.request("GET", url, params=parameters)

# results = json.loads(page.text)

# results.keys()

# #print(results["queries"])

# #print(results["items"][0])

# def process_search(results):
#     link_list = [item["link"] for item in results["items"]]
#     df = pd.DataFrame(link_list, columns=["link"])
#     df["title"] = [item["title"] for item in results["items"]]
#     df["snippet"] = [item["snippet"] for item in results["items"]]
#     return df
# df = process_search(results)

# next_index = results["queries"]["nextPage"][0]["startIndex"]
# search_terms = results["queries"]["nextPage"][0]["searchTerms"]

# url = "https://www.googleapis.com/customsearch/v1"
# parameters = {"q": search_terms,
#               "cx": cx,
#               "key": key,
#               "start": next_index
#               }

# page = requests.request("GET", url, params=parameters)
# results = json.loads(page.text)

# def process_search(results):
#     link_list = [item["link"] for item in results["items"]]
#     df = pd.DataFrame(link_list, columns=["link"])
#     df["title"] = [item["title"] for item in results["items"]]
#     df["snippet"] = [item["snippet"] for item in results["items"]]
#     return df
# temp_df = process_search(results)
# df = pd.concat([df, temp_df], ignore_index=True)

# print(df)