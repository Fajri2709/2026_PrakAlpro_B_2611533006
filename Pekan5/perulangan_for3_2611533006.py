# Buat file dengan nama perulangan_for3_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan format input

ulang_3006 = int(input("Masukkan jumlah perulangan: "))

jumlah_3006 = 0
for i_3006 in range(1, ulang_3006 + 1):
    print(i_3006, end=" ")
    jumlah_3006 = jumlah_3006 + i_3006

    if i_3006 < ulang_3006:
        print(" + ", end=" ")
    else:
        print(" = ", jumlah_3006, end="")
print()
print("Jumlah =", jumlah_3006)