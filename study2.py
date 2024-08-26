# Typecasting = Bir veri türünü başka bir veri türüne dönüştürme işlemi
name = "Arsen"
age = 21
AGNO = 2.84
is_student = True

print(type(name)) #string
print(type(age)) #integer
print(type(AGNO)) #float
print(type(is_student)) #boolean

AGNO = int(AGNO) # = 2
age = float(age) # = 25.0
age = str(age) # = 25(string)

name = bool(name) # Eğer isim varsa "True" yok ise "False" verir.