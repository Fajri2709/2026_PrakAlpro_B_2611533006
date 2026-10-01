# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan format input

tinggi_3006 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3006 %2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_3006 = tinggi_3006
    c_3006 = a_3006
    lebar_3006 = (2 * tinggi_3006) - 2

    for i_3006 in range(1, tinggi_3006 + 1):
        b_3006 = c_3006 + 1

        for j_3006 in range(1, lebar_3006 + 1):

            # Baris atas dan bawah
            if i_3006 == 1 or i_3006 == tinggi_3006:
                if j_3006 == 1 or j_3006 == lebar_3006:
                    print("#", end="")
                else:
                    print("=", end="")

            # Baris Isi
            else:
                if j_3006 == 1 or j_3006 == lebar_3006:
                    print("|", end="")
                else:
                    if j_3006 == c_3006:
                        print("<", end="")
                    elif j_3006 == b_3006:
                        print(">", end="")
                    elif j_3006 == (lebar_3006 - c_3006):
                        print("<", end="")
                    elif j_3006 == (lebar_3006 - c_3006 + 1):
                        print(">", end="")
                    elif j_3006 > b_3006 and j_3006 < (lebar_3006 - c_3006):
                        print(".", end="")
                    else:
                        print(" ", end="")

print()

# Logika asli Java
a_3006 -= 2

if a_3006 <= 0:
    c_3006 = (-a_3006) + 2
else:
    c_3006 = a_3006