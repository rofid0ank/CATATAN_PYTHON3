# if, elif, else

# if, else
# Pengambilan keputusan (kondisi if else) tidak hanya digunakan untuk menentukan tindakan apa yang akan diambil sesuai dengan kondisi, tetapi juga digunakan untuk menentukan tindakan apa yang akan diambil/dijalankan jika kondisi tidak sesuai.Pada python ada beberapa statement/kondisi diantaranya adalah if, else dan elif Kondisi if digunakan untuk mengeksekusi kode jika kondisi bernilai benar.Kondisi if else adalah kondisi dimana jika pernyataan benar True maka kode dalam if akan dieksekusi, tetapi jika bernilai salah False maka akan mengeksekusi kode di dalam else.

# if, else
nama = 'rofi'
if nama == nama: # jika variabel nilainya true maka akan dieksekusi 
  print('benar, itu saya')
else: # jika variabel nilainya false tidak akan dieksekusi 
  print('salah, itu bukan saya')

# if, elif, else
nilai = 80
if nilai > 80:
  print('anda tidak mengikuti remedial')
elif nilai == 80: # mengecek jika variabel nilainya true maka akan dieksekusi 
  print('anda tidak mengikuti remedial')
else:
  print('anda harus mengikuti remedial')
