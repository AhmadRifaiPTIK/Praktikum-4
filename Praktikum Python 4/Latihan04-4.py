import math
import decimal
print("Perjalanan Kota A ke Kota B adalah 125 Km")

JarakKotaAKeKotaB = 125000

KecepatanDariKotaAKeKotaB = 62000 // 60

print("Perjalanan Kota B ke Kota C adalah 256 Km")

JarakKotaBKeKotaC = 256000

KecepatanDariKotaBKeKotaC = 70000 // 60

WaktuMulai = 360

WaktuIstirahat = 45

WaktuDariAkeB = JarakKotaAKeKotaB // KecepatanDariKotaAKeKotaB

WaktuDariBkeC = JarakKotaBKeKotaC // KecepatanDariKotaBKeKotaC

WaktuTotal = WaktuIstirahat + WaktuDariAkeB + WaktuDariBkeC

end_jam = WaktuMulai + WaktuTotal

WaktuSampai = end_jam / 60

print("lama dari kota A ke Kota B :",WaktuDariAkeB)

print("Lama dari kota B ke Kota C :",WaktuDariBkeC)

print("Lama Total perjalanana ditambah waktu istirahat adalah (dalam menit):",WaktuTotal)

print("Jam Berapa Pak Amir Sampai ?")

print("Pak Amir Sampai pada pukul :",WaktuSampai)
