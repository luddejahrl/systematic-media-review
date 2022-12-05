# The purpose of this script is to train and subsequently then classify a news article 
# as RELEVANT or NOT RELEVANT for mass truama 

# Code based on:
# https://medium.com/analytics-vidhya/nlp-tutorial-for-text-classification-in-python-8f19cd17b49e

#------------------------------------------------Importing Libraries------------------------------------------------

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#for text pre-processing
import re, string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

from pandas import DataFrame as df

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')

#for model-building
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.metrics import roc_curve, auc, roc_auc_score

# bag of words
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

#for word embedding
import gensim
from gensim.models import Word2Vec

#importing datasets
#df_train = pd.read_csv('../input/nlp-getting-started/train.csv') # 7,613 tweets in training (labelled) dataset
#df_test = pd.read_csv('../input/nlp-getting-started/test.csv') # 3,263 in the test(unlabelled) dataset

#------------------------------------------------Loading the datasets------------------------------------------------

#/Users/luddejahrl/Desktop/Systematic_media_review/ML_prototype/
df_train = pd.read_csv('/Users/luddejahrl/Desktop/Systematic_media_review/ML_prototype/nlp-getting-started/train.csv') # 7,613 tweets in training (labelled) dataset
df_test = pd.read_csv('/Users/luddejahrl/Desktop/Systematic_media_review/ML_prototype/nlp-getting-started/test.csv') # 3,263 in the test(unlabelled) dataset

#------------------------------------------Exploratory Data Analysis (EDA)--------------------------------------------

# Class distribution: There are more tweets with class 0 
# ( no disaster) than class 1 ( disaster tweets). We can 
# say that the dataset is relatively balanced with 4342 
# non-disaster tweets (57%) and 3271 disaster tweets (43%). 
# Since the data is balanced, we won’t be applying data-balancing 
# techniques like SMOTE while building the model.

x = df_train['target'].value_counts()
print(x)
y = x.index
#sns.barplot(x.index,x)

#------------------------------------------------Missing values: ------------------------------------------------
# We have ~2.5k missing values in location field and 61 missing values in keyword column

df_train.isna().sum()


#------------------------------------------Number of words in a tweet: ------------------------------------------
# Disaster tweets are more wordy than the non-disaster tweets

# WORD-COUNT
df_train['word_count'] = df_train['text'].apply(lambda x: len(str(x).split()))
print(df_train[df_train['target']==1]['word_count'].mean()) #Disaster tweets
print(df_train[df_train['target']==0]['word_count'].mean()) #Non-Disaster tweets

# The average number of words in a disaster tweet is 15.17 as 
# compared to an average of 14.7 words in a non-disaster tweet

# PLOTTING WORD-COUNT
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,4))
train_words=df_train[df_train['target']==1]['word_count']
ax1.hist(train_words,color='red')
ax1.set_title('Disaster tweets')
train_words=df_train[df_train['target']==0]['word_count']
ax2.hist(train_words,color='green')
ax2.set_title('Non-disaster tweets')
fig.suptitle('Words per tweet')
plt.show()

##------------------------------------------Number of characters in a tweet: #------------------------------------------
# Disaster tweets are longer than the non-disaster tweets

# CHARACTER-COUNT
df_train['char_count'] = df_train['text'].apply(lambda x: len(str(x)))
print(df_train[df_train['target']==1]['char_count'].mean()) #Disaster tweets
print(df_train[df_train['target']==0]['char_count'].mean()) #Non-Disaster tweets

# The average characters in a disaster tweet is 108.1 as 
# compared to an average of 95.7 characters in a non-disaster tweet



# #------------------------------------------Text Pre-Processing ------------------------------------------
# Before we move to model building, we need to preprocess our dataset by removing punctuations 
# & special characters, cleaning texts, removing stop words, and applying lemmatization

# Simple text cleaning processes: Some of the common text cleaning process involves:
# Removing punctuations, special characters, URLs & hashtags
# Removing leading, trailing & extra white spaces/tabs
# Typos, slangs are corrected, abbreviations are written in their long forms

#/
# Stop-word removal: We can remove a list of generic stop words from the English vocabulary using nltk. 
# A few such words are ‘i’,’you’,’a’,’the’,’he’,’which’ etc.

# Stemming: Refers to the process of slicing the end or the beginning of words with the intention 
# of removing affixes(prefix/suffix)

# Lemmatization: It is the process of reducing the word to its base form
#/

# INITIAL pre-processing
#convert to lowercase, strip and remove punctuations
def preprocess(text):
    text = text.lower() 
    text=text.strip()  
    text=re.compile('<.*?>').sub('', text) 
    text = re.compile('[%s]' % re.escape(string.punctuation)).sub(' ', text)  
    text = re.sub('\s+', ' ', text)  
    text = re.sub(r'\[[0-9]*\]',' ',text) 
    text=re.sub(r'[^\w\s]', '', str(text).lower().strip())
    text = re.sub(r'\d',' ',text) 
    text = re.sub(r'\s+',' ',text) 
    return text

 
# STOPWORD REMOVAL
def stopword(string):
    a= [i for i in string.split() if i not in stopwords.words('english')]
    return ' '.join(a)

#LEMMATIZATION
# Initialize the lemmatizer
wl = WordNetLemmatizer()
 
# This is a helper function to map NTLK position tags
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
    
# Tokenize the sentence
def lemmatizer(string):
    word_pos_tags = nltk.pos_tag(word_tokenize(string)) # Get position tags
    a=[wl.lemmatize(tag[0], get_wordnet_pos(tag[1])) for idx, tag in enumerate(word_pos_tags)] # Map the position tag and lemmatize the word/token
    return " ".join(a)

# FINAL pre-processing
def finalpreprocess(string):
    return lemmatizer(stopword(preprocess(string)))
df_train['clean_text'] = df_train['text'].apply(lambda x: finalpreprocess(x))
df_train.head()

#------------------------------------------Extracting vectors from text (Vectorization)------------------------------------------
# It’s difficult to work with text data while building Machine learning models since 
# these models need well-defined numerical data. The process to convert text data into 
# numerical data/vector, is called vectorization or in the NLP world, word embedding. Bag-of-Words(BoW) and 
# Word Embedding (with Word2Vec) are two well-known methods for converting text data to numerical data.

# There are a few versions of Bag of Words, corresponding to different words scoring methods. 
# We use the Sklearn library to calculate the BoW numerical values using these approaches

#------------------------------------------------------- Count vectors: -----------------------------------------
# It builds a vocabulary from a corpus of documents and counts how many times the words appear in each document

# Term Frequency-Inverse Document Frequencies (tf-Idf): Count vectors might not be the best representation for 
# converting text data to numerical data. So, instead of simple counting, we can also use an advanced variant of 
# the Bag-of-Words that uses the term frequency–inverse document frequency (or Tf-Idf). Basically, the value of a 
# word increases proportionally to count in the document, but it is inversely proportional to the frequency of the 
# word in the corpus

# Word2Vec: One of the major drawbacks of using Bag-of-words techniques is that it can’t capture the meaning or 
# relation of the words from vectors. Word2Vec is one of the most popular technique to learn word embeddings using 
# shallow neural network which is capable of capturing context of a word in a document, semantic and syntactic 
# similarity, relation with other words, etc.

# We can use any of these approaches to convert our text data to numerical form which will be used to build the
# classification model. With this in mind, I am going to first partition the dataset into training set 
# (80%) and test set (20%) using the below-mentioned code

#SPLITTING THE TRAINING DATASET INTO TRAIN AND TEST
X_train, X_test, y_train, y_test = train_test_split(df_train["clean_text"],df_train["target"],test_size=0.2,shuffle=True)

#Word2Vec
# Word2Vec runs on tokenized sentences
X_train_tok= [nltk.word_tokenize(i) for i in X_train]  
X_test_tok= [nltk.word_tokenize(i) for i in X_test]

# vectorization using Bag-of-Words (with Tf-Idf ) and Word2Vec
#Tf-Idf
tfidf_vectorizer = TfidfVectorizer(use_idf=True)
X_train_vectors_tfidf = tfidf_vectorizer.fit_transform(X_train) 
X_test_vectors_tfidf = tfidf_vectorizer.transform(X_test)

#building Word2Vec model
class MeanEmbeddingVectorizer(object):
    def __init__(self, word2vec):
        self.word2vec = word2vec
        # if a text is empty we should return a vector of zeros
        # with the same dimensionality as all the other vectors
        self.dim = len(next(iter(word2vec.values())))
        
def fit(self, X, y):
        return self
    
def transform(self, X):
        return np.array([
            np.mean([self.word2vec[w] for w in words if w in self.word2vec]
                    or [np.zeros(self.dim)], axis=0)
            for words in X
        ])
        
w2v = dict(zip(model.wv.index2word, model.wv.syn0)) 
df['clean_text_tok']=[nltk.word_tokenize(i) for i in df['clean_text']]
model = Word2Vec(df['clean_text_tok'],min_count=1)     
modelw = MeanEmbeddingVectorizer(w2v)

# converting text to numerical data using Word2Vec
X_train_vectors_w2v = modelw.transform(X_train_tok)
X_val_vectors_w2v = modelw.transform(X_test_tok)

#------------------------------------------------  ML algorithms ------------------------------------------------
# It’s time to train a machine learning model on the vectorized dataset and test it. Now that we have 
# converted the text data to numerical data, we can run ML models on X_train_vector_tfidf & y_train. 
# We’ll test this model on X_test_vectors_tfidf to get y_predict and further evaluate the performance of the model


#------------------------------------------------ Logistic Regression: -----------------------------------------------------
# We will start with the most simplest one Logistic Regression. You can easily build a LogisticRegression in scikit using below lines of code

#FITTING THE CLASSIFICATION MODEL using Logistic Regression(tf-idf)
lr_tfidf=LogisticRegression(solver = 'liblinear', C=10, penalty = 'l2')
lr_tfidf.fit(X_train_vectors_tfidf, y_train)  

#Predict y value for test dataset
y_predict = lr_tfidf.predict(X_test_vectors_tfidf)
y_prob = lr_tfidf.predict_proba(X_test_vectors_tfidf)[:,1]
print(classification_report(y_test,y_predict))
print('Confusion Matrix:',confusion_matrix(y_test, y_predict))
 
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)
print('AUC:', roc_auc)

#FITTING THE CLASSIFICATION MODEL using Logistic Regression (W2v)
lr_w2v=LogisticRegression(solver = 'liblinear', C=10, penalty = 'l2')
lr_w2v.fit(X_train_vectors_w2v, y_train)  #model
#Predict y value for test dataset
y_predict = lr_w2v.predict(X_test_vectors_w2v)
y_prob = lr_w2v.predict_proba(X_test_vectors_w2v)[:,1]
print(classification_report(y_test,y_predict))
print('Confusion Matrix:',confusion_matrix(y_test, y_predict))
 
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)
print('AUC:', roc_auc)

#------------------------------------------------Naive Bayes: ------------------------------------------------
# It’s a probabilistic classifier that makes use of Bayes’ Theorem, a rule that uses probability to make 
# predictions based on prior knowledge of conditions that might be related

#FITTING THE CLASSIFICATION MODEL using Naive Bayes(tf-idf)
nb_tfidf = MultinomialNB()
nb_tfidf.fit(X_train_vectors_tfidf, y_train)  

#Predict y value for test dataset
y_predict = nb_tfidf.predict(X_test_vectors_tfidf)
y_prob = nb_tfidf.predict_proba(X_test_vectors_tfidf)[:,1]
print(classification_report(y_test,y_predict))
print('Confusion Matrix:',confusion_matrix(y_test, y_predict))
 
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)
print('AUC:', roc_auc)

# One can now select the best model (lr_tfidf in our case) to estimate ‘target’ values for the 
# unlabelled dataset (df_test). 

#Pre-processing the new dataset
df_test['clean_text'] = df_test['text'].apply(lambda x: finalpreprocess(x)) #preprocess the data
X_test=df_test['clean_text'] 

#converting words to numerical data using tf-idf
X_vector=tfidf_vectorizer.transform(X_test)

#use the best model to predict 'target' value for the new dataset 
y_predict = lr_tfidf.predict(X_vector)      
y_prob = lr_tfidf.predict_proba(X_vector)[:,1]
df_test['predict_prob']= y_prob
df_test['target']= y_predict
final=df_test[['clean_text','target']].reset_index(drop=True)
print(final.head())