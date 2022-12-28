from product import Product
from datetime import datetime


# Making an object of product class
def main():

    product1 = Product(1,4,"iPhone 13","Nothing","""The iPhone 13 and iPhone 13 Mini (stylized as iPhone 13 mini) are smartphones designed, developed, marketed, and sold by Apple Inc. They are the fifteenth 
                        generation of iPhones (succeeding the iPhone 12 and iPhone 12 Mini respectively). They were unveiled at an Apple Event in Apple Park in Cupertino, California on September 14, 2021, alongside the higher-priced
                        iPhone 13 Pro and iPhone 13 Pro Max flagships. Pre-orders for the iPhone 13 and iPhone 13 Mini began on September 17, 2021. They were officially released on September 24, 2021. """,
                        "product","https://en.wikipedia.org/wiki/IPhone_13",True,"nothing",1.0,1.1300,999.0,1,1,True,datetime.now(),datetime.now()) 

    # Create
    print(product1.create())
    print("---------------------------")
    
    # Update
    print(product1.update("it has updated."))
    print("---------------------------")

    # Read
    print(product1.read(5))
    print("--------------------------")

    # ReadAll
    print(product1.read_all())
    print("-------------------------")

    # Delete
    print(product1.delete())
    
    


    print("-----------------------------")
    # Return True if product1 is an instance of class Product
    print(isinstance(product1,Product)) 
    # Return type of object product1
    print(type(product1)) 



# This module wont work if it's imported
if __name__ == "__main__":
    main()