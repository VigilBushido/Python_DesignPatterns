# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 16:26:55 2022

@author: vigilbushido
"""
import json 
from dataclasses import dataclass

from game.character import GameCharacter


@dataclass
class Sorcerer:
    
    name: str()
    
    def make_a_noise(self) -> None:
        print("Aaaargh!")
        
    
@dataclass
class Wizard:
    
    name: str()
    
    def make_a_noise(self) -> None:
        print("Hmmm")
        
def main() ->:
    """Creates game characters from a file containing a level definition"""
    
    # read data from a JSON file
    with open("./level.json") as file:
        data = json.load(file)
        
        #create the characters
        
    