
#-----------------------------------------------DEFAULT SEARCH SETTINGS FOR QUERY------------------------------------------------------------
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

# List of outcomes (mass-trauma outcomes)
keywords_list_2 = [
'"dead"', '"deaseased"', '"deadly"', '"death"',
'"fatal"',
'"injury"', '"injur"', '"injured"', '"injurys"',
'"wound"', '"wounds"', '"wounded"', 
'"truamas"', '"truama"', 
'"kill"', '"killed"', '"kills"',
'"car crash"']
#ADD accident?

# search refinement by appending common sites  
common_sites = [
"",
"reuters.com/",
"english.news.cn/",
"bbc.com/"
]

# search refinement by excluding common sites  
exclude_sites = [
"wikipedia.org/",
"cdc.gov/",
"featureshoot.com/"
]

#Search refinement by including certain years at the end of each Query
years_refinement = [
"2010",
"2011",
"2012",
"2013",
"2014",
"2015",
"2016",
"2017",
"2018",
"2019",
"2020"
]

#-----------------------------------------------/DEFAULT SEARCH SETTINGS FOR QUERY------------------------------------------------------------

def duckduckgo_build_url_list(csv_url_list):

    #from ast import keyword
    import csv
    from distutils import config
    from duckduckgo_search import ddg
    from duckduckgo_search import ddg_news
    import time
    #import newspaper

    #https://pypi.org/project/duckduckgo-search/

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

    # ORIGINAL QUERY
    # “Rwanda” 
    # AND “(shoot OR machete OR stab OR explosion OR detonation OR weapon)” 
    # AND “(dead OR death OR fatal OR injury OR wound OR trauma OR kill)” 2010..2020

    #-----------------------------------------------SEARCH SETTINGS FOR QUERY------------------------------------------------------------
    print('Use default settings? (Country: Rwanda, Including Common: Yes, Excluding Unwanted: yes)')
    val = input("y/n: ")

    # DEFAULT SEARCH SETTINGS
    if(val == "y" or val == "Y"):
        print('\nProceding with standard values...') #Do nothing - USE DEFAULT

    # SEARCH SETTINGS
    else:
        # CREATE SEARCH QUERY
        
        # COUNTRY
        country = input("Country: ")
        
        # LIST OF INJURIES AND CAUSES
        print('Use default List of injuries/cuases? (mass-trauma causes)')
        val = input("y/n: ")
        if(val == "y" or val == "Y"):
            print('Proceding with standard List of injuries/cuases') #Do nothing - Use defaults
        else:    
            # List of injuries/cuases (mass-trauma causes)
            keywords_list_1 = []
            keywords_list_1_max_length = 20
            
            while len(keywords_list_1) < keywords_list_1_max_length:
                keywords_list_1_item = input("Add terms of injuries/cuases (Finish with 0): ")
                
                if keywords_list_1_item not in keywords_list_1:
                    keywords_list_1.append(keywords_list_1_item)
                    
                #stopping term provided
                if keywords_list_1_item == "0":
                    # Remove the last item of the list (stopping number 0)
                    keywords_list_1 = keywords_list_1[ : -1]
                    break
        print('List of injuries/cuases (mass-trauma causes)')
        print(keywords_list_1)


        # LIST OF OUTCOMES
        print('Use default List of outcomes? (mass-trauma outcomes)')
        val = input("y/n: ")
        if(val == "y" or val == "Y"):
            print('Proceding with standard List of outcomes') #Do nothing - Use defaults
        else:    
            # List of injuries/cuases (mass-trauma causes)
            keywords_list_2 = []
            keywords_list_2_max_length = 20
            
            while len(keywords_list_2) < keywords_list_2_max_length:
                keywords_list_2_item = input("Add terms of injuries/cuases (Finish with 0): ")
                
                if keywords_list_2_item not in keywords_list_2:
                    keywords_list_2.append(keywords_list_2_item)
                    
                #stopping term provided
                if keywords_list_2_item == "0":
                    # Remove the last item of the list (stopping number 0)
                    keywords_list_2 = keywords_list_2[ : -1]
                    break
        print('List of outcomes (mass-trauma outcomes)')
        print(keywords_list_2)


        # LIST OF COMMON WEBSITES TO APPPEND FOR QUERY REFINEMENT
        print('Include search refinemnt by using common websites appending?')
        val = input("y/n: ")
        if(val == "y" or val == "Y"):
            print('Use default list of common websites appeding?') #Do nothing 
            val = input("y/n: ")
            if(val == "y" or val == "Y"):
                print('Proceding with standard List of common websites appended') #Do nothing - Use defaults
            else:
                common_sites = []
                common_sites_max_length = 20
                
                while len(common_sites) < common_sites_max_length:
                    common_sites_item = input("Add sites to append [Ex: 'reuters.com/'] (Finish with 0): ")
                    
                    if common_sites_item not in common_sites:
                        common_sites.append(common_sites_item)
                        
                    #stopping term provided
                    if common_sites_item == "0":
                        # Remove the last item of the list (stopping number 0)
                        common_sites = common_sites[ : -1]
                        break
        else:    
            common_sites = [] # empty list of common sites
        print('List of appended websites:')
        print(common_sites)
        
        
        # LIST OF COMMON WEBSITES TO EXCLUDE FOR QUERY REFINEMENT
        print('Include search refinemnt by excluding certain websites?')
        val = input("y/n: ")
        if(val == "y" or val == "Y"):
            print('Use default list of excluding certain websites?') #Do nothing 
            val = input("y/n: ")
            if(val == "y" or val == "Y"):
                print('Proceding with standard list of excluding certain websites') #Do nothing - Use defaults
            else:
                exclude_sites = []
                exclude_sites_max_length = 20
                
                while len(exclude_sites) < exclude_sites_max_length:
                    exclude_sites_item = input("Exclude sites [Ex: 'wikipedia.org/'] (Finish with 0): ")
                    
                    if exclude_sites_item not in exclude_sites:
                        exclude_sites.append(exclude_sites_item)

                    #stopping term provided
                    if exclude_sites_item == "0":
                        # Remove the last item of the list (stopping number 0)
                        exclude_sites = exclude_sites[ : -1]
                        break
        else:    
            exclude_sites = [] # empty list of common sites
        print('List of excluded websites:')
        print(exclude_sites)
        
    ## ADD so that certain years may be included (ask what start year to start at then what year to end at)

    #-----------------------------------------------LIST OF RWANDAN NEWSITES FOUND ONLINE------------------------------------------------------------

    sites_list_rwanda_eng = [
    #"", #empty to include search for non site specifik searches
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
    # https://www.bbc.com/
    # https://www.reuters.com/

    #-----------------------------------------------/LIST OF RWANDAN NEWSITES FOUND ONLINE------------------------------------------------------------

    #-----------------------------------------------CREATE FULL LIST OF SEARCH QUERYS------------------------------------------------------------

    #string to form exclusion string
    exclude = ""

    #create site exclusion string:
    for words in exclude_sites:
        exclude += " -site:" + words
        
    site_suffix = "site:"

    # Full list of individual search querrys
    full_list = []
        
    # Every combination of List (cause) and List (outcome) 

    #QUERY ONLY COUNTRY + TERM 1 + TERM 2
    for i, words in enumerate(keywords_list_1):
        for j, words in enumerate(keywords_list_2):
            full_list.append(country + " " + keywords_list_1[i] +  " AND " + keywords_list_2[j])    
            
    #QUERY COUNTRY + TERM 1 + TERM 2 + YEAR
    for i, words in enumerate(keywords_list_1):
        for j, words in enumerate(keywords_list_2):
            for k, words in enumerate(years_refinement):
                full_list.append(country + " " + keywords_list_1[i] +  " AND " + keywords_list_2[j] + " " + years_refinement[k])

    #QUERY COUNTRY + TERM 1 + TERM 2 + EXCLUDED SITES
    for i, words in enumerate(keywords_list_1):
        for j, words in enumerate(keywords_list_2):
            full_list.append(country + " " + keywords_list_1[i] +  " AND " + keywords_list_2[j] + exclude)    

    #QUERY COUNTRY + TERM 1 + TERM 2 + REFINEMENT SITES
    for i, words in enumerate(keywords_list_1):
        for j, words in enumerate(keywords_list_2):
            for k, sites in enumerate(sites_list_rwanda_eng):
                full_list.append(country + " " + keywords_list_1[i] +  " AND " + keywords_list_2[j] + " " + site_suffix + sites_list_rwanda_eng[k])
                

    print("\nFull list of querys (Total: " + str(len(full_list)) + ")\n")
    print("Print full list of querys?")
    val = input("y/n: ")
    if(val == "y" or val == "Y"):
        for x in range(len(full_list)):
            print(full_list[x])

    print("\nBuilding List of Duck Duck Go search API results... (Results found in; 'ddg_url_list_v(x).csv')\n")  

    #-----------------------------------------------/CREATE FULL LIST OF SEARCH QUERYS------------------------------------------------------------

    #-----------------------------------------------CALLING DUCK DUCK GO SEARCH API------------------------------------------------------------

    # DuckDuckGo text search. Query params: https://duckduckgo.com/params
    #     Args:
    #         keywords (str): keywords for query.
    #         region (str, optional): wt-wt, us-en, uk-en, ru-ru, etc. Defaults to "wt-wt".
    #         safesearch (str, optional): on, moderate, off. Defaults to "moderate".
    #         time (Optional[str], optional): d, w, m, y. Defaults to None.

    #           time paramtre filters so that it is the latest within a (d)ay, (w)eek, (m)onth, (y)ear    

    #         max_results (Optional[int], optional): maximum number of results, max=200. Defaults to None.
    #             if max_results is set, then the parameter page is not taken into account.

    #           max=200 for ddg & max=240 for ddg_news

    #         page (int, optional): page for pagination. Defaults to 1.
    #         output (Optional[str], optional): csv, json. Defaults to None.
    #         download (bool, optional): if True, download and save dociments to 'keywords' folder.
    #             Defaults to False.

    #     Returns:
    #         Optional[List[dict]]: DuckDuckGo text search results.

    results_header = ['title', 'url']

    # STATISTICS FOR THE API CALL
    #Counter to check if the maximum amount of results were achieved, meaning possible loss
    reached_max_results_ddg = 0
    reached_max_results_ddg_news = 0

    #paramtres used to check percentage of maximum hits to all querys
    # maximum_hits_ddg = len(full_list) * 200
    # maximum_hits_ddg_news = len(full_list) * 240

    #counter to check if the query
    no_hits_found_ddg = 0;
    no_hits_found_ddg_news = 0;

    #API call progress
    searches_made = 0

    #Total number of hits & hits after dupes removal
    total_number_of_hits = 0
    total_number_of_hits_no_dupes = 0

    #start measuring time for api calls
    start_time = time.time()

    csv_url_list = './Systematic_Media_Review_v2/data/ddg_url_list_v1.csv'

    # 1. Open a new CSV file
    with open(csv_url_list, 'w', encoding="UTF8") as file:
        # 2. Create a CSV writer
        writer = csv.writer(file)

        # 3. Write data to the file
        writer.writerow(results_header)
        
        for keyword in full_list:
            
            keywords = keyword
            
            r = ddg(keywords, region='wt-wt', safesearch='Off', max_results=200)
            p = ddg_news(keywords, region='wt-wt', safesearch='Off', max_results=240)   
            
            try:
                for x, items in enumerate(r):
                    #print(r[x]['href'])
                    #writer.writerow([r[x]['title'], r[x]['href'], r[x]['body']])
                    writer.writerow([r[x]['title'], r[x]['href']])

                    
                    #Maximum amount of hits found for query (ddg)
                    if x == 200:
                        reached_max_results_ddg += 1
                    
                    len_r = len(r)
            except:
                #No hits found
                no_hits_found_ddg += 1
                len_r = 0
                pass
            
            try:
                for y, items in enumerate(p):
                    #print(p[y]['href'])
                    #writer.writerow([p[x]['title'], p[y]['href'], p[x]['body']])
                    writer.writerow([p[x]['title'], p[y]['href']])
                    
                    #Maximum amount of hits found for query (ddg)
                    if x == 240:
                        reached_max_results_ddg += 1
                    
                    len_p = len(p)
            except:
                #No hits found
                no_hits_found_ddg_news += 1
                len_p = 0
                pass
            
            total_number_of_hits += (len_p + len_r)
            
            searches_made +=1
            
            #progress indicator (needs to be one line to be able to read stream correctly on mac ('\r' issue), add \n to windows machine?)
            print('Progress: ' + str(searches_made) + '/' + str(len(full_list)) + ' (' + str(round((searches_made/(len(full_list))) * 100, 2)) + ' %)' + ' | Tot. hits: ' + str(total_number_of_hits) + ' | No results found: ' + str(no_hits_found_ddg + no_hits_found_ddg_news)  + ' | Max. results hit: ' + str(reached_max_results_ddg), end='\r')    
            
    #-----------------------------------------------/CALLING DUCK DUCK GO SEARCH API------------------------------------------------------------

    #-----------------------------------------------REMOVING DUPLICATES------------------------------------------------------------

    # print("\n\nRemoving duplicates from list of API search results... (Results found in; 'ddg_url_list_duplicates_removed_v(x).csv'")

    # csv_url_list_duplicates_removed = './Systematic_Media_Review_v2/ddg_url_list_duplicates_removed_v1.csv'

    # with open(csv_url_list, 'r') as in_file, open(csv_url_list_duplicates_removed, 'w') as out_file:
        
    #     writer.writerow(results_header)
        
    #     seen = set() # set for fast O(1) amortized lookup
    #     for line in in_file:
    #         if line in seen: continue # skip duplicate

    #         seen.add(line)
    #         out_file.write(line)
    #         total_number_of_hits_no_dupes += 1

    #-----------------------------------------------/REMOVING DUPLICATES------------------------------------------------------------

    #-----------------------------------------------SEARCH STATISTICS------------------------------------------------------------
    print('\n\n\nFINAL SEARCH STATISTICS:')
    print('Total number of search terms:                  ' + str(len(full_list)))
    print('Total number of API calls:                     ' + str(len(full_list)*2))

    print('Total number of hits:                          ' + str(total_number_of_hits))
    print('Average hits per search:                       ' + str(round(total_number_of_hits/len(full_list),2)))

    #print('Total number of hits (duplicates removed):     ' + str(total_number_of_hits_no_dupes))
    #print('Average hits per search (duplicates removed):  ' + str(round(total_number_of_hits_no_dupes/len(full_list), 2)))

    print('Reached maximum results (ddg):                 ' + str(reached_max_results_ddg))
    print('Reached maximum results (ddg_news):            ' + str(reached_max_results_ddg_news))

    print('No results (ddg):                              ' + str(no_hits_found_ddg))
    print('No results (ddg_news):                         ' + str(no_hits_found_ddg_news))
    print('Total searches with no results:               ' + str(no_hits_found_ddg_news+no_hits_found_ddg))

    print('API call time:                                 ' + '%s seconds' % (time.time() - start_time))

    print("\nddg_search_v1: DONE")
    
    return(csv_url_list)

    # Progress: 5579/7812 (71.42 %) | Tot. hits: 42776 | No results found: 9635 | Max. results hit: 0

























