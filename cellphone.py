import cellphone_class as c

def main():
    man = 'Apple'
    mod = 'iphone 13'
    price = 1000
    phone = c.cellphone(man, mod, price)
    
    print('Your phone manufacturer is:',phone.get_manufact())
    print('Your phone model is:', phone.get_mod())
    print('Your phone price is:', '$', phone.get_price())
    
   
main()