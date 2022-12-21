from product_entity import Product
from datetime import datetime

#? In Python, a class is an object of the class type
product1 = Product(1,1,"test_title","Nothing","Nothing","product","link",True,"nothing",1.0,1.0,1.0,1,1,True,datetime.now(),datetime.now())
print(type(type(product1)))


#? We can easily make a new dynamic class using type method 
def Product__init__(self,name):
    self.name = name
Product2 = type("Product2",(),{"__init__":Product__init__,"name": lambda self: "Hi, I am " + self.name})
item1 = Product2("phone")
print(item1.name)

#? isinstance method : this method receives an object as a first arg and a class name 
#? as a second arguman and determine if an object belongs to that specific class or not
print(isinstance(datetime,type))
print(isinstance(item1,Product2))
print(isinstance(item1,Product))