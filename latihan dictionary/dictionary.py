# latihan dictionary


# library python
import os
from os import system
import string
import random
from random import choice

# template dictionary
template = {
    'nama':'nama',
    'kelas':'kelas',
    'jurusan':'jurusan'
}

system('cls') # membersihkan layar

# data siswa
data_siswa = {}

while True:
    # menggunakan template
    siswa = dict.fromkeys(template.keys())
    # memasukan nama siswa
    siswa['nama'] = input('nama siswa : ')
    # memasukan kelas
    siswa['kelas'] = input('kelas : ')
    # memasukan jurusan
    siswa['jurusan'] = input('jurusan : ')
    # membuat key dictionary random
    keys = ''.join(choice(string.ascii_uppercase) for x in range (6))
    # update dictionary
    data_siswa.update({keys:siswa})
    
    print(f"\n{'KEYS':<15} {'NAMA SISWA':<15} {'KELAS':<15} {'JURUSAN':<15}")        

    for data in data_siswa:
        key = data
        nama = data_siswa[key]['nama']
        kelas = data_siswa[key]['kelas']
        jurusan = data_siswa[key]['jurusan']

        print(f"{key:<15} {nama:<15} {kelas:<15} {jurusan:<15}")        
    print()
