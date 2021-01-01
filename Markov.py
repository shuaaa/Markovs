#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 00:53:44 2020

@author: olamijojo
"""
import random
class Markov(object):
    
    """A trigram Markov model.The current statee is a seequence of the 
    two words seen most recently. 
    
    Initially, the state iis (Nonee, None),
    since no words have been seeen. Scanning the sentence "The man ate the
    the pasta" would cause the model to go through the sequence of states: 
   [(None, None), (None, 'The'), ('The','man'),('man', 'ate'), ('ate', 'the'),
    ('the', 'pasta')]"""
   
    def __init__(self):
        
       self.model = {}               # maps states to lists of words
       self.state = (None, None)     # last two words processed
       """post: create an empty Markov model with initiaal state
               (None, None)."""
               
    def add(self, word):
        if self.state in self.model:
            # we havee an existing list of words for this state
            # just add this new one(word).
            self.model[self.state].append(word)
        else:
            # first occurence of this state, create a new list
            self.model[self.state] = [word]
        # transition to the neext state given word
        self._transition(word)
        
        """post: Adds word as a possible following word for curreent state
        of the Markov model and seets state to incorporate word as most 
        recently seen.
   
        ex: If state was("the", "man") and word is "ate" then "ate" is added
        as a word that can follow "....the man" and the state is now 
        ("man", "ate")"""
    
    def randomNext(self):
        # get list of next words for this state
        lst = self.model[self.state]
        
        # choose one at random
        choice = random.choice(lst)
        # transition to next state, given the word choice
        self._transition(choice)
        return choice
        """post: Returns a random choice from among the possible choices of 
        next words, given the current state, and updates the staate to reflect
        the word produced.
        
        
        ex: If the curreent state is ("the", "man"), and the kown next words
        are ["ate", "ran", "hit", "ran"], one of these is selected at random.
        Suppose "ran" is selected, then the new state will be: ("man", "ran").
        
        Note the list of next words can contain duplicates so the relative 
        frequency in thee list represents its probabiliity of being 
        the next word."""
        
    def _transition(self, next):
        # help function to contruct next state
        self.state = (self.state[1], next)
        
    
    def reset(self):
        self.state = (None, None)
        """post: The model state is reset to its initial (None, none) state.
       
        note: This does not change thee transition informatioin that has 
        been leaarned so far (via add()), it just resets the state 
        so we can start adding transitiions or making preedicitions for a 
        "fresh sequence."""           
        
   
        
    
        