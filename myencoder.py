#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:44:12 2023

@author: sunyenpeng
"""


def reversecoder(text, method):
    letter="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low=letter.lower()
    key="ZYXWVUTSRQPONMLKJIHGFEDCBA"
    keylow=key.lower()
    if method=="encode":
        output=''
        for i in text:
            if i.isspace():
                output+=" "
            elif i.isupper():
                output+=key[letter.index(i)]
            elif i.islower():
                output+=keylow[low.index(i)]
        return output
    elif method=="decode":
        output=''
        for j in text:
            if j.isspace():
                output+=' '
            elif j.isupper():
                output+=letter[key.index(j)]
            elif j.islower():
                output+=low[keylow.index(j)]
        return output

if __name__=="__main__":
    print("Do you want to encode or decode?")
    r=input("> ").lower()
    if r.startswith("e"):
        method="encode"
    elif r.startswith("d"):
        method="decode"
    print("Please enter contents you want to encode/decode:")
    text=input("> ")
    print(reversecoder(text, method))
        
        
                






























































