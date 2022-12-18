from datetime import datetime
import json

products = []

class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return str(obj)
        return json.JSONEncoder.default(self, obj)

class Product():

    def create(self,Product_id:int,category_id:int,title:str,
    short_description:str,description:str,
    slug:str,permalink:str,IsAvailable:bool,sku:str,price:float,
    regular_price:float,sale_price:float,
    manage_stock:int,stock_quantity:int,IsVisible:bool,
    date_created_gmt:datetime,date_modified_gmt:datetime
    ):
        mdict = {
        "product_id":Product_id,
        "category_id":category_id,
        "title":title,
        "short_description":short_description,
        "description":description,
        "slug": slug,
        "permalink":permalink,
        "IsAvailable":IsAvailable,
        "sku":sku,
        "price":price,
        "regular_price":regular_price,
        "sale_price":sale_price,
        "manage_stock":manage_stock,
        "stock_quantity":stock_quantity,
        "IsVisible":IsVisible,
        "date_created_gmt":date_created_gmt,
        "date_modified_gmt":date_modified_gmt
        }
        products.append(mdict)
        data= json.dumps(products, indent = 4,cls=DTEncoder)
        return data


    def read(self,product_id:int):
        for product in products:
            if product["product_id"] == product_id:
                return(product)
        else:
            return("No products matched with given id.")


    def update(self,title:str,short_description:str,description:str,
    slug:str,permalink:str,IsAvailable:bool,sku:str,price:float,
    regular_price:float,sale_price:float,
    manage_stock:int,stock_quantity:int,IsVisible:bool,
    date_created_gmt:datetime,date_modified_gmt:datetime
    ):
        user_product_id = int(input("Which product do you want to update: "))
        mdict = {
        "product_id":"test",
        "category_id":"test",
        "title":title,
        "short_description":short_description,
        "description":description,
        "slug": slug,
        "permalink":permalink,
        "IsAvailable":IsAvailable,
        "sku":sku,
        "price":price,
        "regular_price":regular_price,
        "sale_price":sale_price,
        "manage_stock":manage_stock,
        "stock_quantity":stock_quantity,
        "IsVisible":IsVisible,
        "date_created_gmt":date_created_gmt,
        "date_modified_gmt":date_modified_gmt
        }
        for product in products:
            if product["product_id"] == user_product_id:
                product__id = product["product_id"]
                category__id = product["category_id"]
                index_of_product = products.index(product)
                mdict.update(product_id=product__id,category_id=category__id)
                products[index_of_product] = mdict
                return(products)
        else:
            return("No product were matched with the given id")
                

    def delete(self,product_id:int):
        for product in products:
            if product["product_id"] == product_id:
                products.remove(product)
                print("it has succesfully deleted.")
                return(products)
        else:
            return("No product found with the given id")

# obj1 = Product()
# dat = datetime(2014,3,4,4,3,2)
# print(obj1.create(3,5,"g","h","h","j","j",True,"d",3.0,3.0,3.0,3,3,True,dat,dat))
# print(obj1.update("gggg","hhhh","hhhh","j","j",True,"d",3.0,3.0,3.0,3,3,True,dat,dat))
# print(obj1.delete(3))

# print(obj1.read(4))