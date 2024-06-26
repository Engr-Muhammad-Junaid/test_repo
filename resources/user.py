import sqlite3
from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from models.user import UserModel


        

class UserRegister(Resource):
    parser=reqparse.RequestParser() 
    parser.add_argument('username',
                            type=str,
                            required=True,
                            help="This field cannot be left  blank!"
                            
                            )
    parser.add_argument('password',
                            type=str,
                            required=True,
                            help="This field cannot be left  blank!"
                            
                            )
  
    #data come to the postrequest in json can be parse(can be validated,should be some contraint on it)
    def post(self):
        data=UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"Message":"A user with that username already exists"},400
        user=UserModel(**data)
        user.save_to_db()
        return {'Message':'User created successfully'}
    
   
    









    
    
    


    



