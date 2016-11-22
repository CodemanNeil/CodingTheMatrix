# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist):
    return [dct[x] for x in keylist]

def list2dict(L, keylist):
    return {keylist[i] : L[i] for i in range(len(L))}

def listrange2dict(L):
    return {i : L[i] for i in range(len(L))}