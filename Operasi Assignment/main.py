 # operasi assignment = operasi yg dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5 #ini adalah assignment
print ('nilai a : ', a)

a += 1 # ini sama kaya a = a + 1
print ('nilai a += 1, nilai a menjadi', a)

a-= 2 # ini sama kaya a = a - 1
print ('nilai a -= 2, nilai a menjadi', a)

a*= 4 # ini sama kaya a = a * 1
print ('nilai a *= 4, nilai a menjadi', a)

a/= 2 # ini sama kaya a = a / 1
print ('nilai a /= 2, nilai a menjadi', a)

#modulus
b = 10
print ('nilai b : ', b)

b %= 3 
print ('nilai b %= 3, nilai b menjadi : ', b)

#leftdivision
b = 10
print ('nilai b : ', b)

b //= 3 #floor division
print ('nilai b //= 3, nilai b menjadi : ', b)

a = 5 
print("nilai a = ", a)
a **= 3 # pangkat atau eksponen
print ("nilai a **= 3, nilai menjadi", a)

#operasi bitwise
# OR 
c = True
print ("\n nilai c : ",c)
c |= False
print ("nilai c |= False, nilai c menjadi", c)

c = False
print ("\n nilai c : ",c)
c |= False
print ("nilai c |= False, nilai c menjadi", c)

#AND
c = True
print ("\n nilai c : ",c)
c &= False
print ("nilai c &= False, nilai c menjadi", c)

c = True
print ("\n nilai c : ",c)
c &= True
print ("nilai c &= False, nilai c menjadi", c)

#XOR
c = True
print ("\n nilai c : ",c)
c ^= False
print ("nilai c ^= False, nilai c menjadi", c)

c = True
print ("\n nilai c : ",c)
c ^= True
print ("nilai c ^= True, nilai c menjadi", c)


#geser geser
d = 0b0100
print ("\nNilai d = ", format(d, '04b'))
d >>= 2
print ("nilai d >>= 2, nilai d menjadi ", format(d, '04b') )
d <<= 2
print ("nilai d <<= 2, nilai d menjadi ", format(d, '04b') )
