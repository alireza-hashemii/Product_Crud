from product import Product
from datetime import datetime

product1 = Product(1,1,"test_title","Nothing","Nothing","product","link",True,"nothing",1.0,1.0,1.0,1,1,True,datetime.now(),datetime.now())

# Making an object of product class
def main():
    product1 = Product(1,1,"test_title","Nothing","Nothing","product","link",True,"nothing",1.0,1.0,1.0,1,1,True,datetime.now(),datetime.now()) 
    # C
    print(product1.create())
    # R
    print(product1.read())
    # U
    print(product1.update([2,2,"test","No","No","product","link",True,"nothing",1.0,1.0,1.0,3,3,False,datetime.now(),datetime.now()]))
    # D
    print(product1.delete())

# isisntance method
print(isinstance(product1,Product)) # Output --> True

# type method
print(type(product1)) # Output --> <class 'product.Product'>


if __name__ == "__main__":
    main()