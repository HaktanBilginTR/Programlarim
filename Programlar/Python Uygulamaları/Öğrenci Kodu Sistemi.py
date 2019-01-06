
def hesaplama(a,b,c):
     try:
        m=((int(a))-(len(a))+(int(a)*int(a))//(int(3)+(int(b))*(int(c)+int(16))))
        return m
     except ValueError:
         print("Lütfen Düzgün Bir Şey Giriniz!")

while True:
    a=input("Öğrenci Numaranızı Giriniz :")
    b=input("Kimlik Numaranızın İlk Rakamı :")
    c=input("Kimlik Numaranızın Son Rakamı :")
    if c==0:
        c+=14
    elif b==0:
        b+=7
    elif a==0:
        a+=7
    print("Giriş Kodunuz Hazırlanıyor...")
    import time
    time.sleep(1)
    m=hesaplama(a,b,c)
    if m == None:
        print("")
    else:
        print("Giriş Kodunuz :",m)
    continue