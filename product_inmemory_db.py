class ProductInMemoryDb:
    products_list = []

    def __init__(self,data:dict):
        self.products_list.append(data)

    def __str__(self) -> str:
        return f"Product list : \n {self.products_list}"  
        