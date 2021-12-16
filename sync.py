# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 18:32:20 2021

@author: vigilbushido
"""

import requests

base_url = 'http://httpbin.org/'

def get_delay(seconds):
    endpoint = f'/delay/{seconds}'
    
    print(f'Getting with {seconds} delay ...')
    
    resp = requests.get(base_url+endpoint)
    data = resp.json()
    print(data)
    
get_delay(5)

print('Okay! all finished getting reuest.')