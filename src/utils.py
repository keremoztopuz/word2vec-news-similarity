import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print("no data file found")
    
def clean_text(df):
    df = df.lower()
    df = re.sub(r'[^\w\s]', '', df)
    df = re.sub(r'\s+', ' ', df).strip()
    return df

def tokenize_text(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]
    return tokens

print(len("/Users/keremoztopuz/word2vec_project/data/bbc_news.csv"))