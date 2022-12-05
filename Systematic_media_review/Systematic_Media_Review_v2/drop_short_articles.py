import pandas as pd

#this function is supposed to remove rows that articles shorter then 15 characters
def drop_short_art(data):
    
    #minimum article length (in characters)
    minimum_artcile_length = 20

    #data = './Systematic_Media_Review_v2/retrieved_articles/retrieved_articles_v1.csv'

    retrieved_article_csv = './Systematic_Media_Review_v2/retrieved_articles/retrieved_articles_shorts_removed_v1.csv'

    df_file = pd.read_csv(data) 

    df_file_len_prior = len(df_file)

    print('\nRemoving rows were article text is shorter than 15 characters...')

    df_file = df_file.drop(df_file[df_file['text'].map(len) < minimum_artcile_length].index)

    print('\nRows dropped: ' + str(df_file_len_prior - len(df_file)) + ' | Total number of articles: ' + str(len(df_file)))

    df_file.to_csv(retrieved_article_csv, index=False)

    return(retrieved_article_csv)
    
    
    
    
    
    