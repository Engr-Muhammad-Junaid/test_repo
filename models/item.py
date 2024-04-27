#the itemmodel is an our internal representation so it has to contain the properties of an item as obj properties
#so object has a name and price properties
from db import db

class ItemModel(db.Model):
    __tablename__ = "items"
    id=db.Column(db.INTEGER,primary_key=True)
    name=db.Column(db.String(80))
    price=db.Column(db.Float(precision=2))
   

    store_id=db.Column(db.Integer, db.ForeignKey('stores.id'))  #every model has a property store that is the store which matches this store id in it's id.
    store=db.relationship('StoreModel')
 


    def __init__(self,name,price,store_id):
        self.name=name
        self.price=price
        self.store_id=store_id
    def json(self):
        return{"name": self.name,"price": self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
      
                                                             #ItemModel which is the class a type of sqlalchemy model,then we want to query the model and now the sqlalchemy knows we are
                                                            #we are building the query on the database.The function return the ItemModel object that has properties of name and price

  
    def save_to_db(self):
        db.session.add(self)    #here we inserting the object to the session,the session is a collection of objects that we are going to write into database
                              #this method is usally for both the update and inserting data into database
        db.session.commit()
    
        
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
       
  

       