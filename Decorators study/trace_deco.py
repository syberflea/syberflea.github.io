#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import functools


def trace(func):
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    functools.update_wrapper(inner, func)
    return inner


@trace 
def identity(x):
    "I do nothing useful"
    return x 
    
        
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))
  

def main():
    ''' Entry point.'''
    print('Art Deco')
    identity(8)


if __name__ == '__main__':
  main()