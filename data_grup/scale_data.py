import re
import tarfile
from sklearn.feature_extraction.text import CountVectorizer


def clean_chat(text, banned_words=None):
    if banned_words is None:
        banned_words = set()

    cleaned_text = re.sub(r"[^a-zA-Z.,!?;:'\"()\[\]{}\-_/ ]+", "", text)
    cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()

    words = cleaned_text.split()
    cleaned_text = " ".join(word for word in words if word.lower() not in banned_words)
    return cleaned_text


def load_chat(nums_docs, banned_words=None):
    path = "data_grup.tar"
    with tarfile.open(path) as tar:
        datafile = tar.extractfile('data_grup.txt')
        content = datafile.read().decode('utf-8', errors='ignore')
        lines = content.splitlines()[:nums_docs]
        cleaned_text = [clean_chat(line, banned_words=banned_words) for line in lines]
        return cleaned_text

    
def make_matrix (docs, binary=False):
    vec = CountVectorizer(min_df=5,max_df=0.9,binary=binary)
    mtx = vec.fit_transform(docs)
    cols = [None] * len(vec.vocabulary_)
    for word, idx in vec.vocabulary_.items():
        cols[idx] = word
    return mtx, cols