# 1
print('----Mencari Celcius ke Fahreinheit----')
def celcius_ke_farheinheit(celcius):
    fahreinheit = (celcius * 9/5) + 32
    return fahreinheit 

print(celcius_ke_farheinheit (0))
print(celcius_ke_farheinheit (100))
print()

# 2
print('----Mencari Bilangan Genap----')
def is_genap(bil_genap): 
    return bil_genap %2 == 0
# Untuk memasukkan value
print(is_genap(4))
print(is_genap(7))
print()

# 3
print('----Melihat Keterangan Lulus atau Tidak Lulus----')
def nilai_kelulusan(nilai):
    if nilai >= 80:
        return 'Lulus'
    else :
        return 'Gagal'
    
 # Untuk n=mencetak value
print(nilai_kelulusan(80))   
print(nilai_kelulusan(60)) 

# 4
print('\n----Cetak Bilangan Genap----')
def bil_ganjil(angka):
    for i in range(1, angka, 2):
        print(i, end="")
# Untuk memasukkan value 
bil_ganjil(20)