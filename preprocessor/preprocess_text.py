#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
================================================
Project:    <Sentiment Analytics>
Module:     <Pre-Process-Text>
Author:     <Sven Bodemer>
================================================
Contact:    <sbodemer.student@gmail.com>

NLP pre-processing stuff with spaCy Lemmatizer
================================================
"""
import spacy
import emoji
from time import time
from data.load_files import read_stopwords

nlp = spacy.load('de')

STOPWORDS_DE = set(read_stopwords("stopwords.txt"))


def spacy_preprocessor(txt):
    t0 = time()
    tokens = nlp(txt)
    tokens = [tok.lemma_.lower().strip() if tok.lemma_ != "-PRON-" else tok.lower_ for tok in tokens]
    EMOJI = [c for c in tokens if c in emoji.UNICODE_EMOJI]
    LINKS = [w for w in tokens if w.startswith('http') or w.startswith('www') or w.startswith('.')]
    tokens = [t for t in tokens if len(t) > 1]
    tokens = [t for t in tokens if t not in STOPWORDS_DE and t not in LINKS]
    tokens.extend(EMOJI)
    train_time = time() - t0
    return tokens, train_time


if __name__ == '__main__':
    sample = 'Musst du ausgerechnet Pommes essen, wenn man gerade keine da hat 😈 ! ' \
             '# ++ & $% https://www.spacy.com/234bhrtzngh ✖ '

    res, t = spacy_preprocessor(sample)
    print('spaCy: pre-process time: %0.3fs' % t)
    print('spaCy: ', res)