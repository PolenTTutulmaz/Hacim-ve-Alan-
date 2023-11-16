kenar1=int(input("Birinci dik kenarın uzunluğunu giriniz : "))
kenar2=int(input("İkinci dik kenarın uzunluğunu giriniz : "))
kenar3=int(input("Üçüncü kenarın (hipotenüs) uzunluğunu giriniz : "))
yükseklik=int(input("Üçgen prizmanın yüksekliğini giriniz: "))
tabanAlanı=(kenar1*kenar2)/2
print("Taban Alanı : ",tabanAlanı)
yanalAlan=(kenar1+kenar2+kenar3)*yükseklik
print("Yanal Alan : ",yanalAlan)
print("Toplam Alan : ",2*tabanAlanı+yanalAlan)
print("Hacim : ",tabanAlanı*yükseklik)
