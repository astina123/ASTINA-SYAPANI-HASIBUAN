# Soal nomor 1
# List utama : kendaraan
Kendaraan = ["beat", "motor", "200cc", "hitam", "roda 2"]

# Mencetak isi dari list kendaraan
print(Kendaraan)

# Menambahkan value atau nilai di ujung list(pakai append())

# Proses append 1 (harga kendaraan)
Kendaraan.append ("19.000.000")

# Proses append (tipe kendaraan)
Kendaraan.append("matic")

# Cetak nilai kendaraan setelah perubahan
print(Kendaraan)

# Sisipkan nilai untuk nilai kendaraan 
Kendaraan.insert (2, "HONDA")

# Cetak hasil list akhirnya
print (Kendaraan)


# Soal nomor 2
Pilihan = int(input("""Pilih nomor pilihan:
1. Menghitung Luas Persegi
2. Menghitung Luas Lingkaran
3. Menghitung Luas Segitiga"""))

match pilihan:
    case 1:
        print("Menghitung Luas Persegi")
        s = int(input("Masukkan nilai sisi: ")) 
        luasPersegi = s * s
        print(f"Luas persegi dengan sisi {s} adalah {luasPersegi}")
    case 2:
        print("Menghitung Luas Lingkaran") 
        pi = 3.14
        r = int(input("Masukkan nilai jari-jari: "))
        luasLingkaran = pi * r ** 2
        print(f"Luas lingkaran dengan jari-jari {r} adalah {luasLingkaran}")
    case 3:
        print("Menghitung Luas Segitiga") 
        alas = int(input("Masukkan nilai alas: "))
        tinggi = int(input("Masukkan nilai tinggi: "))
        luasSegitiga = 1/2 * alas * tinggi
        print(f"LuasSegitiga dengan alas {alas} dan tinggi {tinggi} adalah {luasSegitiga}")

    case _:
        print("Input tidak valid")

