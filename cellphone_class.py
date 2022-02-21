class cellphone:
    def __init__(self, man, mod, pri):
        
        self.__manufacturer = man
        self.__model = mod
        self.__price = pri
   
        
    def set_manufact(self,man):
        self.__manufacturer = man
        

    def set_mod(self,model):
        self.__model = model
        
        
    def set_price(self,price):
        self.__price = price

    def get_manufact(self):
        return self.__manufacturer
        
    def get_mod(self):
        return self.__model
        
    def get_price(self):
        return self.__price
        