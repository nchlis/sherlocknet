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
path = 'all_sherlock_books.txt'
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

#%% split into training and test sets
X_tr, X_ts, y_tr, y_ts = train_test_split(X, y, test_size=0.05, random_state=1)
del(X,y)#original copy of the dataset no longer needs to be in memory

#%%  build the model: a 2-layer LSTM
dropout=0.2
print('Build model...')
model_id='LSTM_2x438_drop'+str(dropout)
model = Sequential()
model.add(LSTM(438, input_shape=(maxlen, len(chars)), return_sequences=True, dropout=dropout))
model.add(LSTM(438, dropout=dropout))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))
optimizer = 'adam'
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

csvlog = CSVLogger(model_id+'_train_log.csv',append=True)#save training progress in a .csv
model.summary()#print model summary, also number of parameters

#%% train the model, output generated text after each iteration
loss_hist=[]
val_loss_hist=[]
chars_to_print=400#characters to print after each epoch
file = "generated_text.txt"#file to save the generated text
save_to_file = False#if False, only show output to screen
max_epochs=50#maximum number of epochs to train the model

#some times "RuntimeWarning: divide by zero encountered in log"
#is written in the generated text, suppress warnings to avoid this.
#warnings.filterwarnings("ignore")

for iteration in range(0, max_epochs):
    print()
    print('-' * 50)
    print('Iteration', iteration)
    #print('Iteration', type(iteration))
    hst = model.fit(X_tr, y_tr, batch_size=512, epochs=iteration+1, initial_epoch=iteration,
                    callbacks=[csvlog], validation_data=(X_ts, y_ts))
    cur_loss=hst.history['loss'][0]
    cur_val_loss=hst.history['val_loss'][0]
    loss_hist.append(cur_loss)
    savepath=model_id+' epoch'+str(iteration)+' val_loss'+str(cur_val_loss)+'.h5'
    model.save(savepath)
    
    for diversity in [0.3, 0.5]:
        print()
        print()
        print('===== diversity:', diversity,'=====',file=sys.stdout)
        if(save_to_file==True):
            print('',file=open(file, "a"))
            print('',file=open(file, "a"))
            print('===== diversity:', diversity,'=====',file=open(file, "a"))
            
    
        generated = ''
        sentence = '.'*maxlen
        generated += sentence
        print(generated)
    
        for i in range(chars_to_print):
            x = np.zeros((1, maxlen, len(indices_char)))
            for t, char in enumerate(sentence):
                x[0, t, char_indices[char]] = 1.
    
            preds = model.predict(x, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_char = indices_char[next_index]
    
            generated += next_char
            sentence = sentence[1:] + next_char
            print(next_char, end='',file=sys.stdout)      
            if(save_to_file==True):
                print(next_char, end='',file=open(file, "a"))



