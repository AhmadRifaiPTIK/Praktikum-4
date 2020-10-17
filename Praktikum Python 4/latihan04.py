import math
# Aplikasi penghitung tarif sewa

print("Aplikasi Penghitung Tarif Sewa Rental")
tarifSewaPertama = 200000
print("Tarif sewa 12 jam pertama",tarifSewaPertama)
tarifSewaSelanjutnya = 10000
print("Tarif sewa 1 jam selanjutnya",tarifSewaSelanjutnya)

waktuMulai = 06.00
waktuSelesai = math.ceil(23.50)
waktuSewa = waktuSelesai - waktuMulai

waktuSewaPertama = 12
waktuSewaTambahan = waktuSewa - waktuSewaPertama

biayaTambahan = waktuSewaTambahan*tarifSewaSelanjutnya
totalBiaya = tarifSewaPertama + biayaTambahan

print("Tarif sewa pertama: ",tarifSewaPertama)
print("Tarif sewa tambahan: ",biayaTambahan)
print("Total yang harus dibayar: ",totalBiaya)