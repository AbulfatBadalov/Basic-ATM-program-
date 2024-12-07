#Bankamat
import streamlit as st
while True:
  a=int(input("mebleg daxil edin: "))
  b=int(input("1.Pul kocurme Emeliyyati\n2.Cari Balans\n3Balans artirma\n4Cixis\n. "))
  if b==1:
     c=int(input("Ne qeder kocurme edeceksen? "))
     if c<=a:
      d=a-c #d-qaliq balans
      print(f"{c} Azn Kocuruldu")
      print(f"Qaliq Balans: {d}")
     else:
      print("Kifayet qeder vesait yoxdur.")
  elif b==2:
    print(f"Cari balans: {a}")
  elif b==3:
      e=int(input("Ne qeder artirma edeceksen? "))
      a=a+e
      print(f"{e} Azn artirma olundu.")
      print(f"Yeni balans:{a}")
  elif b==4:
    print("Emeliyyat sonlandi.\nHelelik")
    break
