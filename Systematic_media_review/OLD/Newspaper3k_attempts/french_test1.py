import csv
import newspaper
from newspaper import Config
from newspaper import news_pool

# implementation example
# https://stackoverflow.com/questions/64250654/newspaper3k-scrape-several-websites

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0'
# Mozilla/5.0 (Macintosh; Intel Mac OS X 12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36
# https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome

config = Config()
config.browser_user_agent = USER_AGENT
config.request_timeout = 10

#lm_paper = newspaper.build('https://www.lemonde.fr/', config=config, memoize_articles=False)
#parisien_paper = newspaper.build('https://www.leparisien.fr/', config=config, memoize_articles=False)
#french_papers = [lm_paper, parisien_paper]

# LIST of NEWS sites for RWANDA
# https://www.w3newspapers.com/rwanda/

#ENGLISH originl
new_times_paper = newspaper.build('https://www.newtimes.co.rw/', config=config, memoize_articles=False)
umuryango_paper = newspaper.build('https://www.umuryango.rw/eng/', config=config, memoize_articles=False)
# ktpress_paper = newspaper.build('https://www.ktpress.rw/', config=config, memoize_articles=False)
# hose_paper = newspaper.build('https://hose.rw/', config=config, memoize_articles=False)
# rwandatoday_paper = newspaper.build('https://rwandatoday.africa/', config=config, memoize_articles=False)
# therwandan_paper = newspaper.build('https://www.therwandan.com/', config=config, memoize_articles=False)

# #ENGLISH translated
# inyarwanda_paper = newspaper.build('https://eng.inyarwanda.com/', config=config, memoize_articles=False)
# igihe_paper = newspaper.build('https://www.en.igihe.com/', config=config, memoize_articles=False)
# ukwezi_paper = newspaper.build('http://en.ukwezi.rw/', config=config, memoize_articles=False)
# jambonews_paper = newspaper.build('https://www.jambonews.net/en/', config=config, memoize_articles=False)

# #FRENCH
# lerwandais_paper = newspaper.build('https://www.lerwandais.com/', config=config, memoize_articles=False)
# musabyimana_paper = newspaper.build('http://www.musabyimana.net/', config=config, memoize_articles=False)
# radiomaria_paper = newspaper.build('https://www.radiomaria.rw/', config=config, memoize_articles=False)
# rnanews_paper = newspaper.build('http://www.rnanews.com/', config=config, memoize_articles=False)

# #RWANDAN translated
# inyarwanda_rw_paper = newspaper.build('https://inyarwanda.com/', config=config, memoize_articles=False)
# igihe_rw_paper = newspaper.build('https://www.igihe.com/', config=config, memoize_articles=False)
# ukwezi_rw_paper = newspaper.build('http://ukwezi.rw/', config=config, memoize_articles=False)
# jambonews_rw_paper = newspaper.build('https://www.jambonews.net/rw/', config=config, memoize_articles=False)

# #RWANDAN original
# umuseke_paper = newspaper.build('https://www.umuseke.rw/', config=config, memoize_articles=False) 
# kigalitoday_paper = newspaper.build('https://www.kigalitoday.com/', config=config, memoize_articles=False)
# imvahonshya_paper = newspaper.build('https://imvahonshya.co.rw/', config=config, memoize_articles=False)
# rwandaises_paper = newspaper.build('https://rwandaises.com/', config=config, memoize_articles=False)
# rugali_paper = newspaper.build('https://rugali.com/', config=config, memoize_articles=False)
# intyoza_paper = newspaper.build('https://www.intyoza.com/', config=config, memoize_articles=False)
# rba_paper = newspaper.build('https://www.rba.co.rw/', config=config, memoize_articles=False)

#English paper pool
#english_papers = [new_times_paper, umuryango_paper, ktpress_paper, hose_paper, rwandatoday_paper, therwandan_paper]
#english_papers = [new_times_paper, umuryango_paper]
english_papers = [new_times_paper]

# this setting is adjustable 
news_pool.config.number_threads = 2

# this setting is adjustable 
news_pool.config.thread_timeout_seconds = 1

news_pool.set(english_papers)
news_pool.join()

# Define the structure of the data
test_header = ['article_title']

# 1. Open a new CSV file
with open('french_test1_v3.csv', 'w', encoding="UTF8") as file:
    # 2. Create a CSV writer
    writer = csv.writer(file)

    # 3. Write data to the file
    writer.writerow(test_header)

    for source in english_papers:
        for article_extract in source.articles:
            if article_extract:
                article_extract.parse()
                print(article_extract.url)
                #writer.writerow(article_extract.url)
                
print("DONE")
                
                
