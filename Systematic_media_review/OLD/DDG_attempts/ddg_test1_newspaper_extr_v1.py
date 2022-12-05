import csv
from csv import reader
import newspaper
from newspaper import Article
#from newspaper import news_pool


# with open('ddg_url_test_no_dupes_v3.csv', 'r') as in_file, open('ddg_url_test_no_dupes_full_text.csv', 'w') as out_file:

#     csv_reader = reader(in_file)

#     for row in csv_reader:
#             print(row[0])

#             article = Article((row[0]))
                
#             article.download()
#             article.parse()
                
#             out_file.write(article.text)


fn = open('ddg_url_test_no_dupes_v3.csv', 'r')

fnew = fn.read()

fs = fnew.split('\n')

i = 1

for value in fs:
    
    article = Article(value)
    
    try:
        article.download()
        article.parse()
        
        with open("/Users/luddejahrl/Desktop/Systematic_media_review/Full_text_version_1/fulltext_version1_{" + str(i) +"}.txt", 'w') as f:
        
            f.write(article.text)
            f.close
            
        print("PING")
        i+=1
    except:
        pass

# for value in fs:
#    f = [open("/Users/luddejahrl/Desktop/Systematic_media_review/Full_text_version_1/" % i, 'w') for i in range(len(fnew))]

# f.write(value)
# f.close()

        
print("DONE")