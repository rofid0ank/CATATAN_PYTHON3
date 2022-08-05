# if, elif, else

# if
angka = 3
if angka > 0: # jika variabel nilai lebih besar dari 0 maka akan mengeksekusi 
  print('benar, angka 3 lebih besar dari angka 0')

# if, else
nama = 'rofi'
if nama == nama: # jika variabel nilainya true maka akan mengeksekusi 
  print('benar, itu saya')
else: # jika variabel nama nilainya false tidak akan dieksekusi 
  print('salah, itu bukan saya')

# if, elif, else
nilai = 80
if nilai > 80:
  print('anda tidak mengikuti remedial')
elif nilai == 80:
  print('anda tidak mengikuti remedial')
else:
  print('anda harus mengikuti remedial')
