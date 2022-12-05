import csv

i = 2

#id_nr = 1

k = 256

#/Users/luddejahrl/Desktop/Systematic_media_review/SMR_retrieved/OUTPUT_v4

# 1. Open a new CSV file
with open('manual_retrieved_v1.csv', 'w', encoding="UTF8") as file:
    # 2. Create a CSV writer
    writer = csv.writer(file)
    
    writer.writerow(['text', 'target'])
    
    # adding the manually approved MTI
    for i in range(k):
        
        #lines = ''
        
        with open("/Users/luddejahrl/Desktop/Systematic_media_review/SMR_retrieved/OUTPUT_manual/fulltext_version4_{" + str(i+1) +"}.txt", 'r') as f:
            
            #reads all of the txt into one list of strings list[str]
            lines = f.readlines()

        lines_str = ' '.join(map(str, lines))
        
        res = []
        for sub in lines:
            res.append(sub.replace("\n", ""))
        
        text = str(res).replace(",", "")            

        print(text)
        
        # 3. Write data to the file
        writer.writerow([text, '1'])
        
        i += 1
        
    #add the non-MTI from another dataset (target = '0')
    
    
# scramble the lines 
        


print('DONE')