from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"
    id=db.Column(db.INTEGER,primary_key=True)
    name=db.Column(db.String(80))
    
    items=db.relationship('ItemModel',lazy='dynamic')  #we  have a relationship with itemModel then sqlalchemy goes to the item.py find the store_id which means one item is related to store

    def __init__(self,name):
        self.name=name

    def json(self):
        return{"name": self.name,"items":[item.json() for item in self.items.all()]}

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
    