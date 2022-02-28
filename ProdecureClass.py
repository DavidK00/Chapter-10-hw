class procedure:
    def __init__(self, name, date, prac, charge, id):
        self.__name = name
        self.__date = date
        self.__prac = prac #practitioner
        self.__charge = charge
        self.__id = id

 
    #Accessor Methods
    def get_name(self): 
        return self.__name

    def get_date(self): 
        return self.__date
    
    def get_prac(self): 
        return self.__prac

    def get_charge(self): 
        return self.__charge
    
    def get_id(self): 
        return self.__id