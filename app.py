from flask import Flask,request
from flask_restful import Resource, Api
from flask_jwt import JWT,jwt_required

from security import authenticate,identity

app = Flask(__name__)
app.secret_key='jose'
api = Api(app)

jwt=JWT(app,authenticate,identity)
   
items=[]


class item(Resource):
    @jwt_required()
    def get(self,name):
       item= next(filter(lambda x: x['name'] == name,items),None)
       return {'item':item},200 if item else 404  

    def post(self,name):
        if next(filter(lambda x:x['name']==name,items),None):
            return {'message':"an item with '()alredy exist".format(name)},404
        
       
        data=request.get_json()
        item={'name':name,'price':data["price"]}
        items.append(item)
        return item,201


class itemlist(Resource):
    def get(self):
        return {'item':items} 


api.add_resource(item,'/item/<string:name>') 
api.add_resource(itemlist,'/items')
app.run(port=5000,debug=True)      
