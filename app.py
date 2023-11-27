#!/usr/bin/env python
# coding: utf-8

# In[2]:


# app.py
from flask import Flask, render_template, request
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist

import nltk
nltk.download('stopwords')

app = Flask(__name__)

def preprocess_text(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word.lower() not in stop_words]

    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    return sentences, words

def extractive_summarization(sentences, words, num_sentences=3):
    word_freq = FreqDist(words)
    sentence_scores = {sentence: sum(word_freq[word] for word in word_tokenize(sentence.lower())) for sentence in sentences}

    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    summary = ' '.join(sorted_sentences[:num_sentences])

    return summary

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarizer():
    if request.method == 'POST':
        user_input = request.form['document']
        sentences, words = preprocess_text(user_input)
        summary = extractive_summarization(sentences, words)
        return render_template('index.html', document=user_input, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




