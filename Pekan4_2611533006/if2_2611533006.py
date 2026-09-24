# Buat file dengan nama if2_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh; ipk_1234
# Program ini menggunakan fungsi input()

ipk_3006 = float(input("Input IPK Anda = "))

if ipk_3006 > 2.75:
    print("Anda lulus Sangat Memuaskan dengan IPK " + str(ipk_3006))
else:
    print("Anda Tidak Lulus")
print("Program Selesai")