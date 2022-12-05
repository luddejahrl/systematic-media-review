#from ast import keyword
import csv
from distutils import config
from duckduckgo_search import ddg
from duckduckgo_search import ddg_news
#import newspaper

## DUCKDUCKGO SEARCH QUERY 
# cats dogs     	        - Results about cats or dogs
# "cats and dogs"	        - Results for exact term "cats and dogs". If no results are found, related results are shown.
# cats -dogs	            - Fewer dogs in results
# cats +dogs    	        - More dogs in results
# cats filetype:pdf	        - PDFs about cats. Supported file types: pdf, doc(x), xls(x), ppt(x), html
# dogs site:example.com     - Pages about dogs from example.com
# cats -site:example.com	- Pages about cats, excluding example.com
# intitle:dogs	            - Page title includes the word "dogs"
# inurl:cats	            - Page url includes the word "cats"

# Boolean searches always get more complex than is usually needed, but DuckDuckGo offers full support 
# for AND/OR searches and parenthetical groupings. By default, all terms are combined 
# with AND (use double quotes to search for an exact phrase). Using AND or OR only affects 
# the words adjacent to the boolean, so markdown editor OR previewer searches for 
# ((markdown)AND((editor)OR(previewer)). As you can see from that example, typing out the full 
# boolean search version is far more cumbersome than just running the original search. 
# In most cases an OR search that doesn’t make sense in plain text is probably easiest as two 
# different searches. You can also combine phrases by using double quotes, e.g.
# "markdown previewer" OR "markdown editor".

#ORIGINAL QUERY:
# “Rwanda” 
# AND “(shoot OR machete OR stab OR explosion OR detonation OR weapon)” 
# AND “(dead OR death OR fatal OR injury OR wound OR trauma OR kill)” 2010..2020

# Create search querry
country = '"Rwanda"'

# List of injuries/cuases (mass-trauma causes)
keywords_list_1 = ['"shoot"', '"shooting"', 
'"machete"', 
'"stab"', '"stabbing"', '"stabbed"',
'"explosion"', '"exploaded"',
'"detonation"', '"detonated"',
'"weapon"', '"weapons"', '"gun"', '"guns"'
]

keywords_list_2 = [
'"dead"', '"deaseased"', '"deadly"', '"death"',
'"fatal"',
'"injury"', '"injur"', '"injured"', '"injurys"',
'"wound"', '"wounds"', '"wounded"', 
'"truamas"', '"truama"', 
'"kill"', '"killed"', '"kills"',
'"car crash"']

# keywords_list = ['"shoot"', '"shooting"', 
# '"machete"', 
# '"stab"', '"stabbing"', '"stabbed"',
# '"explosion"', '"exploaded"',
# '"detonation"', '"detonated"',
# '"weapon"', '"weapons"', '"gun"', '"guns"',
# '"dead"', '"deaseased"', '"deadly"', '"death"',
# '"fatal"',
# '"injury"', '"injur"', '"injured"', '"injurys"',
# '"wound"', '"wounds"', '"wounded"', 
# '"truamas"', '"truama"', 
# '"kill"', '"killed"', '"kills"',
# '"car crash"']

common_sites = []

# keywords_list = ["""shoot""", 
# """machete""",
# """stab""",
# """explosion""",
# """detonation""",
# """weapon""",
# """dead""",
# """death""",
# """fatal""",
# """injury""",
# """wound""",
# """trauma""",
# """kill"""]

site_suffix = "site:"

sites_list_rwanda_eng = [
"",
"newtimes.co.rw/",
"umuryango.rw/eng/",
"ktpress.rw/",
"rwandatoday.africa/",
"therwandan.com/",
"eng.inyarwanda.com/",
"en.igihe.com/",
"en.ukwezi.rw/",
"jambonews.net/en/"
]

sites_list_rwanda_fre = [
"lerwandais.com/",
"musabyimana.net/",
"radiomaria.rw/",
"rnanews.com/"]

sites_list_rwanda_other = [
"allafrica.com/",
"www.bbc.com/news/world/africa"
]

# LIST of NEWS sites for RWANDA
# https://www.w3newspapers.com/rwanda/

#ENGLISH originl
# new_times_paper = newspaper.build('https://www.newtimes.co.rw/', config=config, memoize_articles=False)
# umuryango_paper = newspaper.build('https://www.umuryango.rw/eng/', config=config, memoize_articles=False)
# ktpress_paper = newspaper.build('https://www.ktpress.rw/', config=config, memoize_articles=False)
# hose_paper = newspaper.build('https://hose.rw/', config=config, memoize_articles=False)
# rwandatoday_paper = newspaper.build('https://rwandatoday.africa/', config=config, memoize_articles=False)
# therwandan_paper = newspaper.build('https://www.therwandan.com/', config=config, memoize_articles=False)

# #ENGLISH translated
# inyarwanda_paper = newspaper.build('https://eng.inyarwanda.com/', config=config, memoize_articles=False)
# igihe_paper = newspaper.build('https://www.en.igihe.com/', config=config, memoize_articles=False)
# ukwezi_paper = newspaper.build('http://en.ukwezi.rw/', config=config, memoize_articles=False)
# jambonews_paper = newspaper.build('https://www.jambonews.net/en/', config=config, memoize_articles=False)

# #FRENCH
# lerwandais_paper = newspaper.build('https://www.lerwandais.com/', config=config, memoize_articles=False)
# musabyimana_paper = newspaper.build('http://www.musabyimana.net/', config=config, memoize_articles=False)
# radiomaria_paper = newspaper.build('https://www.radiomaria.rw/', config=config, memoize_articles=False)
# rnanews_paper = newspaper.build('http://www.rnanews.com/', config=config, memoize_articles=False)

# #RWANDAN translated
# inyarwanda_rw_paper = newspaper.build('https://inyarwanda.com/', config=config, memoize_articles=False)
# igihe_rw_paper = newspaper.build('https://www.igihe.com/', config=config, memoize_articles=False)
# ukwezi_rw_paper = newspaper.build('http://ukwezi.rw/', config=config, memoize_articles=False)
# jambonews_rw_paper = newspaper.build('https://www.jambonews.net/rw/', config=config, memoize_articles=False)

# #RWANDAN original
# umuseke_paper = newspaper.build('https://www.umuseke.rw/', config=config, memoize_articles=False) 
# kigalitoday_paper = newspaper.build('https://www.kigalitoday.com/', config=config, memoize_articles=False)
# imvahonshya_paper = newspaper.build('https://imvahonshya.co.rw/', config=config, memoize_articles=False)
# rwandaises_paper = newspaper.build('https://rwandaises.com/', config=config, memoize_articles=False)
# rugali_paper = newspaper.build('https://rugali.com/', config=config, memoize_articles=False)
# intyoza_paper = newspaper.build('https://www.intyoza.com/', config=config, memoize_articles=False)
# rba_paper = newspaper.build('https://www.rba.co.rw/', config=config, memoize_articles=False)

# #OTHER
# https://allafrica.com/
# https://www.bbc.com/news/world/africa




#-----------------------------------------------CREATE FULL LIST OF SEARCH QUERYS------------------------------------------------------------

full_list = []
    
for words, i in enumerate(keywords_list_1):
    for words, j in enumerate(keywords_list_2):
        full_list.append(country + " " + keywords_list_1[i] +  " AND " + keywords_list_1[j])    

for words, i in enumerate(keywords_list_1):
    for words, j in enumerate(keywords_list_2):
        for sites, k in enumerate(sites_list_rwanda_eng):
            full_list.append(country + " " + keywords_list_1[i] +  " AND " + keywords_list_1[j] + " " + site_suffix + sites_list_rwanda_eng[k])    

# i = 0
# j = 0

# for words in keywords_list_1:
#     for words in keywords_list_2:
#         full_list.append(country + " " + keywords_list_1[i] +  " AND " + keywords_list_1[j])
#         i+=1
#     j+=1

# for words, i in enumerate(keywords_list_1):
#     for words, j in enumerate(keywords_list_2):
#         full_list.append(country + " " + keywords_list_1[i] +  " AND " + keywords_list_1[j])

# for words in keywords_list:
    
#     i = 0
#     j = 0
    
#     for sites in sites_list_rwanda_eng:

#         full_list.append(country + " " + keywords_list[i] + " " + site_suffix + sites_list_rwanda_eng[j])
                
#         i+=1
#         j+=1
            
# for words in keywords_list:
    
#     i = 0
#     j = 0
    
#     for sites in sites_list_rwanda_eng:

#         full_list.append(keywords_list[i] + " " + site_suffix + sites_list_rwanda_eng[j])
                
#         i+=1
#         j+=1
            
# for words in keywords_list:
    
#     i = 0
#     j = 0
    
#     for sites in sites_list_rwanda_other:

#         full_list.append(keywords_list[i] + " " + site_suffix + sites_list_rwanda_other[j])
                
#         i+=1
#         j+=1

# for words in keywords_list:

#     j = 0
    
#     for sites in sites_list_rwanda_fre:

#             full_list.append(country + " " + site_suffix + sites_list_rwanda_fre[j])
                
#             j+=1
            
#-----------------------------------------------------------------------------------------------------------------------------    
# i = 0        
# for words in keywords_list:
#         keywords_list[i] = country + " " + and_paramter + " " + keywords_list[i]
#         i+=1
    
#print(full_list)

# keywords_list = [""""Rwanda" AND shoot""", 
# """"Rwanda" AND machete""",
# """"Rwanda" AND stab""",
# """"Rwanda" AND explosion""",
# """"Rwanda" AND detonation""",
# """"Rwanda" AND weapon""",
# """"Rwanda" AND dead""",
# """"Rwanda" AND death""",
# """"Rwanda" AND fatal""",
# """"Rwanda" AND injury""",
# """"Rwanda" AND wound""",
# """"Rwanda" AND trauma""",
# """"Rwanda" AND kill"""]

# for keyword in keywords_list:
    
#     keywords = keyword

#keywords = "wikipedia"

# def ddg_news(keywords, region='wt-wt', safesearch='off', time=None, max_results=2, output=print):
#         """DuckDuckGo news search

#         Args:
#             keywords: keywords for query.
#             region: country of results - wt-wt (Global), us-en, uk-en, ru-ru, etc. Defaults to "wt-wt".
#             safesearch: On (kp = 1), Moderate (kp = -1), Off (kp = -2). Defaults to "Moderate".
#             time: 'd' (day), 'w' (week), 'm' (month). Defaults to None.
#             max_results: maximum DDG_news gives out 240 results. Defaults to 25.
#             output: csv, json, print. Defaults to None.
#         Returns:
#             DuckDuckGo news search results.
#         """

# test_header = ['date', 'title', 'body', 'url', 'image', 'source']

# # 1. Open a new CSV file
# with open('ddg_segmented_v3.csv', 'w', encoding="UTF8") as file:
#     # 2. Create a CSV writer
#     writer = csv.writer(file)

#     # 3. Write data to the file
#     writer.writerow(test_header)

#     for keyword in keywords_list:
        
#         keywords = keyword
        
#         r = ddg_news(keywords, region='wt-wt', safesearch='Off', time='w', max_results=10, output=csv)      
        
#         writer.writerow(r)
        
#         print(r)

test_header = ['url']

# 1. Open a new CSV file
with open('ddg_url_test2.csv', 'w', encoding="UTF8") as file:
    # 2. Create a CSV writer
    writer = csv.writer(file)

    # 3. Write data to the file
    writer.writerow(test_header)

    for keyword in full_list:
            
        keywords = keyword
            
        r = ddg(keywords, region='wt-wt', safesearch='Off', time='w', max_results=240)
        p = ddg_news(keywords, region='wt-wt', safesearch='Off', time='w', max_results=240)   
        
        x = 0
        try:
            for items in r:
                
                print(r[x]['href'])
                print(p[x]['href'])
                writer.writerow([r[x]['href']])
                writer.writerow([p[x]['href']])
                
                x+= 1
        except:
            pass
    
#Remove duplicates 
with open('ddg_url_test2.csv', 'r') as in_file, open('ddg_url_test_no_dupes_v3.csv', 'w') as out_file:
    seen = set() # set for fast O(1) amortized lookup
    for line in in_file:
        if line in seen: continue # skip duplicate

        seen.add(line)
        out_file.write(line)

    
print("DONE")


























