from datetime import datetime

products = []
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

        self.data_list = [self.product_id,self.category_id,self.title,self.short_description,self.description,
        self.slug,self.permalink,self.is_available,self.sku,self.price,self.regular_price,self.sale_price,
        self.manage_stock,self.stock_quantity,self.is_visible,self.date_created_gmt,self.date_modified_gmt]

    def create(self):
        str_product_id = str(self.data_list[0])
        str_title = self.data_list[2]
        save_to_products = f"{str_product_id}-{str_title}"
        products.append(save_to_products) 
        print("It has succesfully created.")
        return self.__repr__()

    def read(self):
        for product in products:
            return(product)
   

    def update(self,updated_values:list):
        if len(updated_values) < 17:
            print("Pleasse assign a value to the all fields")
        else:
            if len(self.products) == 0:
                return("There is nothing to update.")
            else: 
                self.products.clear()
                for item in updated_values:
                    products.append(item)
                print("It has succesfully updated.")
                return(self.__repr__())

    def delete(self):
        if len(products) != 0:
            products.clear()
            print("It has succesfully deleted.")
            return(self.__repr__())
        else:
            return("There is no product")
            
    def __repr__(self) -> str:
        return(f"Products: {products}")

product1 = Product(1,1,"test_title","Nothing","Nothing","product","link",True,"nothing",1.0,1.0,1.0,1,1,True,datetime.now(),datetime.now())
print(product1.create())

product3 = Product(3,1,"test_title","Nothing","Nothing","product","link",True,"nothing",1.0,1.0,1.0,1,1,True,datetime.now(),datetime.now())
print(product3.create())
print(product3.read())