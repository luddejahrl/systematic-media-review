import newspaper
from newspaper import Article
from newspaper import news_pool

cnn_paper = newspaper.build('http://cnn.com')

print(cnn_paper.size())

# new_times_paper = newspaper.build('https://www.newtimes.co.rw/')
# umuryango_paper = newspaper.build('https://umuryango.rw/eng/')

# for article in new_times_paper.articles:
#     print(article.url)
    
# #article = Article(cnn_paper.url)
# #article.download()
# #article.parse()
# #print(article.text)

# slate_paper = newspaper.build('http://slate.com')
# tc_paper = newspaper.build('http://techcrunch.com')
# espn_paper = newspaper.build('http://espn.com')

# papers = [slate_paper, tc_paper, espn_paper]
# news_pool.set(papers, threads_per_source=2) # (3*2) = 6 threads total
# news_pool.join()

# print(slate_paper.articles[10].html)
# print("hello")