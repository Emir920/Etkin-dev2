print("Futbol takımına mat notu 85 üzeri erkek öğrenciler katılabilir.")
puan = int(input ("Matematik puanın kaç? "))
c = input ("Cinsiyetin nedir? ")
if puan < 0 or puan > 100 : print("Yanlış giriş")
else :
    if puan > 85 : print ("Puanın çok güzel")
    elif puan > 70 : print ("Puanın iyi")
    elif puan > 50 : print ("Geçmişsin")
    else : print ("Kalmışsın dostum.")


    if puan>85 and  (c.lower() in ["e","erkek"]):
        print("Futbol takımına girebilirsin")
    else : print("Takıma giremezsin")




"""
Eşitse/eşit mi          : a == b
Eşit değilse / eşit değil mi    : a != b
Küçükse / küçük mü      : a < b
Küçük veya eşitse   : a <= b
Büyükse         : a > b
Büyük ya da eşitse  : a >= b
ve              : and
veya                : or
değil               : not
öyle                : is
içindeyse           : in
!!! elif diğer şartların atlanmasıyla performans artışına katkı sağlar.


"""
