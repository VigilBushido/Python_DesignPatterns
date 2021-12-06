# -*- coding: utf-8 -*-
"""
Created on Sat Dec 6 

@author: vigilbushido
"""
from flask import Flask, jsonify, request #to work in the brower we read in jsonify data
app = Flask(__name__)

stores = [
    {
         'name': 'beautiful store',
         'items': [
             {
                 'name': '1800-FLOWERS',
                 'price': 100
             }
          ]
    },
    {
         'name': 'beautiful store 2',
         'items': [
             {
                 'name': 'books',
                 'price': 100
             }
         ]
     }
 ]
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if(store['name']==name):
            return jsonify(store['name'])
    return jsonify({'message':'Store not found'})

@app.route('/store/<string:name>/item')
def get_store_items(name):
    for store in stores:
        if(store['name']==name):
            return jsonify(store['items'])
    return jsonify({'message':'Store not found'})

@app.route('/store', methods = ['Post'])
def create_store():
    req_data = request.get_json()
    new_store = {
    'name': req_data['name'],
    'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>/item', methods = ['POST'])
def create_store_item(name):
    for store in stores:
        if(store['name']==name):
            req_data = request.get_json()
            new_item = {
            'name' : req_data['name'],
            'price' : req_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'Store not found'})
@app.route('/')
def home():
    return "Store Home Page"

if __name__ == "__main__":
    app.run(port=8080 , debug = False)

