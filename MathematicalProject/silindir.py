import math
yükseklik=int(input("Silindirin yüksekliğini giriniz: "))
yarıçap=int(input("Silindirin yarıçapını giriniz: "))
print("Silindirin Hacmi: ",(math.pi*yarıçap**2*yükseklik))
print("Silindirin Alanı: ",(2*math.pi*yarıçap*(yarıçap+yükseklik)))
#math.pi yerine 3 veya 3.14 yazarak küsüratsız sonuç elde edebilirsiniz.