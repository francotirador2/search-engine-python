from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem.porter import PorterStemmer

import os 


stop_words = set(stopwords.words('english')) 
  
def clean(text):
    word_tokens = word_tokenize(text) 
    word_tokens = [w for w in word_tokens if w.isalpha()]
    word_tokens = [w.lower() for w in word_tokens if not w in stop_words]
    stemmer = PorterStemmer()
    word_tokens = [stemmer.stem(w) for w in word_tokens]
    return word_tokens




