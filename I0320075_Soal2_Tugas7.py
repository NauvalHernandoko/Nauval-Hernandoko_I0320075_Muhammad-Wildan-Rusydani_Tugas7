judul = "membuat program menggunakan fungsi numeric"
a = judul.center(80,"=")
print(a)

import math
nilai1 = float(input("masukkan nilai1: "))
nilai2 = float(input("masukkan nilai2: "))
nilai3 = float(input("masukkan nilai3: "))

nilaislrh = [nilai1, nilai2, nilai3]
print(nilaislrh)
print("Nilai max = ", max(nilai1, nilai2, nilai3))
print("Nilai min = ", min(nilai1, nilai2, nilai3))

rerata = (nilai1 + nilai2 + nilai3)/3
print("rerata nilai", rerata)
print("rerata bulat ke atas: ", math.ceil(rerata))
print("rerata bulat ke bawah: ", math.floor(rerata))

#memilih nilai secara random
import random
print("pilihan random: ", random.choice(nilaislrh) )

