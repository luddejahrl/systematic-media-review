import csv

import pandas as pd
import numpy as np

#/Users/luddejahrl/Desktop/Systematic_media_review/SMR_retrieved/OUTPUT_v4


df = pd.read_csv('/Users/luddejahrl/Desktop/Systematic_media_review/ML_prototype/nlp-getting-started/AG_news_News_articles/train_test_1_1.csv') 

df = df[df.label != 1]
df = df[df.label != 2]
df = df[df.label != 3]

df.to_csv('test_123x.csv', index=False)



print('DONE')