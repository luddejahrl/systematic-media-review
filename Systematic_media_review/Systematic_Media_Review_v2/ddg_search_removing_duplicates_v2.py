def remove_duplicates(csv_url_list):

    import csv
    from distutils import config
    from duckduckgo_search import ddg
    from duckduckgo_search import ddg_news
    import pandas as pd

#-----------------------------------------------REMOVING DUPLICATES------------------------------------------------------------

    #csv_url_list = './Systematic_Media_Review_v2/ddg_url_list_v1.csv'

    print("\nRemoving duplicates from list of API search results... (Results found in; '/data/ddg_url_list_duplicates_removed_v(x).csv'")

    csv_url_list_duplicates_removed = './Systematic_Media_Review_v2/data/ddg_url_list_duplicates_removed_v2.csv'
    
    #convert csv to dataframe
    df_file = pd.read_csv(csv_url_list) 
    
    df_file_duplicates_removed = df_file.drop_duplicates(subset=['url'], keep='first')
    
    #number of duplicates
    total_number_of_hits_no_dupes = len(df_file.index) - len(df_file_duplicates_removed.index)

    print('\nDuplicates removed: ' + str(total_number_of_hits_no_dupes))
    
    print('\nThe resulting list of articles: ')
    
    print(df_file_duplicates_removed)
    
    df_file_duplicates_removed.to_csv(csv_url_list_duplicates_removed, index=False)

    print('\nRemoving duplicates DONE')

    return(csv_url_list_duplicates_removed)

#-----------------------------------------------/REMOVING DUPLICATES------------------------------------------------------------


    # seen = set() # set for fast O(1) amortized lookup
    
    # for row in df_file.iterrows():
        
    #     print(row)
        
    #     if row in seen: continue # skip duplicate
    #     seen.add([row])
        
    # seen.to_csv('/Systematic_Media_Review_v3/ddg_url_list_duplicates_removed_v3.csv', index=False)    
    
    # with open(csv_url_list, 'r') as in_file, open(csv_url_list_duplicates_removed, 'w') as out_file:
    
    #     writer = csv.writer(out_file)
                
    #     seen = set() # set for fast O(1) amortized lookup
        
    #     for line in in_file:
            
    #         print(line)
            
    #         if line in seen: continue # skip duplicate

    #         seen.add(line)
    #         #out_file.write(line)
    #         writer.writerow([line])
            
    #         total_number_of_hits_no_dupes += 1


# final[final.target != 0].to_csv('submissions_hit.csv', index=False)