from bs4 import BeautifulSoup
import urllib
import re

site = urllib.urlopen('http://duckduckgo.com/html/?q=example ')
data = site.read()

parsed = BeautifulSoup(data)
topics = parsed.findAll('div', {'id': 'zero_click_topics'})[0]
results = topics.findAll('div', {'class': re.compile('results_*')})

print(results[0].text)