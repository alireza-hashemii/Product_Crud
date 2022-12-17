from abc import ABC , abstractmethod
from datetime import datetime

#! Abstract class for CRUD operations 
class IProduct(ABC):
    @abstractmethod
    def create(self,Product_id:int,category_id:int,title:str,
        short_description:str,description:str,
        slug:str,permalink:str,IsAvailable:bool,sku:str,price:float,
        regular_price:float,sale_price:float,
        manage_stock:int,stock_quantity:int,IsVisible:bool,
        # date_created_gmt:datetime,date_modified_gmt:datetime
    ):
        raise(NotImplementedError)

    @abstractmethod
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
