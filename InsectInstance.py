from unittest import mock
import InsectClass as i

mosquito = i.Insect(2,4,9)
housefly = i.Insect(3,6,8)

print(mosquito.flight_length())
print(housefly.flight_length())

print('This insect will fly', mosquito.get_fly()) 
print('This insect will fly', housefly.get_fly()) 



