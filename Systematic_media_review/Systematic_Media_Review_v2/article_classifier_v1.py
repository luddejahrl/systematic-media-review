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

nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

#for model-building
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
from sklearn.metrics import roc_curve, auc, roc_auc_score

# bag of words
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

#for word embedding
import gensim
from gensim.models import Word2Vec #Word2Vec is mostly used for huge datasets
#import os

def classifier(current_corpus):

    #/Users/luddejahrl
    #os.chdir('/Users/luddejahrl/Desktop/')

    df_train = pd.read_csv('./Systematic_Media_Review_v2/data/pos_training_data.csv') 
    
    #final classified csv outputs:
    classified_csv = './Systematic_Media_Review_v2/classified_articles/classified_articles_v1.csv'
    classified_csv_hits = './Systematic_Media_Review_v2/classified_articles/classified_articles_hits_v1.csv'

    # articless in training (labelled) dataset
    print(df_train.shape)
    df_train.head()
    print(df_train.head())

    ## CLASS DISTRIBUTION
    #if dataset is balanced or not
    # .value_counts()  -> . Return a Series containing counts of unique rows in the DataFrame.
    x = df_train['target'].value_counts()
    print(x)
    
    print('\nShow barplot? ')
    val_show_plot_1 = input("y/n: ")
    if(val_show_plot_1 == "y" or val_show_plot_1 == "Y"):
        # SHOW PLOT
        sns.barplot(x.index,x)
        plt.show()
    else:
        print('\nNo plot shown')
    
    #Missing values
    df_train.isna().sum()

    #1. WORD-COUNT
    df_train['word_count'] = df_train['text'].apply(lambda x: len(str(x).split()))
    print('\nWORD-COUNT')
    print("mass-trauma articless", df_train[df_train['target']==1]['word_count'].mean()) #mass-trauma articless
    print("Non-mass-trauma articless", df_train[df_train['target']==0]['word_count'].mean()) #Non-mass-trauma articless

    #mass-trauma articless are more wordy than the non-mass-trauma articless




    #2. CHARACTER-COUNT
    df_train['char_count'] = df_train['text'].apply(lambda x: len(str(x)))
    print('\nCHARACTER-COUNT')
    print("mass-trauma articless", df_train[df_train['target']==1]['char_count'].mean()) #mass-trauma articless
    print("Non-mass-trauma articless", df_train[df_train['target']==0]['char_count'].mean()) #Non-mass-trauma articless

    #mass-trauma articless are longer than the non-mass-trauma articless


    #3. UNIQUE WORD-COUNT
    df_train['unique_word_count'] = df_train['text'].apply(lambda x: len(set(str(x).split())))
    print('\nUNIQUE WORD-COUNT')
    print("mass-trauma articless", df_train[df_train['target']==1]['unique_word_count'].mean()) #mass-trauma articles
    print("Non-mass-trauma articless", df_train[df_train['target']==0]['unique_word_count'].mean()) #Non-mass-trauma articles
    print('\n')

    ## Plotting word-count per articles
    fig,(ax1,ax2)=plt.subplots(1,2,figsize=(10,4))
    train_words=df_train[df_train['target']==1]['word_count']
    ax1.hist(train_words,color='red')
    ax1.set_title('mass-trauma articles')
    train_words=df_train[df_train['target']==0]['word_count']
    ax2.hist(train_words,color='green')
    ax2.set_title('Non-mass-trauma articles')
    fig.suptitle('Words per articles')


    print('\nShow word count per article plot? ')
    val_show_plot_2 = input("y/n: ")
    if(val_show_plot_2 == "y" or val_show_plot_2 == "Y"):
        # SHOW PLOT - word count per articles
        plt.show()
    else:
        print('\nNo plot shown')
    

    #1. Common text preprocessing
    #text = "   This is a message to be cleaned. It may involve some things like: , ?, :, ''  adjacent spaces and tabs     .  "

    #convert to lowercase and remove punctuations and characters and then strip
    def preprocess(text):
        text = text.lower() #lowercase text
        text = text.strip() #get rid of leading/trailing whitespace 
        text = re.compile('<.*?>').sub('', text) #Remove HTML tags/markups
        text = re.compile('[%s]' % re.escape(string.punctuation)).sub(' ', text)  #Replace punctuation with space. Careful since punctuation can sometime be useful
        text = re.sub('\s+', ' ', text)  #Remove extra space and tabs
        text = re.sub(r'\[[0-9]*\]',' ',text) #[0-9] matches any digit (0 to 10000...)
        text = re.sub(r'[^\w\s]', '', str(text).lower().strip())
        text = re.sub(r'\d',' ',text) #matches any digit from 0 to 100000..., \D matches non-digits
        text = re.sub(r'\s+',' ',text) #\s matches any whitespace, \s+ matches multiple whitespace, \S matches non-whitespace 
        
        return text

    #text = preprocess(text)
    #print(text)  #text is a string

    #3. LEXICON-BASED TEXT PROCESSING EXAMPLES

    #1. STOPWORD REMOVAL
    def stopword(string):
        a= [i for i in string.split() if i not in stopwords.words('english')]
        return ' '.join(a)

    #text=stopword(text)
    #print(text)

    #2. STEMMING
    
    # Initialize the stemmer
    snow = SnowballStemmer('english')
    def stemming(string):
        a=[snow.stem(i) for i in word_tokenize(string) ]
        return " ".join(a)

    #text=stemming(text)
    #print(text)



    #3. LEMMATIZATION
    # Initialize the lemmatizer
    wl = WordNetLemmatizer()
    
    
    

    # This is a helper function to map NTLK position tags
    # Full list is available here: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
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

    #text = lemmatizer(text)
    #print(text)



    #FINAL PREPROCESSING
    def finalpreprocess(string):
        return lemmatizer(stopword(preprocess(string)))

    df_train['clean_text'] = df_train['text'].apply(lambda x: finalpreprocess(x))
    df_train=df_train.drop(columns=['word_count','char_count','unique_word_count'])
    df_train.head()



    # create Word2vec model
    #here words_f should be a list containing words from each document. say 1st row of the list is words from the 1st document/sentence
    #length of words_f is number of documents/sentences in your dataset
    df_train['clean_text_tok']=[nltk.word_tokenize(i) for i in df_train['clean_text']] #convert preprocessed sentence to tokenized sentence
    model = Word2Vec(df_train['clean_text_tok'],min_count=1)  #min_count=1 means word should be present at least across all documents,
    #if min_count=2 means if the word is present less than 2 times across all the documents then we shouldn't consider it


    w2v = dict(zip(model.wv.index_to_key, model.wv.vectors))  #combination of word and its vector
    #w2v = dict(zip(model.wv.index2word, model.wv.syn0))


    #for converting sentence to vectors/numbers from word vectors result by Word2Vec
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
            
            #SPLITTING THE TRAINING DATASET INTO TRAINING AND VALIDATION
    
    
    
    # Input: "reviewText", "rating" and "time"
    # Target: "log_votes"
    X_train, X_val, y_train, y_val = train_test_split(df_train["clean_text"], df_train["target"], test_size=0.2, shuffle=True)
    X_train_tok= [nltk.word_tokenize(i) for i in X_train]  #for word2vec
    X_val_tok= [nltk.word_tokenize(i) for i in X_val]      #for word2vec



    #TF-IDF
    # Convert x_train to vector since model can only run on numbers and not words- Fit and transform
    tfidf_vectorizer = TfidfVectorizer(use_idf=True)
    X_train_vectors_tfidf = tfidf_vectorizer.fit_transform(X_train) #tfidf runs on non-tokenized sentences unlike word2vec
    # Only transform x_test (not fit and transform)
    X_val_vectors_tfidf = tfidf_vectorizer.transform(X_val) #Don't fit() your TfidfVectorizer to your test data: it will 
    #change the word-indexes & weights to match test data. Rather, fit on the training data, then use the same train-data-
    #fit model on the test data, to reflect the fact you're analyzing the test data only based on what was learned without 
    #it, and the have compatible


    #Word2vec
    # Fit and transform
    modelw = MeanEmbeddingVectorizer(w2v)
    X_train_vectors_w2v = modelw.transform(X_train_tok)
    X_val_vectors_w2v = modelw.transform(X_val_tok)




    #FITTING THE CLASSIFICATION MODEL using Logistic Regression(tf-idf)

    lr_tfidf=LogisticRegression(solver = 'liblinear', C=10, penalty = 'l2')
    lr_tfidf.fit(X_train_vectors_tfidf, y_train)  #model

    #Predict y value for test dataset
    y_predict = lr_tfidf.predict(X_val_vectors_tfidf)
    y_prob = lr_tfidf.predict_proba(X_val_vectors_tfidf)[:,1]
    
    print('Logistic Regression(tf-idf)')
    print(classification_report(y_val,y_predict))
    print('Confusion Matrix:',confusion_matrix(y_val, y_predict))
    
    fpr, tpr, thresholds = roc_curve(y_val, y_prob)
    roc_auc = auc(fpr, tpr)
    print('AUC:', roc_auc)  





    #FITTING THE CLASSIFICATION MODEL using Naive Bayes(tf-idf)
    #It's a probabilistic classifier that makes use of Bayes' Theorem, a rule that uses probability to make predictions based on prior knowledge of conditions that might be related. This algorithm is the most suitable for such large dataset as it considers each feature independently, calculates the probability of each category, and then predicts the category with the highest probability.

    nb_tfidf = MultinomialNB()
    nb_tfidf.fit(X_train_vectors_tfidf, y_train)  #model

    #Predict y value for test dataset
    y_predict = nb_tfidf.predict(X_val_vectors_tfidf)
    y_prob = nb_tfidf.predict_proba(X_val_vectors_tfidf)[:,1]
    
    print('Naive Bayes(tf-idf)')
    print(classification_report(y_val,y_predict))
    print('Confusion Matrix:',confusion_matrix(y_val, y_predict))
    
    fpr, tpr, thresholds = roc_curve(y_val, y_prob)
    roc_auc = auc(fpr, tpr)
    print('AUC:', roc_auc)  



    #FITTING THE CLASSIFICATION MODEL using Logistic Regression (W2v)
    lr_w2v=LogisticRegression(solver = 'liblinear', C=10, penalty = 'l2')
    lr_w2v.fit(X_train_vectors_w2v, y_train)  #model

    #Predict y value for test dataset
    y_predict = lr_w2v.predict(X_val_vectors_w2v)
    y_prob = lr_w2v.predict_proba(X_val_vectors_w2v)[:,1]
    

    print(classification_report(y_val,y_predict))
    print('Confusion Matrix:',confusion_matrix(y_val, y_predict))
    
    fpr, tpr, thresholds = roc_curve(y_val, y_prob)
    roc_auc = auc(fpr, tpr)
    print('AUC:', roc_auc)  


    #Testing it on new dataset with the best model
    #df_test=pd.read_csv('test.csv')  #reading the data
    #df_test = pd.read_csv('/Users/luddejahrl/Desktop/Systematic_media_review/ML_prototype/nlp-getting-started/test.csv') #reading the data
    df_test = pd.read_csv(current_corpus)
    df_test['clean_text'] = df_test['text'].apply(lambda x: finalpreprocess(x)) #preprocess the data
    X_test = df_test['clean_text'] 

    X_vector = tfidf_vectorizer.transform(X_test) # converting X_test to vector
    y_predict = lr_tfidf.predict(X_vector)        # use the trained model on X_vector
    y_prob = lr_tfidf.predict_proba(X_vector)[:,1]

    # X_vector = tfidf_vectorizer.transform(X_test) # converting X_test to vector
    # y_predict = lr_tfidf.predict(X_vector)        # use the trained model on X_vector
    # y_prob = lr_tfidf.predict_proba(X_vector)[:,1]

    df_test['predict_prob'] = y_prob
    df_test['target'] = y_predict
    print(df_test.head())

    #final=df_test[['id','target']].reset_index(drop=True)

    final = df_test
    final.to_csv(classified_csv, index=False)

    final[final.target != 0].to_csv(classified_csv_hits, index=False)
    
    print('\nArticles classified as Relevant: ' + str(len(classified_csv_hits)) + ' | Articles classified as Non-Relevant: ' + str(len(df_test) - len(classified_csv_hits)))
    
    print('\nClassification DONE\n') 
    
    return(classified_csv_hits)


