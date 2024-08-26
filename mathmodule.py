import math

x = 9
y = 10.2
print(math.pi) #Pi sayısı
print(math.e) # "e" sayısı
sonuc = math.sqrt(x) # Kök alma
sonuc2 = math.ceil(y) # Sayıyı yukarı yuvarlama
sonuc3 = math.floor(y) # Sayıyı aşağı yuvarama

# Dairenin çevresi

r = float(input("Daire yarıçapını giriniz: "))
pi = math.pi
C = 2*pi*r
print(f"Dairenin çevresi = {round(C,2)}")

# Dairenin alanı

r = float(input("Daire yarıçapını giriniz: "))
pi = math.pi
A = round(pi*math.pow(r,2),2)
print(f"Dairenin alanı = {A}")