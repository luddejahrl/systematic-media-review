def drop_duplicate_title(csv_list):
    
    import pandas as pd
    import csv
    from distutils import config
    from duckduckgo_search import ddg
    from duckduckgo_search import ddg_news
    import pandas as pd

#-----------------------------------------------REMOVING DUPLICATES------------------------------------------------------------

    print("\nRemoving duplicates from list of API search results... '")
    
    file_out = csv_list[:len(csv_list)-4] + '_title_checked.csv' #csv_url_list[:len(csv_url_list)-4]
    
    #convert csv to dataframe
    df_file = pd.read_csv(csv_list) 
    
    df_file_duplicates_removed = df_file.drop_duplicates(subset=['title'], keep='first')
    
    #number of duplicates
    total_number_of_hits_no_dupes = len(df_file.index) - len(df_file_duplicates_removed.index)

    print('\nDuplicates removed: ' + str(total_number_of_hits_no_dupes))
    
    print('\nThe resulting list of articles: ')
    
    print(df_file_duplicates_removed)
    
    df_file_duplicates_removed.to_csv(file_out, index=False)

    print('\nRemoving duplicates DONE')

    return(file_out)

        
        
        
            
            
        