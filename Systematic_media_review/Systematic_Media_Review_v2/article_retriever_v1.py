import csv
from csv import reader
import newspaper
from newspaper import Article
import pandas as pd

def retriever(list): #list should have ['title','url']
    
    list = './Systematic_Media_Review_v2/data/url_list_keyword_confirmation_v1.csv'

    df_file_in = pd.read_csv(list) 

    #article failed counter
    article_download_fail = 0

    #retrievals attempt counter
    retrievals_attempted = 0

    df_file_in_len = len(df_file_in)

    retrieved_article_csv = './Systematic_Media_Review_v2/retrieved_articles/retrieved_articles_v1.csv'

    # add new colomn 'text' to contain article text
    with open(retrieved_article_csv, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['title', 'url', 'text'])

    #new dataframe with
    df_file_out = pd.read_csv(retrieved_article_csv)

    removal_char = ","

    for index, row in df_file_in.iterrows():
        
        #print(row['url'])
        
        article = Article(row['url'])
        
        try:
            article.download()
            article.parse()
            
            retrieved_text = article.text
            
            #remove comma (,) to not mess with formating when converting to csv
            retrieved_text = retrieved_text.replace(removal_char, " ")
            
            new_row = pd.Series({'title': row['title'], 'url': row['url'], 'text': [retrieved_text]})
            
            df_file_out = pd.concat([df_file_out, new_row.to_frame().T], ignore_index=True)
            
            #print(df_file_out)
            
            df_file_out.to_csv(retrieved_article_csv, index=False)
        
        except:
            article_download_fail += 1
            pass
        
        retrievals_attempted += 1
        
        #one line due to \r
        print('Progress: ' + str(retrievals_attempted) + '/' + str(df_file_in_len) + ' (' + str(round((retrievals_attempted/(df_file_in_len)) * 100, 2)) + ' %)' + ' | Unable to download: ' + str(article_download_fail), end='\r')    

    # an empty column is made? so its simply deleted
    #del df_file_out['text.1']

    print('\nNumber of articles downloaded: ' + str(df_file_in_len-article_download_fail) + ' Number of articles unable to download: ' + str(article_download_fail)) # retrieved_article_csv

    #remove articles without any retrieved text? 
    #df_file_out = df_file_out.drop(df_file_out[len(df_file_out.text) < 20].index)

    df_file_out.to_csv(retrieved_article_csv, index=False)

    print("Retrieval DONE")
    
    return(retrieved_article_csv)

