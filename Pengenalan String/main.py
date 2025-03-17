# membuat string

# (1.1) string dengan single quote
data = 'ini adalah string single quote'
print (data)

# (1.2) string dengan double quote
data = "ini adalah string double quote"
print (data)

# (1.3) menggabungkan single quote dan double quote atau sebaliknya
print ('"hai apa kabar?"')
print ("'kabar baik'")


# ***MENGGUNAKAN TANDA \ ***

# (2.1) membuat tanda ' menjadi string
print ('hari ini adalah hari jum\'at')
print ('g\'day, isn\'t ?' )

# backlash
# (2.2) membuat tanda (\) agar dapat tampil ketika di run menggunakan \ 
print ("C : \\ user \\ Wildan") # jadi double backlash, yang satu sebagai perintah, yg satunya lagi yg akan tampil ketika di run


# menggunakan \t sebagai tab
# (3.1) satu kali tab 
print ("wildan\t ganteng")
# (3.2) dua kali tab 
print ("wildan\t\t ganteng")

#backspace
# (4.1)
print ("wildan \b mewing")

# newline
#(5.1) baris baru (\n)
print ("ini baris pertama\nini baris kedua") # LF = Line Feed 
print ("ini baris ketiga\nini baris keempat") # CR = Carriage Return
print ("ini baris pertama\n\rini baris kedua") # CRLF = Line Feed Carriage Return


# *** STRING LITERAL ATAU RAW ***

# (1.1) Menggunakan raw string
print (r'C:\new \t\r\f\a folder: Wildan') # setelah memasukan raw string (r), jangan menambahkan spasi karna bakal error

# (2.1) Menggunakan literal string
print ( """
Nama : Wildan
Kelas : Reguler
""" )

# (3.1) multiline literal string dan raw
print (r"""
Nama : Wildan
Kelas : Reg B
Website : www.wildan.com\news """  )  