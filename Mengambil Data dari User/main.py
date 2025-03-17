
#data yg dimasukan pasti string
data = input ("Masukan Data :")
print("data : ", data, ",type = ", type(data))

#jika kita ingin menggunakan integer atau float, 
angka = int(input("Masukan angka :", ))
angka = float(input("Masukan angka :", ))

print ("data = ", angka, "type=", type(angka))

#bagaimana dengan boolean?
biner = bool(int(input("Masukan nilai boolean : " )))
print ("data = ", biner,"type = ", type (biner))

#karena tidak bisa langsung menggunakan boolean, dicasting dulu ke integer (penambahan "int" di samping tulisan bool)