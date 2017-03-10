# -*- coding: utf-8 -*-
#0 1 2
#3 4 5
#6 7 8
#* 0 #
#0 için 11 1.satır 1.sütun
sozluk={"11":"0","12":"1","13":"2","21":"3","22":"4","23":"5","31":"6","32":"7","33":"8","41":"*","42":"9","43":"#"}
sifreMetin=raw_input("sifreMetin: ")
sayici=0
ikili=""
liste=[]
for i in sifreMetin:
    if sayici <2:
        ikili=ikili+i
        sayici=sayici+1
    if sayici==2:
        liste.append(sozluk[ikili])
        sayici=0
        ikili=""
print liste
