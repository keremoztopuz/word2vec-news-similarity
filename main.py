import os
from gensim.models import KeyedVectors
from src.utils import load_data, clean_text, tokenize_text
from src.train_model import train_model
from src.query_model import query

def main():
    filepath = "/Users/keremoztopuz/word2vec_project/data/bbc_news.csv"
    df = load_data(filepath)
    if df is None:
        exit()

    df['clean_text'] = df['description'].apply(clean_text)
    df['tokens'] = df['clean_text'].apply(tokenize_text)

    sentences = df['tokens'].to_list()

    word_vectors = train_model(sentences)

    model_dir = "/Users/keremoztopuz/word2vec_project/models"
    os.makedirs(model_dir, exist_ok=True)
    word_vectors.save(os.path.join(model_dir, "wordvectors.kv"))

    result = query(word=(input("enter your word:")),sentences=sentences)
    return result

if __name__ == "__main__":
    main()
    
