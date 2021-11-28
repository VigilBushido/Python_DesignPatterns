# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 20:43:44 2021

@author: vigilbushido
"""
def main():
    users = [
    (0, "John", "password"),
    (1, "Programming", "python"),
    (2, "Never", "sink"),
    (3, "entity", "epic1337"),
    ]
    
    username_mapping = {user[1]: user for user in users}
    userid_mapping = {user[0]: user for user in users}
    
    print(username_mapping)
    print("type of username_mapping", type(username_mapping))
    print(username_mapping["John"]) # pulls up his whole directory of information
    print(type(username_mapping["John"])) #returns a tuple
    
if __name__=='__main__':
    main()
