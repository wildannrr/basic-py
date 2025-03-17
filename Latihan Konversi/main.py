""#latihan konversi satuan temperature

#konversi temperature celcius ke temperature lain

print ("\n PROGRAM KONVERSI TEMPERATUR CELCIUS KE TEMPERATURE LAIN\n")

celcius = float (input('Masukan suhu dalam celcius : '))
print ("Suhu dalam celcius adalah : ", celcius, "Celcius")

#reamur
#rumusnya (4/5)C

reamur = (4/5) * celcius
print ("Suhu dalam reamur adalah : ", reamur, "Reamur")

#fahrenheit
#rumusnya (9/5) Celcius + 32
fahrenheit = ((9/5) * celcius) + 32
print ("Suhu dalam fahrenheit adalah : ", fahrenheit, "Fahrenheit" )


#kelvin 
#rumusnya celcius + 273
kelvin = celcius + 273 
print ("Suhu dalam kelvin adalah : ", kelvin, "Kelvin" )



""" KONVERSI TEMPERATURE REUMUR KE TEMPERATURE LAIN"""

print ("\n PROGRAM KONVERSI TEMPERATUR REUMUR KE TEMPERATURE LAIN\n")

reumur = float (input("Masukan suhu dalam temperature reumur : "))
print( "Suhu temperature reumur adalah :", reumur, "Reumur" )

#reumur ke celcius
#rumusnya (5/4 )R

celcius = (5/4)* reumur
print ("Suhu dalam celcius adalah : ", celcius, "Celcius")

#reumur ke farenheit
#rumusnya (9/5)C + 72

fahrenheit = (9/5) * celcius + 72
print ("Suhu dalam farenheit adalah : ", fahrenheit, "Farenheit")

#reumur ke kelvin
#rumusnya (5/4)R + 273

kelvin = (5/4) * reumur + 273
print ("Suhu dalam kelvin adalah : ", kelvin, "Kelvin")
""

"""KONVERSI FARENHEIT KE SUHU LAIN"""


print ("\n PROGRAM KONVERSI TEMPERATUR CELCIUS KE TEMPERATURE LAIN\n")

fahrenheit = float(input("Masukan Suhu Dalam Farenheit : "))

print ("Suhu dalam Fahrenheit adalah : ", fahrenheit, "Fahrenheit")


#Farenheit ke Celcius
#Rumusnya 5/9 (f-32)

celcius = 5/9 * (fahrenheit - 32)
print ("Suhu dalam celcius adalah : ", celcius, "Celcius")

#fahrenheit ke reumur
#rumusnya 4/9 (F-32)

reumur = 4/9 * (fahrenheit - 32)
print ("Suhu dalam reumur adalah :", reumur, "Reumur")


#fahrenheit ke kelvin
#rumusnya (f-32)5/9 +273.15

kelvin - (fahrenheit - 32) * 5/9 + 273.15
print ("Suhu dalam kelvin adalah : ", kelvin, "Kelvin")


"""KONVERSI TEMPERATUR KELVIN KE TEMPERATUR LAIN"""

print ("\n PROGRAM KONVERSI SUHU KELVIN KE SUHU LAINNYA \n ")

kelvin = float (input("Masukan suhu Kelvin-nya :"))
print ("Suhu dalam kelvin adalah : ", kelvin, "Kelvin")

#kelvin ke celcius 
#rumusnya k - 273

celcius = 273 - kelvin
print ("Suhu dalam celcius adalah : ", celcius, "Celcius")

#kelvin ke reumur
#rumusnya 4/5 (k-273)

reamur = (kelvin - 273) * 4/5
print ("Suhu dalam reumur adalah : ", reumur, "Reumur")

#kelvin ke fahrenheit
#rumusnya  9/5 + 273 (Kelvin - 273.15)

fahrenheit = (kelvin - 273.15) * 9/5 + 273.15
