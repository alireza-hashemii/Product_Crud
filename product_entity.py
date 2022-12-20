from datetime import datetime



class Product():
    products = []
    def __init__(self,product_id:int,category_id:int,title:str,short_description:str,description:str,
        slug:str,permalink:str,Is_Available:bool,sku:str,price:float,regular_price:float,
        sale_price:float,manage_stock:int,stock_quantity:int,Is_Visible:bool,
        date_created_gmt:datetime,date_modified_gmt:datetime):

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

        self.data_list = [self.product_id,self.category_id,self.title,self.short_description,self.description,
        self.slug,self.permalink,self.is_available,self.sku,self.price,self.regular_price,self.sale_price,
        self.manage_stock,self.stock_quantity,self.is_visible,self.date_created_gmt,self.date_modified_gmt]

    def create(self):
        for item in self.data_list:
            self.products.append(item)
        print("It has succesfully created.")
        return self.__repr__()

    def read(self):
        for product in self.products:
            print(product,end=", ")
   

    def update(self,updated_values:list):
        if len(updated_values) < 17:
            print("Pleasse assign a value to the all fields")
        else:
            if len(self.products) == 0:
                return("There is nothing to update.")
            else: 
                self.products.clear()
                for item in updated_values:
                    self.products.append(item)
                print("It has succesfully updated.")
                return(self.__repr__())

    def delete(self):
        if len(self.products) != 0:
            self.products.clear()
            print("It has succesfully deleted.")
            return(self.__repr__())
        else:
            return("There is no product")
            
    def __repr__(self) -> str:
        return(f"Products: {self.products}")
