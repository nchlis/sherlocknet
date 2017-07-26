#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
author: N.K.Chlis, https://github.com/nchlis
In this example we use a model trained and saved with sherlocknet_train.py
in order to generate new text.
"""

from keras.models import load_model
#from keras.optimizers import RMSprop
#from keras.utils.data_utils import get_file
import numpy as np
import sys
import warnings
np.random.seed(1)#set the random seed

#sample function original found at the corresponding keras example at
#https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py
def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

#%%load the trained model

model=load_model('LSTM_2x438_drop0.0 epoch34 val_loss1.11933625518.h5')
print('model loaded')

maxlen = int(model.input.shape[1]) #length of each character sequence
char_indices = np.load('char_indices.npy').item()#used to generate encoding of characters
indices_char = np.load('indices_char.npy').item()#used to reverse encoding of characters

#%%generate new text in teminal and also save to file

chars_to_print=800#number of characters to generate
file = "generated_text.txt"#file to save the generated text
save_to_file = True

#some times "RuntimeWarning: divide by zero encountered in log"
#is written in the generated text, suppress warnings to avoid this.
warnings.filterwarnings("ignore")

for diversity in [0.1, 0.3, 0.5, 0.7, 1]:
    print()
    print('',file=open(file, "a"))
    if(save_to_file==True):
        print('----- diversity:', diversity,file=sys.stdout)
        print('----- diversity:', diversity,file=open(file, "a"))
        

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




















