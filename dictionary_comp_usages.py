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
    
    # -- Can be useful to log in for example --

    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    
    _, username, password = username_mapping[username_input]
    
    if password_input == password:
        print("Your details are correct!")
    else:
        print("Your details are incorrect.")
    
if __name__=='__main__':
    main()
