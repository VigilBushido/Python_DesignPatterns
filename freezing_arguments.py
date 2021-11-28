# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 00:58:12 2021

@author: vigilbushido
"""
from tagger import tag
from operator import mul 
from functools import partial

def main():
    triple = partial(mul, 3) # create new triple function from mul, binding first positional argument to 3
    print(triple(7)) # test it
    print(list(map(triple, range(1,10)))) #use triple with map; mul would not work with map 
    
    
    print(tag)
    picture = partial(tag, 'img', cls='pic-frame')
    print(picture(src='wumpus.jpeg'))
    print(picture)
    print(picture.func)
    print(picture.args)
    print(picture.keywords)
    
if __name__ == "__main__":
    main()