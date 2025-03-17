#For Loop - Perulangan

#for kondisi:
#    aksi

angka2_list = [1,2,3,4] # ini adalah list
print (angka2_list)

for i in angka2_list:
    print(f"i sekarang -> {i}")

print("End Program 1 \n")

#ini adalah range
angka2_range = range(5)

for i in angka2_range:
    print(f"i sekarang -> {i}")
print ("End Program 2 \n")

angka2_range = range (1,5) #angka 5 sebagai pembatas

for i in angka2_range:
    print(f"i sekarang -> {i}")
    print ('gua ganteng')

print ("End Program \n")
# Jangan ubah kode ini
dico = 750000
if dico > 500000:
    diskon = 0.1
    total_harga = dico - (dico*diskon)
else total_harga = dico:
print(total_harga)