import pyshark
cap = pyshark.FileCapture(' Kendi Wireshark tarama kodunun yolunu yazınız. ') #### Dikkat!!! #####
cap
engelleme = "Girilen numaralı paket engellenmiştir."
paketNo0 = cap[0]
paketNo1 = cap[1]
paketNo2 = cap[2]

tercih = str(input("Paket taramasını görmek ister misiniz?:(e/h):"))
if tercih=='e' :
   
    print (" ****** 0 Nolu Paket ***** \n",paketNo0)
    print ("-----------------------------------------------------------")
    print (" ***** 1 Nolu Paket ****** \n",paketNo1)
    print ("-----------------------------------------------------------")
    print (" ***** 12 Nolu Paket ****** \n",paketNo2)
else:
    exit

tercih1=str(input("""Engellemek istediğiniz Paket İsmi:\n1)paketNo0\n2)PaketNo1\n3)PaketNo2\n>>>"""))

if tercih1 == "1":
    print (engelleme)
elif tercih1 == "2":   
    print (engelleme)
elif tercih == '3':
    print (engelleme)
else:
    exit
