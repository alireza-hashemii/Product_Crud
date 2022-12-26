from datetime import datetime


class Product():
    products = []
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
        self.products.append(self)
        return(self.products)

    def read(self):
        for product in self.products:
            return(product)
   

    def update(self,name:str):
        self.title = name
        print("it has succesfully updated.")
        return(self.products)

    def delete(self):
        self.products.clear()
        print("it has succesfully deleted.")
        return(self.products)
            
    def __repr__(self) -> str:
        return(f"Products: {self.title}")

