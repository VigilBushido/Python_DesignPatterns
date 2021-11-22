# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 22:09:33 2021

@author: vigilbushido
"""
from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
        
class LightBulb(Switchable): #will inherit from switchable 
    #implements the interface that's defined in switchable
    def turn_on(self):
        print("LightBulb: turned on...")
        
    def turn_off(self):
        print("LightBulb: turned off...")
        
class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")
    
    def turn_off(self):
        print("Fan: turned off...")
        
class ElectricPowerSwitch:
    #we change this so that it is no longer dependent on Lightbulb but instead of 2 classes coupled 
    #we de-coupled them through an interface
    #def __init__(self, l: LightBulb):
    def __init__(self, c: Switchable):
        self.client = c
        self.on = False
        
    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True
            
def main():
    l = LightBulb()
    f = Fan()
    switch = ElectricPowerSwitch(f)
    switch.press()
    switch.press()

if __name__ == "__main__":
    main()