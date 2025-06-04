from gensim.models import Word2Vec
import nltk
import os

def train_model(sentences, vector_size=100, window=5, min_count=1, workers=4):
    nltk.data.path.append('/Users/keremoztopuz/nltk_data')
    model = Word2Vec(
        sentences=sentences,
        vector_size=vector_size,
        window=window,
        min_count=min_count,
        workers=workers
    )
    sentences = model.wv
    return model.wv

