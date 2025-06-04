from gensim.models import KeyedVectors
import os
from src.utils import load_data, clean_text, tokenize_text
from src.train_model import train_model

model_dir = "/Users/keremoztopuz/word2vec_project/models"
model_path = os.path.join(model_dir, "wordvectors.kv")

#word_vectors = KeyedVectors.load(model_path, mmap='r')

def query(word, sentences, topn=5):
    word_vectors = train_model(sentences) 
    words = list(word_vectors.key_to_index.keys())

    dict1 = {}

    if word in word_vectors:
        similar_words = word_vectors.most_similar(word, topn=topn)
        for similar_words, similarity in similar_words:
            similarity = round(similarity, 2)
            dict1.update({similar_words: similarity})
            #print(f"{similar_words}: {similarity:.4f}")
    else:
        dict1 = f"Kelime bulunamadı: '{word}'"

    return dict1

