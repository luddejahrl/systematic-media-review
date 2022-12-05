import nltk
from newspaper import Article
# select a url of any news article

# https://www.newtimes.co.rw/news/two-killed-suspected-fln-attack-nyungwe
url = 'https://www.newtimes.co.rw/news/two-killed-suspected-fln-attack-nyungwe'

#url = 'https://www.indiatoday.in/india/story/heavy-rain-strong-winds-storm-bengaluru-latest-updates-may-24-1681398-2020-05-24'
article = Article(url)

article.download()
article.parse()
nltk.download('punkt')
article.nlp()

article.authors

article.publish_date

print(article.text)