# read in text files from "Full_text_version_1" 

# for every file pre process it into one line without "stop signs?" like u did in another file

# print every line into a new line in a new csv

import csv


i = 2

k = 1098

# for i in range(k):
#     #open("/Users/luddejahrl/Desktop/Systematic_media_review/OUTPUTS_final_v2/fulltext_version2_{" + str(i) +"}.txt", 'w')
#     current_file = open("/Users/luddejahrl/Desktop/Systematic_media_review/Full_text_version_1/fulltext_version1_{" + str(i) + "}.txt", 'r')
#     i += 1   

# 1. Open a new CSV file
with open('txt_to_csv_ddg_retrieved.csv', 'w', encoding="UTF8") as file:
    # 2. Create a CSV writer
    writer = csv.writer(file)
    
    writer.writerow(['text'])
    
    # adding the the searched for articles using ddg
    for i in range(k):
        
        #lines = ''
        
        with open("/Users/luddejahrl/Desktop/Systematic_media_review/Full_text_version_1/fulltext_version1_{" + str(i+1) + "}.txt", 'r') as f:
            
            lines = f.readlines()

        lines_str = ' '.join(map(str, lines))
        
        res = []
        for sub in lines:
            res.append(sub.replace("\n", ""))
        
        text = str(res).replace(",", "")            

        print(text)
        
        # 3. Write data to the file
        writer.writerow([text])
        
        i += 1
        
    #add the non-MTI from another dataset (target = '0')
    
    
# scramble the lines 
        


print('DONE')
    
    
    
    
    