#a = 10, a adalah variabel dengan nilai 10 

#tipe data: Angka satuan (integer)
data_integer = 1
""" print (type("data_integer")) """
print ("data : ", data_integer)
print ("- bertipe : ", type (data_integer))

#tipe data : Angka dengan koma (float)
data_float = 3.75
print ("data : ", data_float)
print ("- bertipe : ", type (data_float))

#tipe data : Kumpulan Karakter (String)
data_string = "wildan"
print ("data :", data_string)
print ("- bertipe : ", type (data_string))

#tipe data : biner true/false (Boolean)
data_boolean = True
print ("data : ", data_boolean)
print ("-bertipe : " , data_boolean)

##tipe data khusus

#bilangan kompleks
data_compleks = complex(5,6)
print("data : ", data_compleks)
print ("- bertipe :" , data_compleks )

#python bisa menggunakan tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double (10.5)
print("data : ", data_c_double)
print ("- bertipe :" , data_c_double)