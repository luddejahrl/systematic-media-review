from ddg_search_removing_duplicates_v2 import remove_duplicates
from ddg_search_v1 import duckduckgo_build_url_list
from confirming_keywords_v2 import confirm_keywords
from article_classifier_v1 import classifier
from article_retriever_v1 import retriever
from drop_short_articles import drop_short_art
from drop_region_based import drop_region
#from ner_extracter_v1 import ner_extract

#main

print('\nWelcome to the Systematic media review Thesis!')

#choose your corpus (build new one or load pre-built corpus)
print('\nWould you like to run Duck Duck Go search protocol to build your list of relevant article urls?')
val_build_corpus = input("y/n: ")
if(val_build_corpus == "y" or val_build_corpus == "Y"):
    print('\nRunning Duck Duck Go search protocol') 
    current_corpus = duckduckgo_build_url_list()
else:    
    print('\nWould you like to use pre-built corpus example? (Rwanda)')
    val_build_corpus = input("y/n: ")
    if(val_build_corpus == "y" or val_build_corpus == "Y"):
        print('\nUsing pre-built corpus example (Rwanda)')
        current_corpus = 'Systematic_Media_Review_v2/data/ddg_url_list_v1.csv'
    else:
        print("\nBuild your corpus from file (.csv, Header: 'title', 'url'), write path: ")
        val_path_corpus = input("path: ")
        current_corpus = val_path_corpus

#remove duplicates from csv 
print('\nWould you like to remove duplicates from your corpus? (url based)')
val_remove_corpus_duplicates = input("y/n: ")
if(val_remove_corpus_duplicates == "y" or val_remove_corpus_duplicates == "Y"):
    current_corpus = remove_duplicates(current_corpus) #returns the path to the csv file with duplicates removed 

# Investegation showed that to a very high degree, that all relevant articles have atleast ONE of the 
# keywords (from keywords_list_1 and _2) in their title. By removing the articles that do not have this in their 
# title may remove alot of unwanted articles that are not relevant.

#confirm the list by removing article titles not containing any of the keywords
print('\nWould you like to validate your list by removing article (titles) not containing any of the keywords?')
val_validate_titles = input("y/n: ")
if(val_validate_titles == "y" or val_validate_titles == "Y"):
    current_corpus = confirm_keywords(current_corpus) #returns the path to the csv file with duplicates removed 
else: 
    print('No validation performed...')

#dowload articles:
print('\nWould you like to download your articles?')
val_classfier = input("y/n: ")
if(val_classfier == "y" or val_classfier == "Y"):
    current_corpus = retriever(current_corpus) #returns the path to the csv file with duplicates removed 
else: 
    print('\nUse pre-loaded dataset?')
    val_classfier_preload = input("y/n: ")
    if(val_classfier_preload == "y" or val_classfier_preload == "Y"):
        current_corpus = './Systematic_Media_Review_v2/retrieved_articles/retrieved_articles_v1.csv' 
    else: 
        print("Enter your own dataset ('title', 'url', 'text') ")
        val_path_corpus = input("path: ")
        current_corpus = val_path_corpus
        
#drop rows with empty articles ('text')
print('\nWould you like to drop articles that are to short? (less than 20 characters)')
val_drop_too_short = input("y/n: ")
if(val_drop_too_short == "y" or val_drop_too_short == "Y"):
    current_corpus = drop_short_art(current_corpus)
else:
    print('\nNo rows were dropped based on article length')
    

#check if 'text' contains "Rwanda" or any other string of places in Rwanda?

# The gathering of this data and list may be scrapped from google by searching "list of rwandan cities" and using BS4 to find:
# Example: data-entityname="Muhanga". alternatively it may be found manually by wikipedia or other source

print("\nWould you like to drop articles that don't contain any mention of relevant regions?")
val_drop_region = input("y/n: ")
if(val_drop_region == "y" or val_drop_region == "Y"):
    current_corpus = drop_region(current_corpus)
else:
    print('\nNo rows were dropped based on region requirement')

#perform classifier:
print('\nWould you like to classify your corpus as (Relevant [1])/(Non-Relevant [0])? ')
val_classfier = input("y/n: ")
if(val_classfier == "y" or val_classfier == "Y"):
    current_corpus = classifier(current_corpus) #returns the classified
else: 
    print('No classification performed')

# #perform NER and extract data
# print('\nWould you like to extract information from your articles? (Location, date, ) ')
# val_ner_extract = input("y/n: ")
# if(val_ner_extract == "y" or val_ner_extract == "Y"):
#     current_corpus = ner_extract(current_corpus) #returns the classified
# else: 
#     print('No classification performed')


print('\nMain DONE')

    
    
    


    

    
    



