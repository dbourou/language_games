#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 19:06:46 2021

@author: usuari
"""


import tkinter as tk
from tkinter import simpledialog
import numpy as np



words = [ 'peritoneal', 'synthetic', 'diabetes', 
'epimorphism', 'psychology', 'ideal', 'etymology',
'syntax', 'parallax', 'atmosphere', 'diameter', 'parameter',
'analog', 'empathize', 'panic', 'antithesis', 'thesaurus',
'geothermal', 'alcohol', 'geometric', 'parenchyma', 'cataract',
'antipathy', 'trident', 'hypothermia', 'zoomorphic','diatome',
'platypus', 'rhythm', 'diagram', 'anamorphic', 'anaphora', 
'paralyze', 'meningitis', 'antibiotic', 'crystal', 'graphic', 
'democrat', 'basis', 'prism', 'place', 'sponge', 'political',
'overestimate', 'correlate', 'omnidirectional', 
'perspicuous', 'compromise', 'medieval', 'ancient', 'rainbow', 
'diffraction', 'digital', 'digitize', 'trivialize', 'counterfactual',
'bistable', 'ferrous', 'omnipotent', 'present', 'cage',
'axiety', 'indent', 'public', 'ratio', 'aquatic', 'society',
'median', 'contraindication', 'iterate', 'mammiferous',
'import', 'export', 'terrarium', 'terraform', 'circumference',
'reference', 'sense', 'poll', 'lattice', 'bilingual', 'locus',
'cancerous', 'bimodal', 'clavicle', 'model', 'realistic' ]

label = ['y']*43 + ['n']*43

half_half = [ 'bipolar', 'sociopolitical', 'geolocation',
'gene', 'matrix', 'cartography' ]
#maybe put these in an advanced level of the game

# One test run
# Make two lists with words and
# correct answers

random = list(np.random.permutation(np.arange(0,len(words)-1))[:10])
test_words = list(map(words.__getitem__, random))
test_correct = list(map(label.__getitem__, random))


'''
Implement experiment in python,
print words in random distribution
and make sound of pronunciation with
either american/british from the internet.

Get user input: G N, and record it 

Try to vary prefixes and suffixes in both sets 
so there can't be heuristics about them.
Give answers only after all questions are answered.
'''

answers = []

for i in range(0, len(test_words)):
    
    ROOT = tk.Tk()

    ROOT.withdraw()
    # the input dialog
    USER_INP = simpledialog.askstring(title="Test",
    prompt="Does the following word have a Greek root? \nType y/n \n\n"+test_words[i]+"\n")

# check it out
    answers.append(USER_INP)  
 

score=0
for l in range(0, len(test_words)):
    
    if test_correct[l] == answers[l]:
        score = score + 1
        
    else:
        continue
  
score= int(score*10)

USER_INP = simpledialog.askstring(title="Test",
    prompt="Nice try! Your score was "+str(score)+" percent!")
    #\n Wanna play again? Type y/n")

