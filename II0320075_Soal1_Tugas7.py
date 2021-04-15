judul = "membuat program membuat password"
a = judul.center(80,"=")
print(a)
nama_depan = input("Masukkan nama depan anda: ")
nama_belakang = input("Masukkan nama belakang anda: ")
asal = input("Masukkan asal anda: ")
tgllahir = input("Masukkan 1 angka terakhir tanggal lahir anda: ")
d = nama_depan.capitalize()
b = nama_depan.capitalize()
a = asal.capitalize()
password = ""
if(len(d) > 2 ):
    password += d[0:2]
else:
    password += d

if(len(b) > 2):
    password += b[:2]
else:
    password += b

if(len(a) > 2):
    password += a[:2]
else:
    password += a

password += tgllahir

print("string pasword anda adalah: ", password)
