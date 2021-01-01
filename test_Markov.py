
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 01:39:02 2020

@author: olamijojo
"""
from Markov import Markov

def makeWordModel(filename):
    # creates a Marko model from words in  filename
    infile = open(filename)
    model = Markov()
    for line in infile:
        words = line.split()
        for w in words:
            model.add(w)
    infile.close()
    
    # Add a sentinel at the end of the text
    model.add(None)
    model.reset()
    return model

def generateWordChain(markov, n):
    # generates upto n words of output from a model
    words = []
    for i in range(n):
        next = markov.randomNext()
        if next is None: break # got a final state
        words.append(next)
    return " ".join(words)

def paragraph():
    
     """return a template for paragrapghs, number of words, autotagging"""
     pass
     
def Spellcheck():
    '''return anagram for spellcheck/proofreading,trigrams, bigram, Xgram'''
    pass 

def autocorrect():
    '''return anagram for suggesting and autocorrect'''
    pass


def test():
    filename = input("To train model Enter filename: ")
    m = makeWordModel(filename)
    print(generateWordChain(m, 30))
test()

"""
def next_word():
    filename = input("To train model Enter filename: ")
    word = input("enter a word to predict next word: ")
    m = makeWordModel(filename)
    print(word, generateWordChain(m, 20))
      
next_word()

"""