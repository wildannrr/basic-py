#operasi boolean
#not, or, and, xor

# NOT
print ('==== NOT ====')
a = True
c = not a
print('Data a = ', a)
print('---NOT---')
print ('Data C = C', c)

# OR
# salah satunya benar, maka jawabannya benar (true)

print ('==== OR ====')
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)



# AND
# dua duanya harus benar (true)

print ('==== AND ====')
a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)



# XOR
# akan benar (true), jika hanya satu true. bisa false karna lebih dari satu true

print ('==== XOR ====')
a = True
b = False
c = a ^ b #tanda topi (^), merepresentasikan XOR
print(a, 'XOR', b, '=', c)