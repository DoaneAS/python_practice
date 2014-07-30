# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 12:38:00 2014

@author: ashleysdoane
"""

import string


def txfile(fin):
    hist = {}
    fin = open(fin)
    for line in fin:
        line = line.replace('-', ' ')
        #line = line.strip()
        for word in line.split():
            #word = word.strip(string.punctuation + string.whitespace)
            word = word.translate(string.maketrans("", ""), string.punctuation)
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1
    return(hist)


def wrd_cnt(hist):
    tot = []
    for k in hist:
        t = (h[k])
        tot.append(t)
        res = sum(tot)
    return(res)


def tot_wrds(hist):
    return sum(hist.values())
    """same result as wrd_cnt, but shorter"""


def dwrd_cnt(hist):
    w = hist.keys()
    tot = len(w)
    return(tot)


def freq_wrd(hist):
    t = list(hist.items())
    tt = []
    for w, n in t:
        tt.append((n, w))
    tt.sort(reverse=True)
    return tt[0:50]


def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res.viewkeys()


if __name__ == '__main__':

    file = raw_input('file path to analyze:')
    #file = '/Users/ashleysdoane/Desktop/freud.txt'

    h = txfile(file)
    words = txfile('/Users/ashleysdoane/Desktop/words.txt')

    print 'ANALYSIS OF', file
    print 'TOTAL NUMBER OF WORDS', tot_wrds(h)
    print 'NUMBER OF UNIQUE WORDS', dwrd_cnt(h)
    print 'TOP 50 MOST COMMON WORDS', freq_wrd(h)
    print 'WORDS IN TEXT THAT ARE NOT FOUND IN REFERENCE LIST, WORDS.TXT', subtract(h, words)


  open(
