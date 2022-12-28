from datetime import datetime

products = {}

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
        for key,value in self.__dict__.items():
            products[key] = value
        return (self.__repr__())
            

    def read(self,id:int):
        for key,value in products.items():
            if key == "product_id" and value == id:
                return(self.__repr__())
        else:
                print("No product found with given id.")
        
   
    def read_all(self):
        for key,value in products.items():
            return(f"{key} : {value}")


    def update(self,title:str):
        self.title = title
        return(self.__repr__())        
      

    def delete(self):
        products.clear()
        print("It has succesfully deleted.")
        return(products)
         
            
    def __repr__(self) -> str:
        return(f"Product is : {self.product_id} \n {self.title} \n {self.category_id} \n {self.short_description} \n {self.description} \n {self.slug} \n {self.permalink} \n {self.is_available} \n {self.sku} \n {self.price} \n {self.stock_quantity}\n {self.date_created_gmt} \n {self.date_modified_gmt}")


