#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: N.K.Chlis, https://github.com/nchlis
In this example we use a model trained and saved with sherlocknet_train.py
in order to generate new text.

the code in this example is based on the keras lstm text generation example
original code at: https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py
"""

from keras.models import load_model
#from keras.optimizers import RMSprop
#from keras.utils.data_utils import get_file
import numpy as np
import random
import sys

def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

#%% load the data

#sherlock holmes books available on project gutenberg
#at https://www.gutenberg.org/
#8 books were concatenated into one .txt file
#the header and footer (added by project gutenberg) of each book were removed
#before concatenation, since they are irrelevant to the learning process.
path = './sherlock/edited_texts/all_sherlock_books.txt'
text = open(path).read().lower()
print('corpus length:', len(text))

chars = sorted(list(set(text)))
print('total chars:', len(chars))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))

# cut the text in semi-redundant sequences of maxlen characters
maxlen = 30
step = 1
sentences = []
next_chars = []
for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
print('nb sequences:', len(sentences))

print('Vectorization...')
X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

#%%load the trained model

model=load_model('LSTM_5x256_drop0.0 epoch41 val_loss1.16370713811.h5')
print('model loaded')

#%%generate new text

chars_to_print=800#characters to print after each epoch
start_index = random.randint(0, len(text) - maxlen - 1)
for diversity in [0.5, 0.7]:
    print()
    print('----- diversity:', diversity)

    generated = ''
    sentence = text[start_index: start_index + maxlen]
    generated += sentence
    print('----- Generating with seed: "' + sentence + '"')
    sys.stdout.write(generated)

    for i in range(chars_to_print):
        x = np.zeros((1, maxlen, len(chars)))
        for t, char in enumerate(sentence):
            x[0, t, char_indices[char]] = 1.

        preds = model.predict(x, verbose=0)[0]
        next_index = sample(preds, diversity)
        next_char = indices_char[next_index]

        generated += next_char
        sentence = sentence[1:] + next_char

        sys.stdout.write(next_char)
        sys.stdout.flush()




















