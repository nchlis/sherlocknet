#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: N.K.Chlis, https://github.com/nchlis
In this example there are some modifications to the code
- different input data
- CSVlogger callback
- splitting data into training and test sets
- deeper network
- saving model after each epoch

original code at: https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py
"""
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.callbacks import CSVLogger
from sklearn.model_selection import train_test_split
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

#%%  build the model: a 5 layer LSTM
print('Build model...')
model_id='LSTM_5x256_drop0.0'
model = Sequential()
model.add(LSTM(256, input_shape=(maxlen, len(chars)), return_sequences=True, dropout=0.4))
model.add(LSTM(256, return_sequences=True, dropout=0.0))
model.add(LSTM(256, return_sequences=True, dropout=0.0))
model.add(LSTM(256, return_sequences=True, dropout=0.0))
model.add(LSTM(256, dropout=0.0))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))
optimizer = 'adam'
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

csvlog = CSVLogger(model_id+'_train_log.csv',append=True)
model.summary()

#%% split into training and test sets
X_tr, X_ts, y_tr, y_ts = train_test_split(X, y, test_size=0.05, random_state=1)

#%% train the model, output generated text after each iteration
loss_hist=[]
val_loss_hist=[]
chars_to_print=400#characters to print after each epoch
for iteration in range(0, 100):
    print()
    print('-' * 50)
    print('Iteration', iteration)
    #print('Iteration', type(iteration))
    hst = model.fit(X_tr, y_tr, batch_size=128, epochs=iteration+1, initial_epoch=iteration,
                    callbacks=[csvlog], validation_data=(X_ts, y_ts))
    cur_loss=hst.history['loss'][0]
    cur_val_loss=hst.history['val_loss'][0]
    loss_hist.append(cur_loss)
    savepath=model_id+' epoch'+str(iteration)+' val_loss'+str(cur_val_loss)+'.h5'
    model.save(savepath)

    start_index = random.randint(0, len(text) - maxlen - 1)

    for diversity in [0.3]:
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
print()



