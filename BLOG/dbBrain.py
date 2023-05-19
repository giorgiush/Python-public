from sqlalchemy import create_engine, Boolean
from sqlalchemy.orm import Session
from distutils.util import strtobool
import random
import json


class dbBrain():
    
    def __init__(self, db_path:str, tables):
        self.db_path = db_path
        self.engine = create_engine(self.db_path)
        tables.Base.metadata.create_all(self.engine, checkfirst=True)
        
        
        
    def __convert_to_boolean(self, table, params):
        """Checks if columns are boolean types and returns dictionary with converted value types"""
        for param in params:
            if getattr(table.__table__.columns, param).type.__class__ == Boolean:
                params[param] = bool(strtobool(params[param]))
        return params    
    
    
    
    def random_row(self, table):
        with Session(self.engine) as sesh:
            return random.choice(sesh.query(table).all())
        
        
        
    def all_json(self, table:object):
        with Session(self.engine) as sesh:
            return json.dumps([{attr:getattr(row, attr) for attr in list(vars(row).keys())[1:]} for row in sesh.query(table).all()])
            
            
            
    def search(self, table:object, params:dict):
        """Takes a table model along with search parameter(s) and returns result in json. If no parameters specified, returns whole table data."""   
        
        with Session(self.engine) as sesh:
            query = sesh.query(table)
            for param in params:
                
                # checks if the column is boolean type and converts
                if getattr(table.__table__.columns, param).type.__class__ == Boolean:
                    params[param] = bool(strtobool(params[param]))
                    query = query.filter(getattr(table, param) == params[param])
                else:
                    query = query.filter_by(**params)
                    
            # returns all the results in json
            result = json.dumps([{attr:getattr(row, attr) for attr in list(vars(row).keys())[1:]} for row in query.all()])
            if "id" in result:
                return result
            else:
                return json.dumps("Not found"), 404
            
            
            
    def add_row(self, table:object, params:dict):
        """Adds row from dictionary of columns:values"""
        
        params = self.__convert_to_boolean(table, params)
                      
        with Session(self.engine) as sesh:
            sesh.add(table(**params))
            sesh.commit()
            return json.dumps("Successfully added new row"), 200
    
        
        
    def patch_by_id(self, table:object, id, params:dict):
        """Searches entry by id and updates attributes with data give in passed dictionary"""
        
        params = self.__convert_to_boolean(table, params)
        
        with Session(self.engine) as sesh:
            query = sesh.query(table).get(id)
            
            if not query:
                return json.dumps("Not found"), 404
            
            elif query:
                for param in params:
                    setattr(query, param, params[param])           
                sesh.commit()
                return json.dumps("Successfully patched"), 200
            
            else:
                return json.dumps("Uknown error"), 500
            
            
            
    def delete_by_id(self, table:object, id:int):
        
        with Session(self.engine) as sesh:
            query = sesh.query(table).get(id)
            
            if query:
                sesh.delete(query)
                sesh.commit()
                return json.dumps("Sucessfully deleted"), 200
            else:
                return json.dumps("Not found"), 404


            
    def get_object_by_id(self,table:object, id:int):
         with Session(self.engine) as sesh:
            return sesh.query(table).get(id)
        
        
        
    def get_object_by_params(self, table:object, params:dict):
        with Session(self.engine) as sesh:
            query = sesh.query(table)
            for param in params:
                # checks if the column is boolean type and converts
                if getattr(table.__table__.columns, param).type.__class__ == Boolean:
                    params[param] = bool(strtobool(params[param]))
                    query = query.filter(getattr(table, param) == params[param])
                else:
                    query = query.filter_by(**params)
            if query.first() != None:
                return query.first()
            else:
                return "Not found"
            
    def get_all_objects(self, table:object,):
        with Session(self.engine) as sesh:
            return sesh.query(table).all()