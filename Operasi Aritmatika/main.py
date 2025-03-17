#operasi aritmatika
a = 50
b = 13

#operasi tambah + 
hasil = a + b
print (a, "+", b, "=", hasil)


#operasi pengurangan - 
hasil = a - b
print (a, "-", b, "=", hasil)



#operasi perkalian * 
hasil = a * b
print (a, "*", b, "=", hasil)

#operasi pembagian / 
hasil = a / b
print (a, "/", b, "=", hasil)

#operasi eksponen (pangkat) **
hasil = a ** b
print (a, "**", b, "=", hasil)

#operasi modulus % 
#mengambil sisa dari perkalian 
#contoh : a = 11, b = 3
#3*3 = 9, sisa 2, 2 tersebut yg jadi jawaban, kalau pas, berarti 0
hasil = a % b
print (a, "*", b, "=", hasil)


#operasi floor division // ( kebalikan dari modulus)
# contoh 10 / 3 = 3.3333, dibulatkan menjadi 3 dan tidak memperdulikan sisanya 
hasil = a // b
print (a, "//", b, "=", hasil)

#prioritas operasi 

"""
    urutan yang bakal di eksekusi duluan 
        1. ()
        2. eksponen [ pangkat **]
        3. perkalian dan teman temannya * / ** % //
        4. pertambahan dan pengurangan        

"""

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print ( x, "**", y, "*", z, "+", x, "/", y, "-", y, "%", z, "//", x, "=", hasil)