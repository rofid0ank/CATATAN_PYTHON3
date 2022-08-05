# Daftar format kode strftime()

'%a'  # hari dalam satu minggu (sun, mon)
'%A'  # Hari dalam satu minggu (sunday, monday)
'%w'  # Hari dalam satu minggu (0, 1)
'%d'  # hari dalam satu bulan  (01, 02)
'%-d' # Hari dalam satu bulan  (1, 2)
'%b'  # Bulan dalam satu tahun (jan, feb)
'%B'  # Bulan dalam satu tahun (january, february)
'%m'  # Bulan dalam satu tahun (01, 02)
'%-m' # Bulan dalam satu tahun (1, 2)
'%y'  # Tahun dalam satu abad  (00, 01)
'%-y' # Tahun dalam satu abad  (0, 1)
'%Y'  # Tahun dalam satu abad  (2002, 2003)
'%H'  # Jam dalam satu hari (00,01) sampai 23
'%-H' # Jam dalam satu hari (0,1) sampai 23
'%I'  # Jam dalam satu hari (00, 01) sampai 12
'%-I' # Jam dalam satu hari (0, 1) sampai 12
'%p'  # Siang atau malam (PM, AM) 
'%M'  # Menit dalam satu jam (00, 01)
'%-M' # Menit dalam satu jam (0, 1)
'%S'  # Detik dalam satu menit (00, 01)
'%-S' # Detik dalam satu menit (0, 1)

# Contoh penggunaan untuk menampilkan tanggal, bulan dan tahun sekarang
import datetime
from datetime import datetime

sekarang = datetime.now()

tanggal_bulan_tahun = sekarang.strftime('%d-%B-%Y')
print(tanggal_bulan_tahun)