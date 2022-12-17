from abstract_structure import IProduct
from datetime import datetime
import json

product = []


class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        # if passed in object is datetime object
        # convert it to a string
        if isinstance(obj, datetime):
            return str(obj)
        # otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)


class Product(IProduct):

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
        product.append(mdict)
        data= json.dumps(product, indent = 4,cls=DTEncoder)
        return data




    def read(self,product_id:int):
        raise(NotImplementedError)



    def update(self,title:str,short_description:str,description:str,
        slug:str,permalink:str,IsAvailable:bool,sku:str,price:float,
        regular_price:float,sale_price:float,
        manage_stock:int,stock_quantity:int,IsVisible:bool,
        date_created_gmt:datetime,date_modified_gmt:datetime
        ):
        raise(NotImplementedError)
    


    def delete(self,product_id:int):
        raise(NotImplementedError)

# obj1 = Product()
# dat = datetime(2014,3,4,4,3,2)
# print(obj1.create(4,3,"g","h","h","j","j",True,"d",3.0,3.0,3.0,3,3,True,dat,dat))
