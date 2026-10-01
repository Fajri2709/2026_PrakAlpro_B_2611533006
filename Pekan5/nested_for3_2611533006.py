# Buat file dengan nama nested_for3_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan format input

batas_3006 = int(input("Masukkan nilai batas: "))
for i_3006 in range(batas_3006+1):
    for j_3006 in range(batas_3006+1):
        print(i_3006+j_3006, end="")
    print() # pindah ke baris selanjutnya