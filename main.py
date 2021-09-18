from src.user import User
from src.address import Address
from src.phone import Phone


a = Address(street='Rua Osorio Borba', number='526', complement='Apto 202', city='Jaboatao', state='PE',
            cep='54400-120')

p = Phone(phone_number='123', phone_type='Celular')
# print(a.show_data())
p2 = Phone(phone_number='456', phone_type='Trabalho')
u = User(name='Milo', birthdate='2020-01-09', email='milo@gamil.com', password='kida', address=a, phones=[p, p2])
print(u.show_data())
