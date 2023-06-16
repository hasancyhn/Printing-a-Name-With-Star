# 20010011091/Hasan/Ceyhan

boyut_Giriniz = int(input("Boyut değerini giriniz: "))
print("\n")

for satir1 in range(boyut_Giriniz):         # Satırlarda dolaşıyoruz
    for sutun1 in range(boyut_Giriniz):     # Sütunlarda dolaşıyoruz
        if sutun1 == 0 or (sutun1 == boyut_Giriniz-1) or ((satir1 == boyut_Giriniz//2) and (sutun1 > 0 and sutun1 < boyut_Giriniz)):
        # Üstteki satırda durumları kontrol ediyoruz.
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")

a_Harfi = ""
for satir2 in range(boyut_Giriniz):         # Satırlarda dolaşıyoruz
    for sutun2 in range(boyut_Giriniz):     # Sütunlarda dolaşıyoruz
        if (sutun2 == 0 or sutun2 == boyut_Giriniz-1) or ((satir2 == 0 or satir2 == boyut_Giriniz//2) and (sutun2 > 0  and sutun2 < boyut_Giriniz)):
        # Üstteki satırda durumları kontrol ediyoruz.
            a_Harfi = a_Harfi + "*"
        else:
            a_Harfi = a_Harfi + " "
    a_Harfi = a_Harfi + "\n"
print(a_Harfi)


for satir3 in range(boyut_Giriniz):         # Satırlarda dolaşıyoruz
    for sutun3 in range(boyut_Giriniz):     # Sütunlarda dolaşıyoruz
        if(satir3==0 or satir3==boyut_Giriniz//2 or satir3==boyut_Giriniz-1) or (sutun3==0 and satir3<boyut_Giriniz//2) or (satir3>boyut_Giriniz//2 and sutun3==boyut_Giriniz-1):
        # Üstteki satırda durumları kontrol ediyoruz.
            print("*",end="")
        else:
            print(" ",end="")
    print("\n",end="")
print("\n")

a_Harfi4 = ""
for satir4 in range(boyut_Giriniz):         # Satırlarda dolaşıyoruz
    for sutun4 in range(boyut_Giriniz):     # Sütunlarda dolaşıyoruz
        if (sutun4 == 0 or sutun4 == boyut_Giriniz-1) or ((satir4 == 0 or satir4 == boyut_Giriniz//2) and (sutun4 > 0  and sutun4 < boyut_Giriniz)):
        # Üstteki satırda durumları kontrol ediyoruz.
            a_Harfi4 = a_Harfi4 + "*"
        else:
            a_Harfi4 = a_Harfi4 + " "
    a_Harfi4 = a_Harfi4 + "\n"
print(a_Harfi4)


for satir5 in range(boyut_Giriniz):         # Satırlarda dolaşıyoruz
    for sutun5 in range(boyut_Giriniz):     # Sütunlarda dolaşıyoruz
        if (sutun5 == 0 or sutun5 == boyut_Giriniz-1) or (satir5 == sutun5):
        # Üstteki satırda durumları kontrol ediyoruz.
            print("*",end="")
        else:
            print(" ",end="")
    print("\n",end="")
