from datetime import datetime
from product_inmemory_db import ProductInMemoryDb


class Product():

    def __init__(self,product_id:int,category_id:int,title:str,short_description:str,description:str,
        slug:str,permalink:str,Is_Available:bool,sku:str,price:float,regular_price:float,
        sale_price:float,manage_stock:int,stock_quantity:int,Is_Visible:bool,
        date_created_gmt:datetime,date_modified_gmt:datetime):

        assert product_id >= 0,f"Product id should be greater than zero but {product_id} is not"
        assert category_id >= 0,f"category id should be greater than zero but {product_id} is not"

        self.product_id = product_id
        self.category_id = category_id
        self.title = title
        self.short_description = short_description
        self.description = description
        self.slug = slug
        self.permalink = permalink
        self.is_available = Is_Available
        self.sku = sku
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.manage_stock = manage_stock
        self.stock_quantity = stock_quantity
        self.is_visible = Is_Visible
        self.date_created_gmt = date_created_gmt
        self.date_modified_gmt =  date_modified_gmt

    def create(self):
        dict = {}
        for key,value in self.__dict__.items():
            dict[key] = value
        object = ProductInMemoryDb(dict)
        return object     


    def read(self,id:int):
        for product in ProductInMemoryDb.products_list:
            if product["product_id"] == id:
                return product
        return("No products found with the given id.")
        
    @classmethod
    def read_all(cls):
        for product in ProductInMemoryDb.products_list:
            print(product,end="\r")


    def update(self,id:int,title:str):
        for product in ProductInMemoryDb.products_list:
            if product["product_id"] == id:
                product["title"] = title
            return(self.__repr__())
        return("No products found with the given id.")
       


    def delete(self,id:int):
        for product in ProductInMemoryDb.products_list:
            if product["product_id"] == id:
                ProductInMemoryDb.products_list.remove(product)
                print("succesfully deleted.")
                return(ProductInMemoryDb.products_list)
        return("No products found with the given id.")

        
    def __repr__(self) -> str:
        return(f"Product is : {self.product_id} \n {self.title} \n {self.category_id} \n {self.short_description} \n {self.description} \n {self.slug} \n {self.permalink} \n {self.is_available} \n {self.sku} \n {self.price} \n {self.stock_quantity} \n {self.date_created_gmt} \n {self.date_modified_gmt}")


product1 = Product(1,4,"iPhone 13","Nothing","""The iPhone 13 and iPhone 13 Mini (stylized as iPhone 13 mini) are smartphones designed, developed, marketed, and sold by Apple Inc. They are the fifteenth 
                        generation of iPhones (succeeding the iPhone 12 and iPhone 12 Mini respectively). They were unveiled at an Apple Event in Apple Park in 
                        iPhone 13 Pro and iPhone 13 Pro Max flagships. Pre-orders for the iPhone 13 and iPhone 13 Mini began on September 17, 2021. They were officially released on September 24, 2021. """,
                        "product","https://en.wikipedia.org/wiki/IPhone_13",True,"nothing",1.0,1.1300,999.0,1,1,True,datetime.now(),datetime.now()) 

product2 = Product(2,4,"iPhone 14","Nothing","""The iPhone 13 and iPhone 13 Mini (stylized as iPhone 13 mini) are smartphones designed, developed, marketed, and sold by Apple Inc. They are the fifteenth 
                        generation of iPhones (succeeding the iPhone 12 and iPhone 12 Mini respectively). They were unveiled at an Apple Event in Apple Park in 
                        iPhone 13 Pro and iPhone 13 Pro Max flagships. Pre-orders for the iPhone 13 and iPhone 13 Mini began on September 17, 2021. They were officially released on September 24, 2021. """,
                        "product","https://en.wikipedia.org/wiki/IPhone_13",True,"nothing",1.0,1.1300,999.0,1,1,True,datetime.now(),datetime.now())
                        
#! 1 - make instances in main.py suitable. \ 2 - polish up the code \ 3 - make str and repr method prettier