
from flask import Flask,request,jsonify
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required
from models.item import ItemModel
from db import db


class Item(Resource):
    parser=reqparse.RequestParser() 
    parser.add_argument('price', 
                            type=float,
                            required=True,
                            help="This field cannot be left  blank!"
                            
                            )
    parser.add_argument('store_id',
                            type=int,
                            required=True,
                            help="Every item needs a store id!"
                            
                            )
    
    @jwt_required()
    def get(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':"Item not found"},404

            
    def post(self,name):
        if ItemModel.find_by_name(name): 
                return {'message':"An item with name '{}' arleady exits".format(name)},400  #the 400 when somethings goes wrong with request
        data=Item.parser.parse_args()
        item=ItemModel(name,data['price'],data['store_id'])
        try:
            item.save_to_db()
        except:
            return {'message':"An error occured inserting the item."},500 #internel server error
        return item.json() ,201     #we also have to return json
   
    def delete(self,name):
        item=ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {"message":"Item deleted"}

        
    
    def put(self,name):
        data=Item.parser.parse_args()

        item=ItemModel.find_by_name(name)
    
        if item is None:
            item=ItemModel(name,data['price'],data['store_id'])

        else:
            item.price=data['price']
        item.save_to_db() 

        return item.json()
    

    
class Itemlist(Resource):
    def get(self):
         return {'items': [item.json()for item in  ItemModel.query.all()]} #it is returning all the objects in a database we getting all the items and then applying the fun of item
        