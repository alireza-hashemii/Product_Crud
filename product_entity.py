from datetime import datetime

products = []

class Product():
    def __init__(self,product_id:int,category_id:int,title:str,short_description:str,description:str,
        slug:str,permalink:str,Is_Available:bool,sku:str,price:float,regular_price:float,
        sale_price:float,manage_stock:int,stock_quantity:int,Is_Visible:bool,
        date_created_gmt:datetime,date_modified_gmt:datetime):

        self.product_id = product_id
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
        products.append(self.title)
        return(products)
        
    def read():
        pass

    def update():
        pass

    def delete():
        pass


#! Uncomment this part and run the code.
# dte = datetime.now()
# oj = Product(3,3,"g","g","g","g","g",True,"h",3.0,3.0,3.0,3,3,True,dte,dte)
# print(oj.create())