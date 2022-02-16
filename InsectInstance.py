from unittest import mock
import InsectClass as i

mostquito = i.Insect()
housefly = i.Insect()

mostquito.flight_length()
housefly.flight_length()

print('This insect will fly', mostquito.get_fly()) 
print('This insect will fly', housefly.get_fly()) 



