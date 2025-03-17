# Latihan komparasi dan logika
# membuat gabungan area rentang dari angka 
# ++++++3---------------10+++++++

inputUser = float (input("Masukan angka yg bernilai kurang dari 3\n atau lebih dari 10 : "))
#++++3----
#memeriksa angka yg kurang dari 3
isKurangDari = inputUser < 3
print ("< 3 : ",isKurangDari)

#-----10++++
#memeriksa angka yg lebih dari 10
inputUser = float (input("Masukan angka yg lebih dari 10 atau kurang dari 3 : "))
isLebihDari = inputUser > 10
print ("> 10 : ", isLebihDari)

"""
#kurang dari sama dengan 3 <=
#memeriksa angka yg kurang dari sama dengan 3 
inputUser = float (input("Masukan angka yg kurang dari sama dengan 3 atau lebih dari 10 :"))
kurdarSamaDengan = inputUser <= 3
print  ("<= :" ,kurdarSamaDengan)

#lebih dari sama dengan 10 >=
#memeriksa angka yg lebih dari sama dengan 10

inputUser = float (input("Masukan angka yg kurang atau lebih dari sama dengan 10 : "))
lebdarSamaDengan = inputUser >= 10
print (">= : " , lebdarSamaDengan)
"""


#+++3------10++++
#menggabungkan 
isCorrect = isKurangDari or isLebihDari
print ("Angka yg anda masukan : ", isCorrect)

#irisan
#+++3-----10++++

#---3+++
inputUser = float (input("Masukan angka lebih dari 3\n dan tidak lebih dari  10 : "))
lebihDari = inputUser > 3 
print ("Lebih dari : ", lebihDari)

#---10
inputUser = float (input("Masukan angka lebih dari 3\n dan tidak lebih dari  10 : "))
kurangDari = inputUser < 10 
print ("Lebih dari : ", kurangDari)

irisan = kurangDari and lebihDari
print ("Maka hasil dari irisannya adalah = ", irisan)