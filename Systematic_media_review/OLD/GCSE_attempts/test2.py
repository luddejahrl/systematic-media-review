##Import necessary libraries
from bs4 import BeautifulSoup as bs
import requests

#https://www.newtimes.co.rw/section/read/188551
#r = requests.get('https://www.newtimes.co.rw/section/read/188551')

# convert to a beutifulsoup object

#soup = bs(r.content, 'html.parser')

#fix indenttation for inspection
#contents = soup.prettify()
#print(contents)
 
#grab all <p>

#find_header = soup.find('h1')

#print(find_header) 

#find_text = soup.find_all('<p>')
#print(find_text) 

## reading content from the file
r = requests.get('https://www.newtimes.co.rw/section/read/188551')
    
## creating a BeautifulSoup object
#soup = bs.BeautifulSoup(r.content, "html.parser")
soup = bs(r.content, 'html.parser')

## finding all p tags
p_tags = soup.find_all('p')     

print(p_tags)

print("\n-----Class Names Of All Paragraphs-----\n")

for tag in p_tags:
    print(tag['class'][0])
    
print("\n-----Content Of All Paragraphs-----\n")

for tag in p_tags:
    print(tag.text)


