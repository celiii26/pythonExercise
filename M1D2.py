### Part 1 ###

# No 1
x = 4
y = 3
z = 2
w = ((x + y * z)/(x * y)) ** z
print(w) # hasil nya menjadi tipe float 0.694444

# No 2
angka = int(input("Silahkan masukkan angka berapapun : "))
print(f"Kuadrat dari {angka} = {angka**2}")

# No 3
hari = 485
tahun , sisaHari = divmod(hari, 360)
bulan, sisaHari = divmod(sisaHari, 30)
minggu, sisaHari = divmod(sisaHari, 7)
print("%d tahun, %d bulan, %d minggu, %d hari" %(tahun, bulan, minggu, sisaHari))

# No 4
andiBudi = 49
rasioAndiBudi = 0.4
# andi + budi = 49, andi/budi = 0.4
budi = 49/1.4
andi = 49 - budi
print(f"Dua tahun lagi umur Andi {andi+2} dan Budi {budi+2}")

# No 5
jarakAB = 120
kecepatanAB = 60 + 40
waktuMenit = jarakAB / kecepatanAB * 60
jam, menit = divmod(waktuMenit, 60)
print(f"A & B akan tabrakan pada jam {9+jam} lebih {menit} menit")

# No 6
hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000
apel = int(input("Masukkan jumlah Apel : "))
jeruk = int(input("Masukkan jumlah Jeruk : "))
anggur = int(input("Masukkan jumlah Anggur : "))
print(f'''
Detail Belanja

Apel : {apel} x {hargaApel} = {apel*hargaApel}
Jeruk : {jeruk} x {hargaJeruk} = {jeruk*hargaJeruk}
Anggur : {anggur} x {hargaAnggur} = {anggur*hargaAnggur}

Total : {apel*hargaApel + jeruk*hargaJeruk + anggur*hargaAnggur}
''')

### PART 2 ###

# No 1
number = int(input("Masukkan angka : "))
if number % 2 == 0:
    print(f"Angka {number} tergolong bilangan Genap")
else:
    print(f"Angka {number} tergolong bilangan Ganjil")

# No 2
massa = int(input("Masukkan Massa (Kg) : "))
tinggi = int(input("Masukkan Tinggi (cm) : "))
print(f"Massa {massa} kg dan tinggi {tinggi/100} m")
imt = massa / ((tinggi/100)**2)
if imt < 18.5:
    print(f"IMT = {imt}, Berat badan kurang")
elif imt >= 18.5 and imt <= 24.9:
    print(f"IMT = {imt}, Berat badan ideal")
elif imt >= 25 and imt <= 29.9:
    print(f"IMT = {imt}, Berat badan berlebih")
elif imt >= 30 and imt <= 39.9:
    print(f"IMT = {imt}, Berat badan sangat berlebih")
else:
    print(f"IMT = {imt}, Obesitas")

# No 3
hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000
apel = int(input("Masukkan jumlah Apel : "))
jeruk = int(input("Masukkan jumlah Jeruk : "))
anggur = int(input("Masukkan jumlah Anggur : "))
total = apel*hargaApel + jeruk*hargaJeruk + anggur*hargaAnggur
print(f'''
Detail Belanja

Apel : {apel} x {hargaApel} = {apel*hargaApel}
Jeruk : {jeruk} x {hargaJeruk} = {jeruk*hargaJeruk}
Anggur : {anggur} x {hargaAnggur} = {anggur*hargaAnggur}

Total : {total}
''')
# Menghitung kembalian
uang = int(input("Masukkan jumlah uang : "))
if uang == total:
    print("Terima Kasih")
elif uang > total:
    print(f"Terima Kasih\n\nUang kembalian anda : {uang-total}")
else:
    print(f"Transaksi anda dibatalkan\n\nUangnya kurang sebesar {total-uang}")
