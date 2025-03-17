# (1). tugasnya ----0++++5----8++++11----- 
# (2). tugasnya ++++0----5++++8----11++++

# SOAL NO 1
print ("======================NO 1=====================")
inputUser = float (input("\nMasukan angka yg kurang dari 0 \n atau lebih dari 5 \n atau tidak kurang dari 8\n dan tidak boleh lebih dari 11 :  "))
kurangDari = inputUser < 0
print ("Kurang dari Nol :", kurangDari)

lebihDari = inputUser > 5
print ("Lebih dari Lima :", lebihDari)

ldSamaDengan = inputUser >= 8
print ("Lebih dari sama dengan 8 :", ldSamaDengan)

kdSamaDengan = inputUser <= 11
print ("Kurang dari sama dengan 11 :", kdSamaDengan)

isCorrect = kurangDari or kdSamaDengan
print (" Maka :", isCorrect)

print("=========================NO 2=================================")
#SOAL NO 2
inputUser = float (input("Masukan angka yg lebih dari 0 \n atau kurang dari 5\n atau kurang dari sama dengan 8\n dan lebih dari sama dengan 11 :  "))
ldNol = inputUser > 0 # ld = lebih dari
print ("Lebih dari Nol : ", ldNol )

kdLima = inputUser < 5 # kd = kurang dari 
print ( "Kurang dari Lima : ", kdLima)

kdsLapan = inputUser <= 8 # kds = kurang dari sama dengan
print ("Kurang dari sama dengan 8 : ", kdsLapan)

ldsSebelas = inputUser >= 11 # lds = lebih dari sama dengan
print ("Lebih dari sama dengan 11 : ", ldsSebelas)

isBenar = ldNol and ldsSebelas 
print ("Maka : ", isBenar)