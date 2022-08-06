# dictionary
# dictionary terdiri dari 'key' dan 'value'

data = {
    # key  # value
    'nama':'rofidoank',
    'hobi':'membaca artikel'
}

# mengambil value
data['nama'] # cara ke 1
data.get('nama') # cara ke 2

# mengubah value
data['nama'] = 'rofi'

# menghapus dictionary
data.clear()

# menghapus key menggunakan del
del data['nama']

# mengecek apakah ada key di dictionary
cek = 'nama' in data
print(cek)

# mengambil seluruh key dan value
data.items()

# mengambil seluruh key nya saja
data.keys()

# mengambil seluruh value nya saja
data.values()

# menghapus key menggunakan pop
data.pop('nama')

# menghapus pasangan key dan value
data.popitem() # menghapus yang paling belakang

# mengupdate dictionary
data_lama = {
    'nama':'rofi'
}

data_lama.update({'nama':'ropi'})
