import math
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import time

#remove warning for:
# SettingWithCopyWarning:  A value is trying to be set on a copy of a slice from a DataFrame
pd.options.mode.chained_assignment = None  # default='warn'

#this function is to remove articls that are the duplicates that are republished by other websites

def vectorize(string):
    # create a vector of zeros
    vector = np.zeros(len(string))

    # iterate through the string and update the vector
    for i, char in enumerate(string):
        vector[i] = ord(char)

    # reshape the vector to a 2D array with a single row
    vector = vector.reshape(1, -1)

    # return the vector
    return vector

#compare strings returns the cosine similarity of the two strings (-1) all different and (1) all the same
def compare_strings(str1, str2):
    # convert strings to vectors
    vector1 = vectorize(str1)
    vector2 = vectorize(str2)

    # ensure vectors have the same length
    if vector1.shape[1] != vector2.shape[1]:
        max_length = max(vector1.shape[1], vector2.shape[1])
        vector1 = np.resize(vector1, (1, max_length))
        vector2 = np.resize(vector2, (1, max_length))

    # calculate cosine similarity
    cosine_sim = cosine_similarity(vector1, vector2)[0,0]

    # calculate the difference of angle between the cosine similarities
    diff_angle = 1 - cosine_sim
    
    return diff_angle

## TO DO: check what threshold of percentage similraity is a reasonable value (95 % as of now)
def remove_duplicate_article_base(csv_infile):
    
    rows_dropped = 0
    
    similarity_val_text = 0.05
    similarity_val_title = 0.025
    
    print('\nRemoving rows were article text or article title is of (' + str(1-similarity_val_text) + '%) & (' + str(1-similarity_val_text) + '%) similarity...')
    
    df_file_in = pd.read_csv(csv_infile)
    
    #df_file_in = pd.read_excel(csv_infile)
    
    #add empty colomn that will store true/flase if positive
    df_file_in['duplicate'] = False
    
    csv_out_path = './Systematic_Media_Review_v2/classified_articles/classified_articles_hits_duplicates_removed_v1.csv'
    
    #csv_out_path = './systematic_media_review_v3/source/data/rwanda_example/test_temp_v1.xlsx'
    
    original_length = len(df_file_in)
    
    progress_len_full = len(df_file_in)*len(df_file_in)
    

    for i in range(len(df_file_in)-1):
        
        #print(i)
        
        str1_text = df_file_in.loc[i]['article_text']
        str1_title = df_file_in.loc[i]['title']
        
        
        for j in range(i, (len(df_file_in)-1), 1):
            
            str2_text = df_file_in.loc[j+1]['article_text']
            str2_title = df_file_in.loc[j+1]['title']
            
            diff_angle_text = compare_strings(str1_text, str2_text)
            diff_angle_title = compare_strings(str1_title, str2_title)
            
            if((diff_angle_text <= similarity_val_text) or (diff_angle_title <= similarity_val_title)):
                
                #print('match found: ' + str(diff_angle_text))
                
                #iterate droped rows counter
                rows_dropped +=1
                
                #set duplicate to true for row
                df_file_in.at[j+1,'duplicate'] = True
                
                #print(df_file_in.loc[j+1]['duplicate'])
                
                
                
                
            
            print('Progress: ' + str(i*j) + '/' + str(progress_len_full) + ' (' + str(round(((i*j)/(progress_len_full)) * 100, 2)) + ' %)' + ' | Duplicates found: ' + str(rows_dropped), end='\r')    

                
    print(df_file_in)
    
    print('Removing rows...')
    
    df_file_out = df_file_in[df_file_in['duplicate'] != True]

    print('Rows removed : ' + str(rows_dropped) +  ' | New total number of rows: ' + str(original_length - rows_dropped))

    print(df_file_out)
    
    #return csv_out
    
    df_file_out.to_csv(csv_out_path, index=False)
    
    return df_file_out

# csv_in_ex = './Systematic_Media_Review_v2/classified_articles/classified_articles_hits_v1.csv'

# example_out = remove_duplicate_article_base(csv_in_ex)

# csv_out_path = './Systematic_Media_Review_v2/classified_articles/classified_articles_hits_duplicates_removed_v1.csv'

# csv_out_path = example_out.to_csv(csv_out_path, index=False)

# print(example_out)

# print('New number of articles: ' + str(len(example_out)))

# print('DONE')