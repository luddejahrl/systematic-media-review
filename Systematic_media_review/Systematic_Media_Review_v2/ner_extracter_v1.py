import pandas as pd
import numpy as np
import csv
import time
import spacy

from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

import string
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English


#--------------------------------------------------------------------------------------------------------------------

#def ner_extract(data_hits)

data_hits = './Systematic_Media_Review_v2/classified_articles/classified_articles_hits_v1.csv'
data_out = './Systematic_Media_Review_v2/ner_extracted/ner_extracted_LDID_v1.csv'

#examples from twitter disatser data compition
test = pd.read_csv("./Systematic_Media_Review_v2/ner_train_data/test.csv")
train = pd.read_csv("./Systematic_Media_Review_v2/ner_train_data/train.csv")

X=train['text']
y=train['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

punctuations = string.punctuation

nlp = English()
stop_words = STOP_WORDS

parser = English()

# Basic tokenizer function
def spacy_tokenizer(sentence):
    mytokens = parser(sentence)
    # Lemmatization - rip words to their lemma equivalent
    mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]
    # Rip out the stop words and punctuations
    mytokens = [ word for word in mytokens if word not in stop_words and word not in punctuations ]
    return mytokens

# Simple transformer implementation to clean the text. 
# This might do something a bit more extensive in a real application like using https://pypi.org/project/tweet-preprocessor/
class TextPreprocessor(TransformerMixin):
    def transform(self, X, **transform_params):
        return [clean_text(text) for text in X]

    def fit(self, X, y=None, **fit_params):
        return self

    def get_params(self, deep=True):
        return {}

def clean_text(text):
    return text.strip().lower()

bow_vector = CountVectorizer(tokenizer = spacy_tokenizer, ngram_range=(1,1))
tfidf = TfidfTransformer()

classifier = LogisticRegression()

pipe = Pipeline([("cleaner", TextPreprocessor()),
                 ('vectorizer', bow_vector),
                 ('tfid', tfidf),
                 ('classifier', classifier)])

pipe.fit(X_train,y_train)

predicted = pipe.predict(X_test)
pred_1_or_0 = np.where(predicted>=0.5, 1, 0)
# Model Accuracy
print("Accuracy:",metrics.accuracy_score(y_test, predicted))
print("Precision:",metrics.precision_score(y_test, predicted))
print("Recall:",metrics.recall_score(y_test, predicted))
print("AUC:",metrics.roc_auc_score(y_test, pred_1_or_0))
print("AUC-PR:",metrics.average_precision_score(y_test, predicted))
print("F1:",metrics.f1_score(y_test, predicted))

#--------------------------------------------------------------------------------------------------------------------


# this link explains the meaning of different tags.
#https://web.archive.org/web/20190206204307/https://www.clips.uantwerpen.be/pages/mbsp-tags
#https://spacy.io/models

#def ner_extract(data_hits):

data_hits = './Systematic_Media_Review_v2/classified_articles/classified_articles_hits_v1.csv'

data_out = './Systematic_Media_Review_v2/ner_extracted/ner_extracted_LDID_v1.csv'

#convert csv to dataframe
df = pd.read_csv(data_hits) 

#numbers for display 
df_len = len(df)

#add colomns to dataframe: with NaN as default value
df["location"] = np.nan
df["deaths"] = np.nan
df["injuries"] = np.nan
df["demographic"] = np.nan

print("Added colomns for: 'Location', 'Deaths', 'Injuries', 'Demographic'")    

for index, row in df.iterrows():
    
    text_to_extract = str(row['text'])
    
    #print(text_to_extract)

    #new_row = pd.Series({'title': row['title'], 'url': row['url'], 'text': [retrieved_text]})
    #df_file_out = pd.concat([df_file_out, new_row.to_frame().T], ignore_index=True)
    
    #print(df_file_out)
    

    
    #one line due to \r
    print('Progress: ' + str(index+1) + '/' + str(df_len) + ' (' + str(round(((index+1)/(df_len)) * 100, 2)) + ' %)', end='\r')    
    



    
#return()    