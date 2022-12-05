#this function is supposed to remove articles that do not contain any of the keywords defined in the seach query
import csv
from distutils import config
#from duckduckgo_search import ddg
#from duckduckgo_search import ddg_news
import pandas as pd

from ddg_search_v1 import keywords_list_1
from ddg_search_v1 import keywords_list_2

keywords_list = keywords_list_1 + keywords_list_2


def confirm_keywords(csv_infile):

    #csv_infile = './Systematic_Media_Review_v2/ddg_url_list_duplicates_removed_v2.csv'    

    #file given to the function
    df_file_in = pd.read_csv(csv_infile) 

    #print(df_file_in)

    #set path for new out_file that contains atleast one of the keywords
    new_out_file = './Systematic_Media_Review_v2/data/url_list_keyword_confirmation_v1.csv'

    #give the same apperance as the in_file
    header_outfile = "title,url"
    with open(new_out_file, 'w') as out_file:
        
        writer = csv.writer(out_file)
        out_file.write(header_outfile)
        #out_file.write("\nvalue_1,value_2")

    #new dataframe with
    df_file_out = pd.read_csv(new_out_file)

    #print(df_file_out)

    #remove special character (") tthat was used in special query
    for i, keyword in enumerate(keywords_list):
        keywords_list[i] = keywords_list[i].replace('"', '')

    for index, row in df_file_in.iterrows():
        word_found = False
        for keyword in keywords_list:
            
            if keyword in row['title']:
                            
                new_row = pd.Series({'title': row['title'], 'url': row['url']})
                
                #print(new_row)
                
                df_file_out = pd.concat([df_file_out, new_row.to_frame().T], ignore_index=True)
                
                word_found = True
                
            if word_found == True:
                break

    print('\nRows removed: ' + str(len(df_file_in) - len(df_file_out)))

    print('\nThe resulting list of articles: ')

    print(df_file_out)

    df_file_out.to_csv(new_out_file, index=False)

    print('\nRemoving unvalidated articles DONE')

#----------------------------------------------------------------------------------------------------------------------------

    # with open(url_list, 'r') as in_file, open(new_out_file, 'w') as out_file:
        
    #     #writer = csv.writer(out_file)
    
    #     seen = set() # set for fast O(1) amortized lookup
        
    #     for line in in_file:
    #         if line in seen: continue # skip duplicate

    #         seen.add(line)
    #         out_file.write(line)
            
    #         removed_counter += 1
            
    
    # for keyword in keywords_list:
    #     with open('new_out_file.csv', 'rt') as f:
    #         reader = csv.reader(f, delimiter=',') 
    #         for row in reader:
    #             for field in row:
    #                 if field == keyword: