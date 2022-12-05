import pandas as pd
import csv
import time

place_names = [
    "Rwanda",
    "Kigali",
    "Byumba",
    "Muhanga",
    "Gisenyi",
    "Kibuye",
    "Rwamagana",
    "Cyangugu",
    "Ruhengeri",
    "Nyanza",
    "Bugarama",
    "Gikongoro",
    "Nyamata",
    "Nyagatare",
    "Busogo",
    "Rubengera",
    "Ruhango",
    "Kayonza",
    "Butare",
    "Kabuga",
    "Musanze",
    "Ndera",
    "Murambi",
    "Gisagara",
    "Ngororero",
    "Kabarore",
    "Kagitumba",
    "Rusumo",
    "Cyanika"
    "Gatuna",
    "Kibeho",
    "Goma",
    "Nemba",
    "Northern Province",
    "Southern Province",
    "Eastern Province", 
    "Western Province"
    ]

def drop_region(data):

    data = './Systematic_Media_Review_v2/retrieved_articles/retrieved_articles_shorts_removed_v1.csv'

    file_out = './Systematic_Media_Review_v2/retrieved_articles/retrieved_articles_region_checked_v1.csv'

    header_outfile = "title,url,text"
    with open(file_out, 'w') as out_file:
        
        writer = csv.writer(out_file)
        out_file.write(header_outfile)

    df_file = pd.read_csv(data) 

    df_file_out = pd.read_csv(file_out) 

    df_file_len_prior = len(df_file)

    print("\nRemoving rows were article text doesn't mention atleast ONE of the regions in list...")

    for index, row in df_file.iterrows():
        word_found = False
        for place in place_names:
            
            article_text = str(row['text'])
            
            # print('Is ' + str(place) + ' in: ')
            # print(article_text)
            
            if place in article_text:
                            
                #print('Yes it is!')
                
                new_row = pd.Series({'title': row['title'], 'url': row['url'], 'text': row['text']})
                
                #print(new_row)
                
                df_file_out = pd.concat([df_file_out, new_row.to_frame().T], ignore_index=True)
                
                word_found = True
                
            if word_found == True:
                break

    print('\nRows dropped: ' + str(df_file_len_prior - len(df_file_out)) + ' | Total number of articles: ' + str(len(df_file_out)))

    df_file.to_csv(file_out, index=False)

    print('Dropped based on region DONE')

    return(file_out)

        
        