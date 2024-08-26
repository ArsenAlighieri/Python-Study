#if = Bir komutu EĞER koşul DOĞRU ise çalıştırır
#else = Eğer if koşulu DOĞRU DEĞİL ise başka bir komutu çalıştırır.
#elif = Birden fazla koşul durumu sıralamak için kullanılır. İlk if durumu karşılanmaz ise başka bir if koşuluna bakar. Doğru ise uygular.

yas = int(input("Yaşınızı giriniz: "))
if(yas >= 18):
    print("İçeri girebilir. ")
elif(yas <= 0):
    print("Daha doğmamışsın.")
else:
    print("İçeri giremez. ")

cevap = input("Yemek yemek ister misin? (Y/N)")
if(cevap == "Y"):
    print("Saat 8'de seni alıyorum o zaman!")
elif(cevap == "N"):
    print("Kendim yiyeceğim demek ki ;( ")
else:
    print("Anlayamadım?")
    
satilik_mi = True
if(satilik_mi == True):
    x = input("Ürünü satın almak ister misin? (Y/N)")
    if(x == "Y"):
        print("Ürünü satın aldın.")
        satilik_mi = False
    else:
        print("peki.")
else:
    print("Ürün Satılık Değil.")