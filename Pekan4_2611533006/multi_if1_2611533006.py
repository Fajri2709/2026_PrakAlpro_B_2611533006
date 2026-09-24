# Buat file dengan nama multi_if1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh; ipk_1234
# Program ini menggunakan fungsi input()

umur_3006 = int(input("Input umur anda: "))
sim_3006 = input("Apakah Anda Sudah Punya Sim C (y/t): ")[0]

if umur_3006 >= 17 and sim_3006 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_3006 >= 17 and sim_3006 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_3006 < 17 and sim_3006 == 'y':
    print("Anda Belum Cukup Umur punya SIM")

if umur_3006 < 17 and sim_3006 != 'y':
    print("Anda Belum Cukup Umur bawa motor")