from product_entity import Product
from datetime import datetime

# Making an object of product class
product1 = Product(
    1,1,"test_title","Nothing","Nothing","product","link",True,
    "nothing",1.0,1.0,1.0,1,1,True,datetime.now(),datetime.now()
    ) 


# C
product1.create()

# R
product1.read()

# U
product1.update([2,2,"test","No","No","product","link",True,
            "nothing",1.0,1.0,1.0,3,3,False,datetime.now(),datetime.now()]
    )

# D
product1.delete()