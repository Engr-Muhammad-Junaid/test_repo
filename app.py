from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item,Itemlist

from flask_sqlalchemy import SQLAlchemy
from resources.store import Store,StoreList

from db import db

db=SQLAlchemy()

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:/Flask/code/data.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
api=Api(app) 
app.secret_key='jose'
jwt=JWT(app,authenticate,identity)


#before any request we made it will first create data.db in our dir from the tablesname which are we specified already in models from the import 
@app.before_request
def create_tables():
    db.create_all()

#this is to know when an object had changed but not been saved to the database,the extension flask sqlalchemy was tracking every change that we made to the sqlalchemy session 
#and that took some resources now turning if off b/s sqlalchemy itself the main library has it is own modifications tracker which is a bit better.
#so this turn off the  flask sqlalchemy modifications tracker,it does not turn off the sqlalchemy modifications tracker

api.add_resource(Store,'/store/<string:name>')

api.add_resource(Item,'/item/<string:name>')    #http://127.0.0.1:5000/student/john
api.add_resource(Itemlist,'/items') 
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register') 



if __name__=="__main__":
    from db import db
    
    db.init_app(app=app) #this must be called before accessing the database engine 
  
    app.run(port=5000,debug=True)