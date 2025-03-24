def penjumlahan (a,b):
    return a+b
def pengurangan (a,b):
    return a-b
def perkalian (a,b):
    return a*b
def pembagian (a,b):
    if b != 0:
        return a/b
    else:
        print("pembagian tidak bisa mengggunakan 0")

print("----- Kalkulator Sederhana -----")
print("--------------------------------")

while True:
    print("Pilih Oprasi: ")
    print("1. penjumlahan")
    print("2. pengurangan ")
    print("3. perkalian ")
    print("4. pembagian ")
    print("5. keluar ")

    pilihan = input("masukkan pilihan 1/2/3/4/5 : ")

    if pilihan == 5:
        print("Anda keluar")
        break
    
    angka1 = float(input("Masukkan angka pertama : "))
    angka2 = float(input("Masukkan angka kedua : "))

    if pilihan == '1':
        hasil = (penjumlahan(angka1,angka2))
        print("hasil penjumlahan  =",hasil)
    elif pilihan == '2':
        hasil = int(pengurangan(angka1,angka2))
        print("hasil pengurangan  =",hasil)
    elif pilihan == '3':
        hasil = int(perkalian(angka1,angka2))
        print("hasil perkalian  =",hasil)
    elif pilihan == '4':
        hasil = int(pembagian(angka1,angka2))
        print("hasil pembagian  =",hasil)
