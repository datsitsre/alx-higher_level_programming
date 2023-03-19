#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if length < 0:
        answer = None
        return (length, answer)
    else:
        answer = sentence[0]
        return (length, answer)
