from newspaper import Article
from newspaper import fulltext
import requests

#example https://www.bbc.com/news/world-africa-37118166
#example https://www.newtimes.co.rw/section/read/188551 

url = 'https://www.newtimes.co.rw/section/read/188551'
url2 = 'https://www.bbc.com/news/world-africa-37118166'

article = Article(url2)

article.download()

article.html

article.parse()

print(article.publish_date)

print(article.text)

#html = requests.get('https://www.newtimes.co.rw/section/read/188551').text
html = requests.get('https://www.bbc.com/news/world-africa-37118166').text

text = fulltext(html)

print(article.html)




#print(article.nlp())

