


# http://blog.newsapi.ai/simplifying-the-data-access-with-iterators/
# https://eventregistry.org/intelligence?tab=items&searchMode=simple&type=articles&conditions=2--1-1-rwanda&categories=9-dmoz%2FSociety-dmoz:Society&dateStart=2022-09-11&dateEnd=2022-10-12&percentile=100&forceMaxDataTimeWindow=31&lang=eng&dataType=news

from eventregistry import * 

er = EventRegistry(apiKey = "c71254cc-3c50-4e8b-b424-b53c3e256197")
q = QueryArticlesIter(conceptUri = er.getConceptUri("George Clooney")) 
for art in q.execQuery(er): 
    print(art) 	# do something with the article here