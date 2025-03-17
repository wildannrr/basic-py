# latihan 

# Kalkulator sederhana 

print ("==========================")
print ("KALKULATOR SEDERHANA")
print ("==========================")
print (20*"=")
print("Kalkulator sederhana")
print (20*"=" + "\n")

angka_1 = float(input("masukan angka 1 = "))
operator = input("operator (x,+,-,/)")
angka_2 = float(input("Masukan angka 2 = "))

#percabangannya

if operator =="+":
    hasil = angka_1 + angka_2
    print (f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print (f"hasilnya adalah {hasil}")
elif operator == "X" or operator == "*" :
    hasil = angka_1 * angka_2
    print (f"hasilnya adalah {hasil}")
elif operator == "/" or operator == ":" :
    hasil = angka_1 / angka_2
    print (f"hasilnya adalah {hasil}")

print ("End")